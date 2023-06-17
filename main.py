import openai

openai.api_key = "insert-your-key-here"


def get_updated_plan(description, schedule, preference, original_plan, notice, feedback):
    """
    Call OpenAI API to generate a study plan based on the given information.

    Parameters:
        description: str, course description and objective
        schedule: str, course schedule
        preference: str, individual preferences
        original_plan: str, original study plan
        notice: str, notice to students
        feedback: str, feedback from learner
    """
    print('Generating answer...')
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        temperature = 0.5,
        max_tokens = 500,
        messages = [
            {"role": "system", "content": "You are a study plan update system."},
            {"role": "system", "content": "You are given the following course description:"},
            {"role": "user", "content": description},
            {"role": "system", "content": "You are given the following course schedule:"},
            {"role": "user", "content": schedule},
            {"role": "system", "content": "You are given the following individual preferences:"},
            {"role": "user", "content": preference},
            {"role": "system", "content": "You are given the following original study plan:"},
            {"role": "user", "content": original_plan},
            {"role": "system", "content": "You are given the following notice to students:"},
            {"role": "user", "content": notice},
            {"role": "system", "content": "You are given the following feedback from learner:"},
            {"role": "user", "content": feedback},
            {"role": "system", "content": "You are asked to generate a study plan update based on the given information."},
            {"role": "system", "content": "Just write out the revised plan and don't talk."},
            ]
    )
    answer = completion.choices[0]["message"]["content"]
    return answer
