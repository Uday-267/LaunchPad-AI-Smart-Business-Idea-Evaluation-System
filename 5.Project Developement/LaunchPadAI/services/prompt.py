def build_prompt(
    startup_name,
    startup_idea,
    target_audience,
    business_model,
    product_features
):
    """
    Builds a structured prompt for Google Gemini AI
    to analyze startup ideas.
    """

    prompt = f"""
You are an experienced Startup Consultant, Venture Capital Advisor,
Business Strategist, and Market Research Expert.

Analyze the startup idea below professionally.

==================================================
STARTUP DETAILS
==================================================

Startup Name:
{startup_name}

Startup Idea:
{startup_idea}

Target Audience:
{target_audience}

Business Model:
{business_model}

Key Features:
{product_features}

==================================================
YOUR TASK
==================================================

Generate a complete startup validation report.

The report MUST follow this exact structure.

# 🚀 Startup Validation Report

## 📊 Startup Scores

Provide scores out of 10.

| Category | Score |
|----------|-------|
| Viability | X/10 |
| Innovation | X/10 |
| Market Potential | X/10 |
| Execution Feasibility | X/10 |
| Overall Rating | X/10 |

After the table explain each score briefly.

--------------------------------------------------

## 💪 SWOT Analysis

### Strengths

- point
- point
- point

### Weaknesses

- point
- point
- point

### Opportunities

- point
- point
- point

### Threats

- point
- point
- point

--------------------------------------------------

## 📈 Market Analysis

Explain

• Current Market Demand

• Industry Growth

• Future Trends

• Customer Segments

--------------------------------------------------

## 🏆 Competitor Analysis

List at least five competitors.

For each competitor explain

• Company Name

• Strength

• Weakness

Present as a table.

--------------------------------------------------

## 💰 Revenue & Monetization

Suggest

• Revenue Model

• Pricing Strategy

• Additional Revenue Sources

--------------------------------------------------

## 🚀 Growth Strategy

Provide

Short-Term Goals

Medium-Term Goals

Long-Term Goals

--------------------------------------------------

## 📢 Customer Acquisition Strategy

Recommend

• Social Media

• SEO

• Influencer Marketing

• Paid Ads

• Partnerships

--------------------------------------------------

## ⚠ Business Risks

Identify

• Financial Risks

• Technical Risks

• Operational Risks

• Market Risks

--------------------------------------------------

## 💡 Recommendations

Give at least ten actionable recommendations.

--------------------------------------------------

## ⭐ Final Verdict

State whether this startup is

Excellent

Good

Average

High Risk

Provide a short explanation.

==================================================

Formatting Rules

Use proper Markdown headings.

Use tables where appropriate.

Use bullet points.

Keep explanations concise and professional.

Do NOT include any extra introduction outside this format.
"""

    return prompt