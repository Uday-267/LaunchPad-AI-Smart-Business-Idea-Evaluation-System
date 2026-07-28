import logging

from google import genai

from config import Config
from services.prompt import build_prompt


class GeminiService:
    """
    Handles communication with Google Gemini AI.
    """

    def __init__(self):

        if not Config.GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY not found in .env"
            )

        self.client = genai.Client(
            api_key=Config.GEMINI_API_KEY
        )

        self.model = Config.GEMINI_MODEL

    # ======================================================
    # Analyze Startup
    # ======================================================

    def analyze_startup(
        self,
        startup_name,
        startup_idea,
        target_audience,
        business_model,
        product_features
    ):

        try:

            prompt = build_prompt(
                startup_name,
                startup_idea,
                target_audience,
                business_model,
                product_features
            )

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )

            if not response:

                return {
                    "success": False,
                    "message": "Gemini returned no response."
                }

            if not response.text:

                return {
                    "success": False,
                    "message": "Empty response received from Gemini."
                }

            return {
                "success": True,
                "result": response.text
            }

        except Exception as e:

            logging.exception(e)

            return {
                "success": False,
                "message": str(e)
            }


# ======================================================
# Singleton Object
# ======================================================

gemini_service = GeminiService()