from project import choose_story, generate_story,get_user_words
def main():
    test_choose_story()
    test_get_user_words()
    test_generate_story()

def test_choose_story():
    story = choose_story()
    assert isinstance(story, str)
    assert story != ""

def test_get_user_words(monkeypatch):
    story = "Once upon a [adjective] [noun], there lived a [adjective] [noun]."
    user_inputs = ["beautiful", "forest", "mighty", "lion"]
    monkeypatch.setattr('builtins.input', lambda _: user_inputs.pop(0))
    assert get_user_words(story) == ["beautiful", "forest", "mighty", "lion"]

def test_generate_story():
    story = "In a [adjective] land lived a [noun]."
    words = []
    assert generate_story(story, words) == story

if __name__ == '__main__':
    main()
