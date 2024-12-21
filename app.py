import streamlit as st
import os
from dotenv import load_dotenv
from mysql.connector import connection
from streamlit_option_menu import option_menu


st.set_page_config(page_title="CRUD OPERATION",layout="wide")

load_dotenv(".env")

# Placeholder for CRUD functionality
st.header(" **Welcome to the CRUD App** ")
st.write(" **Implement CRUD operations with Azure Database.** ")


#conecting to azure mysql flexible server database

cnx = connection.MySQLConnection(
        user="mysqladmin", 
        password=os.getenv("password"),
        host="myfirst-mysql-webapp.mysql.database.azure.com",
        port=3306, 
        database="demo1", 
        ssl_ca="azure_certificate/DigiCertGlobalRootG2.crt.pem"
    )


cursor = cnx.cursor()
def main():
    col1,col2 = st.columns(2)
    with col1:
        st.link_button(label="Linkedin 📧",url="https://www.linkedin.com/in/beasumit/")
    st.divider()
    with col2:
        st.link_button(label="Portfolio 🧑🏻‍🏫",url="https://sumit-portfolio-ds.netlify.app/")
    
    st.sidebar.header("Action Bar",divider=True)
    option = st.sidebar.selectbox(label=" **Select Opeartion** ",options=["Insert","Read","Update","Delete"])
    st.sidebar.divider()
    st.sidebar.text("Made By Sumit Kumar 📟")
    
    #insert
    if option == "Insert":
        st.subheader(" **Insert Into MyTable** ✏️ ")
        st.write(" -> _Insert new records into MyTable_ ")
        Name = st.text_input(label="Enter Name Here..")
        Property  = st.text_input(label="Enter Property Here..")
        if st.button("Submit"):
            sql = "insert into mytable(name,Property) values (%s,%s)"
            val = (Name,Property)
            cursor.execute(sql,val)
            cnx.commit()
            st.success("Data Inserted Sucessfully 🥳 ")
            st.balloons()
    #read
    elif option == "Read":
        st.subheader(" **Read Data** 📖 ")
        st.write("-> _Read existing records_ ")
        cursor.execute("select * from mytable;")
        data = cursor.fetchall()
        for row in data:
            st.code(row,language='mysql') 
    #update
    elif option == "Update":
        st.subheader(" **Update Existing Data** ✍🏻")
        st.write("-> _Update records_")
        st.write(" **Select What you want to update** ")
        id = st.number_input(label="Select ID",min_value=1,step=1)
        name = st.text_input(label="Write the Owner Name Here 👪")
        Property = st.text_input(label="Write the Name of Property Here 💳")
        if st.button("SUBMIT"):
            sql = "update mytable set name =%s, property =%s where id=%s"
            val = (name,Property,id)
            cursor.execute(sql,val)
            cnx.commit()
            st.success("Data Updated Sucessfully 🥳")
            st.snow()
    #delete
    elif option == "Delete":
        st.subheader(" **Delete Data** 💥")
        st.write("- Delete records")
        id  = st.number_input(label="Select The ID for Which you Want to Delete the Record For.",min_value=1,step=1)
        if st.button("CONFORMATION"):
            sql = "delete from mytable where id=%s"
            val = (id,)
            cursor.execute(sql,val)
            cnx.commit()
            st.success("Data Removed From The DataBase 👍🏻")
            st.snow()
        
if __name__ == "__main__":
    main()