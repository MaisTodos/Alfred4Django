from alfred.models.choice import ChoiceField


def test_to_choice():
    obj = ChoiceField(choices=[
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    ])

    assert obj.choices == [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    ]
