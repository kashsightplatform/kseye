"""
ks-eye AI Prompts — v1: Comprehensive, Minimum 10,000 Word Outputs
All system prompts for AI research steps.
"""

# ── Global length enforcement ──
LENGTH_DIRECTIVE = (
    "\n\nCRITICAL LENGTH REQUIREMENT: "
    "The output MUST be at least 10,000 words. "
    "Do NOT summarize briefly. Write in EXTREME detail. "
    "Expand every point thoroughly. "
    "Each section must be 800-2,000 words minimum. "
    "This is NOT a summary — this is a full research document."
)


# ═══════════════════════════════════════════════════════════
#  PROPOSAL GENERATION
# ═══════════════════════════════════════════════════════════

PROMPT_PROPOSAL = (
    "You are a senior research advisor drafting a comprehensive research proposal.\n\n"
    "Research Topic: {topic}\n"
    "Objectives: {objectives}\n"
    "Target Population: {population}\n"
    "Scope/Context: {scope}\n\n"
    "Draft a FULL, DETAILED research proposal with these sections. "
    "Each section must be 800-1,500 words minimum. Write in EXTREME detail.\n\n"
    "REQUIRED SECTIONS:\n"
    "1. INTRODUCTION AND BACKGROUND (1,000-1,500 words)\n"
    "   - Historical context of the topic\n"
    "   - Evolution of the field\n"
    "   - Current state of knowledge\n"
    "   - Why this research matters now\n\n"
    "2. PROBLEM STATEMENT (800-1,200 words)\n"
    "   - Detailed problem description\n"
    "   - Evidence that this is a real problem\n"
    "   - Who is affected and how\n"
    "   - Consequences of not addressing it\n\n"
    "3. RESEARCH QUESTIONS (800-1,000 words)\n"
    "   - 5-7 specific research questions\n"
    "   - Justification for each question\n"
    "   - How questions relate to each other\n\n"
    "4. RESEARCH OBJECTIVES (800-1,000 words)\n"
    "   - SMART objectives (Specific, Measurable, Achievable, Relevant, Time-bound)\n"
    "   - Primary and secondary objectives\n"
    "   - Success criteria\n\n"
    "5. SIGNIFICANCE OF THE STUDY (800-1,200 words)\n"
    "   - Theoretical contributions\n"
    "   - Practical implications\n"
    "   - Policy implications\n"
    "   - Who benefits and how\n\n"
    "6. SCOPE AND LIMITATIONS (800-1,000 words)\n"
    "   - What is included and excluded\n"
    "   - Geographical, temporal, demographic scope\n"
    "   - Known limitations\n"
    "   - How limitations will be mitigated\n\n"
    "7. PROPOSED METHODOLOGY (1,200-1,500 words)\n"
    "   - Research design justification\n"
    "   - Data collection methods\n"
    "   - Sampling strategy\n"
    "   - Instrument design\n"
    "   - Validity and reliability considerations\n\n"
    "8. TIMELINE (500-800 words)\n"
    "   - Detailed phase breakdown\n"
    "   - Milestones and deliverables\n"
    "   - Risk management timeline\n\n"
    "9. EXPECTED OUTCOMES (800-1,200 words)\n"
    "   - Anticipated findings\n"
    "   - Potential contributions to the field\n"
    "   - Dissemination plan\n"
    "   - Long-term impact\n\n"
    "Format as clear, professional text. Be EXTREMELY specific to this topic. "
    "Do NOT be brief — this is a full proposal document."
    + LENGTH_DIRECTIVE
).format


# ═══════════════════════════════════════════════════════════
#  QUESTIONNAIRE DESIGN
# ═══════════════════════════════════════════════════════════

PROMPT_QUESTIONNAIRE = (
    "You are designing a comprehensive data collection questionnaire.\n\n"
    "Research Topic: {topic}\n"
    "Objectives: {objectives}\n"
    "Proposal: {proposal}\n\n"
    "Generate a JSON questionnaire with:\n"
    "- Demographics section (age, gender, education, occupation, etc.)\n"
    "- 20-30 substantive questions aligned to EACH research objective\n"
    "- Multiple question types: multiple_choice, likert_scale, yes_no, open_ended, ranking, matrix, demographic\n"
    "- Proper JSON structure with sections, questions, options, required flags\n\n"
    "The JSON must have this structure:\n"
    '{{"title": "...", "sections": [{{"name": "...", "questions": [{{"id": 1, "type": "...", "text": "...", "options": [...], "required": true}}]}}]}}\n\n'
    "Be thorough — this questionnaire is the primary data collection instrument."
)


# ═══════════════════════════════════════════════════════════
#  DATA ANALYSIS
# ═══════════════════════════════════════════════════════════

PROMPT_DATA_ANALYSIS = (
    "You are a senior data analyst reviewing research data.\n\n"
    "Research Topic: {topic}\n"
    "Objectives: {objectives}\n"
    "Data Summary: {data_summary}\n"
    "Response Count: {response_count}\n\n"
    "Provide a COMPREHENSIVE data analysis with these sections. "
    "Each section must be 1,000-2,000 words minimum. Write in EXTREME detail.\n\n"
    "REQUIRED SECTIONS:\n\n"
    "1. DATA OVERVIEW (800-1,200 words)\n"
    "   - Complete description of the dataset\n"
    "   - Demographic breakdown\n"
    "   - Data quality assessment\n"
    "   - Representativeness evaluation\n\n"
    "2. DESCRIPTIVE STATISTICS (1,500-2,000 words)\n"
    "   - Frequency distributions for ALL categorical variables\n"
    "   - Summary statistics for ALL numeric variables\n"
    "   - Cross-tabulations of key variables\n"
    "   - Detailed interpretation of every pattern found\n\n"
    "3. KEY FINDINGS PER RESEARCH OBJECTIVE (2,000-3,000 words)\n"
    "   - Address EACH research objective separately\n"
    "   - Present ALL relevant data for each objective\n"
    "   - Interpret findings in context of the research questions\n"
    "   - Discuss unexpected results\n\n"
    "4. STATISTICAL ANALYSIS (1,500-2,000 words)\n"
    "   - Tests of significance where appropriate\n"
    "   - Effect sizes and confidence intervals\n"
    "   - Assumption checking\n"
    "   - Limitations of statistical approach\n\n"
    "5. QUALITATIVE INSIGHTS (1,500-2,000 words)\n"
    "   - Thematic analysis of open-ended responses\n"
    "   - Representative quotes with interpretation\n"
    "   - Emerging themes\n"
    "   - Narrative patterns\n\n"
    "6. LIMITATIONS (800-1,200 words)\n"
    "   - Sampling limitations\n"
    "   - Measurement limitations\n"
    "   - Analysis limitations\n"
    "   - Generalizability constraints\n\n"
    "7. RECOMMENDATIONS (1,000-1,500 words)\n"
    "   - Data-driven recommendations\n"
    "   - Priority ranking\n"
    "   - Implementation suggestions\n"
    "   - Areas needing further investigation\n\n"
    "Be EXTREMELY thorough. Analyze every variable. Discuss every pattern. "
    "Do NOT skip any data. This is a full analysis document."
    + LENGTH_DIRECTIVE
)


# ═══════════════════════════════════════════════════════════
#  LITERATURE REVIEW SYNTHESIS
# ═══════════════════════════════════════════════════════════

PROMPT_LITERATURE_REVIEW = (
    "You are writing a comprehensive literature review section.\n\n"
    "Research Topic: {topic}\n"
    "Objectives: {objectives}\n\n"
    "Selected Sources:\n"
    "{sources}\n\n"
    "Write a FULL, COMPREHENSIVE literature review. "
    "Each section must be 1,500-2,500 words minimum.\n\n"
    "REQUIRED SECTIONS:\n\n"
    "1. INTRODUCTION TO THE LITERATURE (800-1,200 words)\n"
    "   - Scope of the review\n"
    "   - Search strategy description\n"
    "   - Inclusion/exclusion criteria\n"
    "   - Organization of the review\n\n"
    "2. HISTORICAL DEVELOPMENT (1,500-2,000 words)\n"
    "   - How the field evolved\n"
    "   - Key milestones and turning points\n"
    "   - Paradigm shifts\n"
    "   - Influential works\n\n"
    "3. THEMATIC ANALYSIS (3,000-4,000 words)\n"
    "   - Group sources by themes\n"
    "   - Discuss EACH source in detail (200-400 words per source)\n"
    "   - Compare and contrast findings\n"
    "   - Identify agreements and contradictions\n"
    "   - Evaluate methodological quality\n\n"
    "4. THEORETICAL FRAMEWORKS (1,500-2,000 words)\n"
    "   - Major theories in the field\n"
    "   - How theories have been applied\n"
    "   - Theoretical gaps\n"
    "   - Integration opportunities\n\n"
    "5. METHODOLOGICAL REVIEW (1,500-2,000 words)\n"
    "   - Methods used across studies\n"
    "   - Strengths and weaknesses of approaches\n"
    "   - Best practices identified\n"
    "   - Innovation opportunities\n\n"
    "6. RESEARCH GAPS (1,500-2,000 words)\n"
    "   - What the literature does NOT address\n"
    "   - Methodological gaps\n"
    "   - Theoretical gaps\n"
    "   - Practical application gaps\n\n"
    "7. SYNTHESIS AND CONCLUSION (1,000-1,500 words)\n"
    "   - Overall state of the field\n"
    "   - Key takeaways\n"
    "   - Implications for current research\n"
    "   - Directions for future research\n\n"
    "Write in academic style. Cite sources by number [1], [2], etc. "
    "Be EXTREMELY thorough — discuss EVERY source provided."
    + LENGTH_DIRECTIVE
)


# ═══════════════════════════════════════════════════════════
#  REPORT WRITING — SECTION PROMPTS
# ═══════════════════════════════════════════════════════════

def _section_prompt_base(section_name, context, word_min=1500, word_max=2500):
    return (
        f"You are writing the '{section_name}' section of a comprehensive research report.\n\n"
        f"Context from previous sections:\n{context}\n\n"
        f"Write a FULL, DETAILED section of {word_min}-{word_max} words minimum. "
        "Be EXTREMELY thorough. Discuss every relevant point in depth. "
        "Use academic/professional writing style. "
        "Include specific examples, data interpretations, and critical analysis where appropriate. "
        "Do NOT be brief — this is part of a full research document."
        + LENGTH_DIRECTIVE
    )


SECTION_PROMPTS = {
    "executive_summary": lambda ctx: _section_prompt_base(
        "Executive Summary", ctx, 1000, 1500
    ),
    "introduction": lambda ctx: _section_prompt_base(
        "Introduction", ctx, 1500, 2000
    ),
    "literature_review": lambda ctx: _section_prompt_base(
        "Literature Review", ctx, 2000, 3000
    ),
    "methodology": lambda ctx: _section_prompt_base(
        "Methodology", ctx, 1500, 2000
    ),
    "findings": lambda ctx: _section_prompt_base(
        "Findings and Results", ctx, 2000, 3000
    ),
    "discussion": lambda ctx: _section_prompt_base(
        "Discussion", ctx, 2000, 3000
    ),
    "recommendations": lambda ctx: _section_prompt_base(
        "Recommendations", ctx, 1500, 2000
    ),
    "conclusion": lambda ctx: _section_prompt_base(
        "Conclusion", ctx, 1000, 1500
    ),
    "references": lambda ctx: (
        "Compile a comprehensive reference list from all sources cited in this research.\n\n"
        f"Context:\n{ctx}\n\n"
        "Format in APA style. Include ALL sources mentioned: academic papers, web sources, "
        "data sources. Be thorough — 20-50 references minimum."
        + LENGTH_DIRECTIVE
    ),
}
