import sys
from google import genai

client = genai.Client()

def main():
    print("=== Interactive Gemini Study Assistant ===")
    
    # 1. Multi-Line Notes Input
    print("\nPaste your lecture notes below.")
    print("(Press Control + D when you are done pasting):\n")
    lecture_text = sys.stdin.read().strip()

    if not lecture_text:
        print("\nNo notes provided. Exiting.")
        return

    # 2. Topic & Depth Customization
    print("\n" + "="*40)
    print("Select Output Style:")
    print("1. Concise Summary & Key Takeaways")
    print("2. Detailed Concept Breakdown")
    print("3. Interactive Quiz Mode")
    print("="*40)
    choice = input("Enter choice (1-3): ").strip()

    if choice == "1":
        prompt = f"Provide a concise summary and 3 key takeaways for these notes:\n\n{lecture_text}"
        response = client.models.generate_content(model="gemini-3.6-flash", contents=prompt)
        print("\n--- Summary ---")
        print(response.text)

    elif choice == "2":
        prompt = f"Provide a detailed concept breakdown with explanations and examples for these notes:\n\n{lecture_text}"
        response = client.models.generate_content(model="gemini-3.6-flash", contents=prompt)
        print("\n--- Detailed Breakdown ---")
        print(response.text)

    elif choice == "3":
        # 3. Interactive Quiz Mode
        print("\nGenerating your quiz question...")
        quiz_prompt = (
            f"Based on these notes, generate 1 challenging short-answer conceptual question. "
            f"Do NOT include the answer.\n\nNotes:\n{lecture_text}"
        )
        question = client.models.generate_content(model="gemini-3.6-flash", contents=quiz_prompt).text
        
        print("\n--- Quiz Question ---")
        print(question)
        user_answer = input("\nYour Answer: ")

        print("\nEvaluating your answer...")
        eval_prompt = (
            f"Question: {question}\n"
            f"User's Answer: {user_answer}\n"
            f"Original Notes: {lecture_text}\n\n"
            f"Evaluate if the user's answer is correct, explain why, and give brief constructive feedback."
        )
        feedback = client.models.generate_content(model="gemini-3.6-flash", contents=eval_prompt)
        print("\n--- Feedback ---")
        print(feedback.text)

    else:
        print("Invalid choice selected.")

if __name__ == "__main__":
    main()

