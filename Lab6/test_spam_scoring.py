from spam_scoring import classify, filter_inbox, inbox_status, score_message


def test_word_scoring_branches():
    # Spam word, lowercase non-spam word, long uppercase word,
    # and short uppercase word.
    assert score_message("FREE! hello HELLO ABC", False, 0) == 3


def test_empty_message_and_link_count_branches():
    assert score_message("", False, 0) == 0
    assert score_message("", False, 2) == 1
    assert score_message("", False, 4) == 4


def test_known_sender_clamping_branches():
    # Score becomes negative and is clamped to zero.
    assert score_message("", True, 0) == 0

    # Score remains positive after subtracting three.
    assert score_message("FREE FREE", True, 0) == 1


def test_classification_branches():
    assert classify(8) == "spam"
    assert classify(4) == "suspicious"
    assert classify(3) == "clean"


def test_filter_inbox_empty():
    assert filter_inbox([]) == {
        "spam": 0,
        "suspicious": 0,
        "clean": 0,
    }


def test_filter_inbox_all_categories():
    messages = [
        ("FREE WINNER PRIZE ALERT", False, 4),
        ("FREE WINNER", False, 0),
        ("hello there", False, 0),
    ]

    assert filter_inbox(messages) == {
        "spam": 1,
        "suspicious": 1,
        "clean": 1,
    }


def test_inbox_status_empty():
    assert (
        inbox_status(
            {
                "spam": 0,
                "suspicious": 0,
                "clean": 0,
            }
        )
        == "empty"
    )


def test_inbox_status_flooded():
    assert (
        inbox_status(
            {
                "spam": 3,
                "suspicious": 1,
                "clean": 1,
            }
        )
        == "flooded"
    )


def test_inbox_status_noisy():
    assert (
        inbox_status(
            {
                "spam": 1,
                "suspicious": 1,
                "clean": 1,
            }
        )
        == "noisy"
    )


def test_inbox_status_healthy():
    assert (
        inbox_status(
            {
                "spam": 1,
                "suspicious": 2,
                "clean": 2,
            }
        )
        == "healthy"
    )
