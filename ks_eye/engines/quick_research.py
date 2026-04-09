"""
ks-eye Quick Online Research — AI-Powered Full Scraping Mode
Uses AI to scrape, analyze, and summarize in one shot.
"""

import json
from datetime import datetime

from ks_eye.engines.tgpt_engine import run_tgpt
from ks_eye.engines.scholar_search import comprehensive_search
from ks_eye.ui import console


def quick_online_research(query, max_sources=30, provider="sky"):
    """
    Fully AI-powered research: scrapes web + academic sources,
    AI analyzes everything and produces a research brief.

    Args:
        query: Research query
        max_sources: Maximum sources to gather
        provider: AI provider to use

    Returns:
        Research brief dict with findings, sources, summary
    """
    results = {
        "query": query,
        "timestamp": datetime.now().isoformat(),
        "mode": "quick_online",
    }

    # Step 1: Scrape sources
    console.print("[cyan]🔍 Scraping online sources...[/cyan]")
    sources = comprehensive_search(query, max_sources=max_sources)
    results["sources"] = sources
    results["source_count"] = len(sources)
    console.print(f"[green]✓ Found {len(sources)} sources[/green]")

    if not sources:
        results["status"] = "error"
        results["message"] = "No sources found"
        return results

    # Step 2: AI analyzes all sources
    console.print("[cyan]🤖 AI analyzing sources...[/cyan]")
    sources_summary = "\n".join([
        f"[{i+1}] {s.get('title', '')}\n    Source: {s.get('source', '')}\n    Summary: {s.get('snippet', '')}"
        for i, s in enumerate(sources[:20])
    ])

    ai_prompt = (
        "You are a senior research analyst and academic writer. I will give you a list of "
        "academic and web sources about a topic. Your job is to produce a COMPREHENSIVE "
        "research brief of MINIMUM 10,000 WORDS.\n\n"
        "CRITICAL REQUIREMENT: The output MUST be at least 10,000 words. "
        "Do NOT summarize briefly. Write in EXTREME detail. Expand every point thoroughly.\n\n"
        "REQUIRED STRUCTURE:\n\n"
        "1. EXECUTIVE SUMMARY (500-800 words)\n"
        "   - Full overview of the research landscape\n"
        "   - Key themes and their significance\n"
        "   - Major contributions in the field\n\n"
        "2. COMPREHENSIVE SYNTHESIS (3,000-4,000 words)\n"
        "   - Combine ALL key findings from every source into a coherent narrative\n"
        "   - Discuss each finding in depth with context and background\n"
        "   - Compare and contrast different sources' conclusions\n"
        "   - Identify patterns, trends, and shifts in understanding\n"
        "   - Provide historical context where relevant\n\n"
        "3. KEY FINDINGS — DETAILED ANALYSIS (2,000-3,000 words)\n"
        "   - List 15-25 most important findings (NOT 5-10)\n"
        "   - For EACH finding provide:\n"
        "     • Detailed explanation (200-300 words per finding)\n"
        "     • Supporting evidence from sources\n"
        "     • Implications and significance\n"
        "     • Limitations and caveats\n\n"
        "4. METHODOLOGICAL ANALYSIS (1,000-1,500 words)\n"
        "   - Research methods used across sources\n"
        "   - Strengths and weaknesses of each approach\n"
        "   - Comparative analysis of methodologies\n"
        "   - Recommendations for future research design\n\n"
        "5. RESEARCH GAPS (1,000-1,500 words)\n"
        "   - Detailed analysis of what's missing from current research\n"
        "   - Underexplored areas and why they matter\n"
        "   - Methodological gaps\n"
        "   - Theoretical gaps\n"
        "   - Practical application gaps\n\n"
        "6. RECOMMENDATIONS (1,000-1,500 words)\n"
        "   - Specific, actionable recommendations for researchers\n"
        "   - Priority areas for future study\n"
        "   - Funding and resource allocation suggestions\n"
        "   - Policy implications\n\n"
        "7. CRITICAL EVALUATION (1,000-1,500 words)\n"
        "   - Overall quality assessment of the literature\n"
        "   - Source reliability analysis\n"
        "   - Bias detection and conflict of interest analysis\n"
        "   - Strength of evidence across sources\n\n"
        "8. CONCLUSION (500-800 words)\n"
        "   - Summary of the state of the field\n"
        "   - Most critical next steps\n"
        "   - Final assessment\n\n"
        f"Sources:\n{sources_summary}\n\n"
        "Write a FULL, DETAILED, COMPREHENSIVE research brief. "
        "MINIMUM 10,000 WORDS. Do not be brief. Expand every section thoroughly. "
        "This is NOT a summary — this is a full research document."
    )

    analysis = run_tgpt(
        message=ai_prompt,
        provider=provider,
        system_prompt=f"You are analyzing research on: {query}",
        timeout=180,
    )

    if analysis:
        results["status"] = "ok"
        results["ai_analysis"] = analysis
        results["message"] = "Quick online research complete."
    else:
        results["status"] = "partial"
        results["ai_analysis"] = "AI analysis failed. Sources are still available for manual review."
        results["message"] = "Sources found but AI analysis unavailable."

    return results


def format_quick_report(result):
    """Format quick research result as readable text"""
    lines = []
    lines.append("=" * 80)
    lines.append(f"QUICK ONLINE RESEARCH REPORT".center(80))
    lines.append("=" * 80)
    lines.append("")
    lines.append(f"Query: {result.get('query', 'N/A')}")
    lines.append(f"Date: {result.get('timestamp', 'N/A')[:19]}")
    lines.append(f"Sources Found: {result.get('source_count', 0)}")
    lines.append(f"Status: {result.get('status', 'unknown')}")
    lines.append("")

    # Sources table
    sources = result.get("sources", [])
    if sources:
        lines.append("SOURCES")
        lines.append("-" * 78)
        for i, s in enumerate(sources[:20], 1):
            lines.append(f"  [{i}] {s.get('title', 'Untitled')}")
            lines.append(f"      Source: {s.get('source', '?')} | Type: {s.get('type', '?')} | Reliability: {s.get('reliability', '?')}")
            if s.get("url"):
                lines.append(f"      URL: {s['url']}")
            if s.get("snippet"):
                lines.append(f"      Summary: {s['snippet'][:150]}")
            lines.append("")

    # AI Analysis
    analysis = result.get("ai_analysis", "")
    if analysis:
        lines.append("")
        lines.append("=" * 80)
        lines.append("AI ANALYSIS".center(80))
        lines.append("=" * 80)
        lines.append("")
        lines.append(analysis)

    lines.append("")
    lines.append("=" * 80)
    lines.append(f"End of Quick Research Report — ks-eye v{__import__('ks_eye').__version__}")
    lines.append("=" * 80)

    return "\n".join(lines)
