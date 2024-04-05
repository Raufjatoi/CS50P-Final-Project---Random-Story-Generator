import random
import re

def main():
    print('\t\t\t Random Story Generator ')
    chosen_story = choose_story()  # Choosin the story randomly
    words = get_user_words(chosen_story)  # Passin the chosen story to get_user_words
    if not words:
        return 'Please provide words'

    generated_story = generate_story(chosen_story, words)  # Pass the chosen story to generate_story
    print(generated_story)

def choose_story():
    stories = [
        "In a distant land, there was a [adjective] [noun] named [name]. "
        "[name] was famous for [action_ing] in the [place]. "
        "One day, [name] encountered a [adjective] [creature] while [action_ing]. "
        "The [creature] seemed [adjective], but [name] was not afraid. "
        "With [name]'s [adjective] courage, they [action] the [creature] and saved the [place].",

        "Deep in the heart of a magical forest lived a [adjective] [animal]. "
        "This [animal] loved to [verb] all day long. "
        "One sunny morning, the [animal] stumbled upon a [adjective] [object]. "
        "Curiosity got the better of them, and they decided to [verb] it. "
        "Suddenly, everything changed!"
    ]

    return random.choice(stories)

def get_user_words(story):
    words = []

    placeholders = re.findall(r"\[(\w+(?: \w+)*)\]", story)
    for placeholder in placeholders:
        prompt = "Enter " + placeholder + ": "
        word = input(prompt)
        words.append(word)

    return words

def generate_story(story, words):
    placeholders = re.findall(r"\[(\w+(?: \w+)*)\]", story)
    for word, placeholder in zip(words, placeholders):
        story = story.replace("[" + placeholder + "]", word, 1)
    return story


if __name__ == "__main__":
    main()
