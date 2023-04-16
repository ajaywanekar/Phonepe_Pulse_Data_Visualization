import mysql.connector as sql
import streamlit as st
from streamlit_player import st_player
import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = 'browser'

connection = sql.connect(
    host="localhost",
    database="phonepe",
    user="root",
    password="",

)
mycursor = connection.cursor(buffered=True)

st.set_page_config(page_title = "PhonePe",layout="wide")

st.title("📱 PHONEPE PULSE DATA VISUALIZATION ")


choice = st.sidebar.selectbox("phonepe Pulse Dashboard",("🏠Home", "📊Data_Visualization", "🧒About"))

#Home
if choice == "🏠Home":
    col1, col2, col3 = st.columns([1, 1, 2])
    col1.image("plogo2.jpg")
    #col2.image("pulseg.gif")
    col2.image("pulse2.gif")
    st.subheader("🖊About Phonepe")
    st.write('''The Indian digital payments story has truly captured the world's imagination. From the largest towns to the remotest villages,
              there is a payments revolution being driven by the penetration of mobile phones and data.
                PhonePe Pulse is your window to the world of how India transacts with interesting trends,
              deep insights and in-depth analysis based on our data put together by the PhonePe team.''')
    st_player("https://www.youtube.com/watch?v=c_1H6vivsiA&embeds_euri=https%3A%2F%2Fwww.phonepe.com%2F&feature=emb_imp_woyt")
    st.subheader("🔸About Dashboard")
    st.write('''The Dashboard is created based on the data available on phonepe pulse github, the link is below''')
    st.write("Phonepe Pulse [Github](https://github.com/PhonePe/pulse)")
    st.subheader("App Created By Ajay Wanekar")
    st.write("[linkedin](https://www.linkedin.com/in/ajay-wanekar-245a50230/) ")
    st.write("[Github](https://github.com/ajaywanekar)")
    st.subheader("🔸Technologies Used")
    st.write("Github Cloning")
    st.write("Python")
    st.write("Pandas")
    st.write("MySQL")
    st.write("Plotly")
    st.write("Streamlit")


elif choice == "📊Data_Visualization":
    choice1 = ("🗺️State_visual","🗺️District_visual")
    select1 = st.sidebar.selectbox("Select View:", choice1)
    YEAR = ['2018', '2019', '2020', '2021', '2022']
    year = st.sidebar.selectbox("Select a year:", YEAR)
    QUARTER = ['1', '2', '3', '4']
    quarter = st.sidebar.selectbox("Select Quarter:", QUARTER)
    def data_fetching():

        mycursor.execute("SELECT * FROM phonepe.a_transaction")
        myresult1 = mycursor.fetchall()
        at = pd.DataFrame(myresult1, columns=['id', 'State', 'Year', 'Quarter', 'Type', 'Count', 'Amount'])

        mycursor.execute("SELECT * FROM phonepe.a_users")
        myresult2 = mycursor.fetchall()
        au = pd.DataFrame(myresult2, columns=['id', 'State', 'Year', 'Quarter', 'Brand', 'Count', 'Percentage'])

        mycursor.execute("SELECT * FROM phonepe.m_transaction")
        myresult3 = mycursor.fetchall()
        mt = pd.DataFrame(myresult3, columns=['id', 'State', 'Year', 'Quarter', 'District', 'Count', 'Amount'])

        mycursor.execute("SELECT * FROM phonepe.m_users")
        myresult4 = mycursor.fetchall()
        mu = pd.DataFrame(myresult4, columns=['id', 'State', 'Year', 'Quarter', 'District', 'Users'])

        mycursor.execute("SELECT * FROM phonepe.t_transaction")
        myresult5 = mycursor.fetchall()
        tt = pd.DataFrame(myresult5, columns=['id', 'State', 'Year', 'Quarter', 'District', 'Count', 'Amount'])

        mycursor.execute(("SELECT * FROM phonepe.t_users"))
        myresult6 = mycursor.fetchall()
        tu = pd.DataFrame(myresult6, columns=['id', 'State', 'Year', 'Quarter', 'District', 'Users'])

        connection.close()

        return at, au, mt, mu, tt, tu

    at, au, mt, mu, tt, tu = data_fetching()

    def Mapvisual():
        selected = st.selectbox(
            options=['Transaction', 'User'],
            label='geovisualization'
        )

        if selected == "Transaction":
                df1 = mt.groupby(['State', 'Year', 'Quarter'], as_index=False).sum()
                df1 = df1.query(f"Year == {year} & Quarter == {quarter}")
                df1 = df1[['State', 'Amount']]

                fig1 = px.choropleth(df1,
                                     geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                     featureidkey='properties.ST_NM',
                                     locations='State',
                                     color='Amount',
                                     hover_data=['State', 'Amount'],
                                     projection="robinson",
                                     color_continuous_scale='Plasma_r',
                                     range_color=(12, 0))
                fig1.update_geos(fitbounds='locations', visible=False)
                fig1.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

                st.plotly_chart(fig1)

                st.write(df1)

        if selected == "User":
                df3 = mu.groupby(['State','Year','Quarter'], as_index=False).sum()
                df3 = df3.query(f"Year =={year} & Quarter =={quarter}")
                df3 = df3[['State', 'Users']]

                fig3 = px.choropleth(df3,
                                     geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                     featureidkey='properties.ST_NM',
                                     locations='State',
                                     color='Users',
                                     hover_data=['State', 'Users'],
                                     projection="robinson",
                                     color_continuous_scale='Viridis_r',
                                     range_color=(12, 0))
                fig3.update_geos(fitbounds='locations', visible=False)
                fig3.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
                st.plotly_chart(fig3)

                st.write(df3)


    #mapvisual()

    def Topvisual():
        selected = st.selectbox(
            options=['Top Transaction', 'Top User'],
            label='District wise visualization'
        )

        if selected == "Top Transaction":
            df2 = pd.read_csv("top_transcation.csv")
            df2 = df2.query(f"Year =={year} & Quarter =={quarter}")
            fig2 = px.sunburst(df2, path=['State', 'District'], values='Amount',
                               color='Amount', hover_data=['Count'],
                               color_continuous_scale='RdBu',
                               )
            st.plotly_chart(fig2)
            st.write(df2)

        elif selected == "Top User":
            df4 = pd.read_csv("top_users.csv")
            df4 = df4.query(f"Year =={year} & Quarter =={quarter}")
            fig4 = px.sunburst(df4, path=['State', 'District'], values='Users',
                               color='Users', hover_data=['Users'],
                               color_continuous_scale='Jet',
                               )
            st.plotly_chart(fig4)
            st.write(df4)

    if select1 == "🗺️State_visual":
        Mapvisual()

    elif select1 == "🗺️District_visual":
        Topvisual()






















