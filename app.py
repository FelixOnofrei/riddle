import streamlit as st


def check_password_level1():
    """Returns `True` if the user had the correct password for level 1."""

    # Check if level 1 password is already verified in session state
    if "level1_unlocked" in st.session_state:
        return st.session_state["level1_unlocked"]

    # If not, show the password input and check it
    password_input = st.text_input(
        "What am I?",
        type="password",
        key="password_input_level1"
    )

    if st.button("Submit", key="submit_level1"):
        if password_input.lower() == st.secrets["password_level1"]:
            st.session_state["level1_unlocked"] = True
            return True
        else:
            st.error("😕 Not today...")
            return False

    # First-time visitor, password not yet submitted
    return False

def check_password_level2():
    """Returns `True` if the user had the correct password for level 2."""

    # Check if level 2 password is already verified in session state
    if "level2_unlocked" in st.session_state:
        return st.session_state["level2_unlocked"]

    # If not, show the password input and check it
    password_input = st.text_input(
        "What opens the secret door?",
        type="password",
        key="password_input_level2"
    )

    if st.button("Submit", key="submit_level2"):
        if password_input.lower() == st.secrets["password_level2"]:
            st.session_state["level2_unlocked"] = True
            return True
        else:
            st.error("😕 Not today...")
            return False

    # Password not yet submitted
    return False

def check_password_level3():
    """Returns `True` if the user had the correct password for level 3."""

    # Check if level 3 password is already verified in session state
    if "level3_unlocked" in st.session_state:
        return st.session_state["level3_unlocked"]

    # If not, show the password input and check it
    password_input = st.text_input(
        "What is buried in the sand?",
        type="password",
        key="password_input_level3"
    )

    if st.button("Submit", key="submit_level3"):
        if password_input.lower() == st.secrets["password_level3"]:
            st.session_state["level3_unlocked"] = True
            # Immediately show the final offer page
            st.session_state["show_final_offer"] = True
            st.experimental_rerun()
            return True
        else:
            st.error("😕 Not today...")
            return False

    # Password not yet submitted
    return False

# Initialize session state for current level if not exists
if "current_level" not in st.session_state:
    st.session_state["current_level"] = 1

# Initialize session state for final offer page
if "show_final_offer" not in st.session_state:
    st.session_state["show_final_offer"] = False

# Main app
# Check if we should show the final offer page
if st.session_state["show_final_offer"]:
    st.title("I'm gonna make you an offer you can't refuse")

    # Display the video from secrets
    st.video(st.secrets["youtube_link"])
else:
    # Different title for each level
    if st.session_state["current_level"] == 1:
        st.title("Level 1: Leave the gun")
    elif st.session_state["current_level"] == 2:
        st.title("Level 2: Take the Cannoli")
    elif st.session_state["current_level"] == 3:
        st.title("Level 3: The Offer")

# Handle level 1
if st.session_state["current_level"] == 1 and not st.session_state["show_final_offer"]:
    if check_password_level1():
        # User entered the correct password for level 1
        st.success("🎉 Congratulations! You've unlocked Level 1!")

        # Display level 1 content
        with st.container():
            st.balloons()

            # Button to proceed to level 2
            if st.button("Take the Cannoli"):
                st.session_state["current_level"] = 2
                st.experimental_rerun()

# Handle level 2
elif st.session_state["current_level"] == 2 and not st.session_state["show_final_offer"]:
    if check_password_level2():
        # User entered the correct password for level 2
        st.success("🎉 Congratulations! You've unlocked Level 2!")
        st.write("A man who doesn't spend time with his family can never be a real man.")

        # Display level 2 content
        with st.container():
            st.balloons()

            # Button to proceed to level 3
            if st.button("The Offer"):
                st.session_state["current_level"] = 3
                st.experimental_rerun()

# Handle level 3
elif st.session_state["current_level"] == 3 and not st.session_state["show_final_offer"]:
    if check_password_level3():
        # User entered the correct password for level 3
        st.success("🎉 Congratulations! You've unlocked Level 3!")

