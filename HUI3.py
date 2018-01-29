constant = 0.371
coef = 1.371

dictHUI3 = {'Vision':         [1.00, 0.98, 0.89, 0.84, 0.75, 0.61],
            'Hearing':        [1.00, 0.95, 0.89, 0.80, 0.74, 0.61],
            'Speech':         [1.00, 0.94, 0.89, 0.81, 0.68],
            'Ambulation':     [1.00, 0.93, 0.86, 0.73, 0.65, 0.58],
            'Dexterity':      [1.00, 0.95, 0.88, 0.76, 0.65, 0.56],
            'Emotion':        [1.00, 0.95, 0.85, 0.64, 0.46],
            'Cognition':      [1.00, 0.92, 0.95, 0.83, 0.60, 0.42],
            'Pain':           [1.00, 0.96, 0.90, 0.77, 0.55]}

def get_score(vision, hearing, speech, ambulation, dexterity, emotion, cognition, pain):
    """
    :param vision:
    :param hearing:
    :param speech:
    :param ambulation:
    :param dexterity:
    :param emotion:
    :param cognition:
    :param pain:
    :return:
    """

    if not(vision in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Value for vision must be between 1 and 6, inclusive.')
    if not(hearing in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Value for hearing must be between 1 and 6, inclusive.')
    if not(speech in [1, 2, 3, 4, 5]):
        raise ValueError('Value for speech must be between 1 and 5, inclusive.')
    if not(ambulation in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Value for ambulation must be between 1 and 6, inclusive.')
    if not(dexterity in [1, 2, 3, 4, 5,6]):
        raise ValueError('Value for dexterity must be between 1 and 6, inclusive.')
    if not(emotion in [1, 2, 3, 4, 5]):
        raise ValueError('Value for emotion must be between 1 and 5, inclusive.')
    if not(cognition in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Value for cognition must be between 1 and 6, inclusive.')
    if not(pain in [1, 2, 3, 4, 5]):
        raise ValueError('Value for pain must be between 1 and 5, inclusive.')

    response = coef

    response *= dictHUI3['Vision'][vision - 1]
    response *= dictHUI3['Hearing'][hearing - 1]
    response *= dictHUI3['Speech'][speech - 1]
    response *= dictHUI3['Ambulation'][ambulation - 1]
    response *= dictHUI3['Dexterity'][dexterity - 1]
    response *= dictHUI3['Emotion'][emotion - 1]
    response *= dictHUI3['Cognition'][cognition - 1]
    response *= dictHUI3['Pain'][pain - 1]

    response -= constant

    return response
