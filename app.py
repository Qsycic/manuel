import streamlit as st

st.title("Manuel and The Magic Fox")

if "step" not in st.session_state:
    st.session_state.step = "c1"

step = st.session_state.step

# ----------------- C1 -----------------
if step == "c1":
    st.write("""Hello! This is the 'Manuel and The Magic Fox' Choose Your Own Adventure story! 
(made by Ryland Frazier 
original story by Ekaterina Sedia
THIS IS NOT AT ALL FULLY TRUE TO THE ORIGINAL STORY I HAVE TRIED TO STAY TRUE BUT HAVE ALTERED SOME PARTS TO PROVIDE YOU WITH A BETTER EXPERIENCE AND OVERALL A FUN STORY!)""")

    st.write("===================================")

    st.write("""You are Manuel a boy who lives in New Mexico. You are returning home from your Uncle's house on a reservation. You are trying to return home before your Mother as she has disliked your Uncle ever since your father died instead of him during a war. While rushing home you spot some animal prints leading off trail. Do you (A) follow them or (B) continue home.""")

    if st.button("A"):
        st.session_state.step = "c2_follow"
        st.rerun()

    if st.button("B"):
        st.session_state.step = "c2_home"
        st.rerun()

# ----------------- C2 FOLLOW -----------------
elif step == "c2_follow":
    st.write("You decide to follow the prints and find a beautiful fox that is whimpering at a rabbit hole, looking hungry. Do you (A) give it some food you brought with you or (B) do you leave for home?")

    if st.button("A"):
        st.session_state.step = "c3_fox"
        st.rerun()

    if st.button("B"):
        st.session_state.step = "c2_home"
        st.rerun()

# ----------------- C3 FOX -----------------
elif step == "c3_fox":
    st.write("""You give the fox the remainders of your lunch, and it happily eats it up! You return home before going upstairs. You quickly fall asleep and wake up to a crashing sound! You hurry downstairs and find your Mother having a stroke!. You get your neighbors to help, and you get her stable though she is paralyzed from the waist down. She insists you go to school, so you do but the teacher lets you go halfway as he has. I've heard of your Mother's condition. You return home, and your Mother tells you a nice girl helped her while you were gone. You meet this girl and she introduces herself as Tomiko and that she had been hiding in the desert after escaping a relocation center. You two quickly become friends and you let her stay at your house. You do end up getting suspiscous as she acts very nervous you go through her stuff and find a fox skin. Do you A take it or B leave it.""")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("A"):
            st.session_state.step = "ending_take"
            st.rerun()

    with col2:
        if st.button("B"):
            st.session_state.step = "ending_best"
            st.rerun()

# ----------------- C2 HOME -----------------
elif step == "c2_home":
    st.write("You hurry home quickly, saying hello to your Mother and going upstairs, having made it just in time! You fall asleep as you are exhausted, only to be woken up by a crash. Hurrying downstairs, you find your mother on the floor having a stroke. Do you (A) go get help or (B) try to help her yourself")

    if st.button("A"):
        st.session_state.step = "c3_neighbors"
        st.rerun()

    if st.button("B"):
        st.session_state.step = "ending_bad"
        st.rerun()

# ----------------- C3 NEIGHBORS -----------------
elif step == "c3_neighbors":
    st.write("You hurry out and get your neighbors and they help put her into a somewhat stable state though she remains paralized from the waste down. Despite you wanting to help her around the house she insists you go to school. Do you (A) respect her wishes and go to school or (B) remain home.")

    if st.button("A"):
        st.session_state.step = "ending_neutral"
        st.rerun()

    if st.button("B"):
        st.session_state.step = "ending_good"
        st.rerun()

# ----------------- ENDINGS -----------------
elif step == "ending_take":
    st.write("You decide to take the fox skin and hide it in your room. She, at night, comes in asking if you've seen it to which you respond by lying that you hadn't. She sees through this and runs off right before you caved and gave it back to her. She returns the next morning with bloody hands and explains she was able to wear the skin to become a fox and she was the fox from earlier. Her hands were bloody since she had tried to dig a hole in the rough hard adobe dirt without her fox claws. You give her back her fox skin, accept her and live happily ever after. THE END reload the page to retry.(NOTE: this is almost fully the original ending and is probably either the 2nd or 3rd best. I am going to say that I wish that I could have had more endings and choices especially here but I simply do not have the time. I hope you had fun and thank you.)")

elif step == "ending_best":
    st.write("You decide to leave the fox skin and ask her about it. She nervously and shyly explains she is able to become a fox by putting on the skin. She also says that she was the fox you fed earlier. You, noticing her discomfort, tell her you are fine with it and you her and your Mother live happily ever after. THE END (Congratulations on finding the ending that in my opinion is the best!)")

elif step == "ending_good":
    st.write("You stay and help her until she makes a full recovery, and you live happily ever after! THE END reload to try again (this is the 2nd best ending in my opinion and the easiest undoubtedly good ending to get)")

elif step == "ending_neutral":
    st.write("You head to school and they allow you to return home after learning of your situation. You learn to take care of your mother and live on. THE END reload the page to retry.")

elif step == "ending_bad":
    st.write("You attempt to help her but sadly you don't know how to perform emergency medical tactics and she succumbs to the stroke. THE END reload the page to try again.")

# ----------------- RESET -----------------
st.write("---")
if st.button("Restart"):
    st.session_state.step = "c1"
    st.rerun()
