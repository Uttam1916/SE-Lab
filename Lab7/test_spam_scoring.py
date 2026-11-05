from hypothesis import given
from hypothesis import strategies as st
from spam_scoring import first_link, sender_domain, shout_ratio


# Test 1: sender_domain
@given(st.text())
def test_sender_domain_no_crash(email):
    sender_domain(email)


# Test 2: first_link
@given(st.text())
def test_first_link_no_crash(text):
    first_link(text)


# Test 3: shout_ratio
@given(st.text())
def test_shout_ratio_no_crash(text):
    shout_ratio(text)
