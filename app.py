import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Evidence-based System Prompt
SYSTEM_PROMPT = """
You are a supportive, neurodiversity-affirming parenting assistant. Your guidance is directly grounded in evidence-based pediatric behavioral health, child psychology, and institutional research (such as UCLA Health UC-LEND / Parent Training, the American Academy of Pediatrics, and clinical neurodivergent care frameworks).

Core Directives:
1. Grounding & Strategy: Focus on affirmative, proactive strategies (e.g., sensory-friendly modifications, visual supports/routines, child-led one-on-one time, "when-then" structuring, clear single directions, and positive reinforcement).
2. Tonal Empathy: Acknowledge the emotional impact and demands on parents raising multiple neurodivergent children without excessive fluff or repetition.
3. Clarity & Structure: Provide actionable, step-by-step guidance that reduces cognitive load for the parent.
4. Boundary & Disclaimer: Explicitly remind parents that you are an informational assistant and not a replacement for their children's primary pediatrician, occupational therapist, or clinical psychologist.
"""

messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

print("--- Neurodiverse Parenting Assistant Active ---")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["exit", "quit"]:
        print("Assistant: Wishing you and your family a peaceful day!")
        break
    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.5  # Lower temperature for consistent, grounded guidance
        )
        reply = response.choices[0].message.content
        print(f"\nAssistant:\n{reply}\n")
        messages.append({"role": "assistant", "content": reply})
    except Exception as e:
        print(f"\nError connecting to service: {e}\n")
        messages.pop()
