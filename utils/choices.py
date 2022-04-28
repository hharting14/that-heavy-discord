"""Choices for the Machine Learning classifier"""

"""The model works only with numbers so the data has to be passed as integers."""


COUNTRY = (
    (0, 'United States'),
    (1, 'England'),
    (2, 'Germany'),
    (3, 'France'),
)

INSTRUMENT = (
    (0, 'Guitar'),
    (1, 'Drums'),
    (2, 'Bass'),
)

DECADE = (
    (80, "80's"),
    (90, "90's"),
    (0, "00's"),
    (10, "10's"),
)

MOOD = (
    (0, 'Reflective'),
    (1, 'Relaxed'),
    (2, 'Angry'),
    (3, 'Energetic'),
)

TOPIC = (
    (0, 'War'),
    (1, 'Politics'),
    (2, 'Religion'),
    (3, 'History'),
    (4, 'Other'),
)
