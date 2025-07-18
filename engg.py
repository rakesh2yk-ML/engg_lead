import mysql.connector
import streamlit as st

try:
    # ✅ Connect to MySQL using Streamlit secrets
    conn = mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"]
    )
    cursor = conn.cursor()

    # ✅ Convert input_data DataFrame to a tuple
    data_tuple = tuple(input_data.iloc[0])

    # ✅ Proper INSERT query (not commented)
    insert_query = """
        INSERT INTO leads_data (
            district, `12th_percentage`, pcm_score, jee_main_appeared, jee_score,
            preferred_branch, scholarship_required, source, counselling_done, follow_up_count
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    # ✅ Execute query
    cursor.execute(insert_query, data_tuple)
    conn.commit()

    st.success("✅ Lead saved to database!")

except Exception as e:
    st.error(f"❌ Error saving to DB: {e}")

finally:
    cursor.close()
    conn.close()
