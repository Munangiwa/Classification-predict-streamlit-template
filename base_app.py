"""
    Simple Streamlit webserver application for serving developed classification
	models.
    Author: Explore Data Science Academy.
    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.
    ---------------------------------------------------------------------
    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend the functionality of this script
	as part of your predict project.
	For further help with the Streamlit framework, see:
	https://docs.streamlit.io/en/latest/
"""
# Streamlit dependencies
import streamlit as st
import joblib,os

# Data dependencies
import pandas as pd

# Vectorizer
# Creating Lemmatizer Function
news_vectorizer = open("resources/vect.pkl","rb")
tweet_cv = joblib.load(news_vectorizer) # loading your vectorizer from the pkl file

# Load your raw data
raw = pd.read_csv("resources/train.csv")

# The main function where we will build the actual app
def main():
	"""Tweet Classifier App with Streamlit """

	# Creates a main title and subheader on your page -
	# these are static across all pages
	st.title("Climate Change Belief Classification")
	st.subheader("Climate change tweet classification")

	# Creating sidebar with selection box -
	# you can create multiple pages this way
	options = ["Home","Information","Exploratory Data Analysis", "Prediction" ]
	selection = st.sidebar.selectbox("Menu", options)



	# Building out the "Home" page
	if selection == "Home":
		st.subheader("Home")
		st.markdown("This is a simple app that will predict wether or not people believe in climate change. It will help Geo- Enviromental companies who are turning to social media to obtain valuable information about job applicants and to monitor their employees activities in relation to their values and beliefs on climate change")
		st.image("resources/climate-word-map.jpg")


	# Building out the "Information" page
	if selection == "Information":
		st.info("General Information")
		# You can read a markdown file from supporting resources folder
		st.markdown("Climate change is a periodic modification of Earth’s climate brought about as a result of changes in the atmosphere as well as interactions between the atmosphere and various other geologic, chemical, biological, and geographic factors within the Earth system.")
		st.image("resources/climate change.jpg")
		st.markdown("Many companies are built around lessening one’s environmental impact or carbon footprint. They offer products and services that are environmentally friendly and sustainable, in line with their values and ideals. They would like to determine how people perceive climate change and whether or not they believe it is a real threat. This would add to their market research efforts in gauging how their product/service may be received.")

		st.markdown("We were challenged  during the Classification Sprint with the task of creating a Machine Learning model that is able to classify whether or not a person believes in climate change, based on their novel tweet data.")
		st.subheader("Raw Twitter data and label")
		if st.checkbox('Show raw data'): # data is hidden if box is unchecked
			st.write(raw[['sentiment', 'message']]) # will write the df to the page

	#Building out the "Exploratory Data Ananlysis" page
	
	if selection == "Exploratory Data Analysis":
		st.subheader("Exploratory Data Analysis")
	
		#To improve speed and cache data
		@st.cache(persist=True)
		def get_data(raw):
			df = pd.read_csv("resources/train.csv")
			return df

		if st.checkbox("Preview DataFrame"):
			data = get_data(raw)
		if st.button("Head"):
			st.write(data.head())
		if st.button("Tail"):
			st.write(data.tail())

		#Show Entire Data frame
		if st.checkbox("Show All Dataframe"):
			data = get_data(raw)
			st.dataframe(data)

		#Show Description
		if st.checkbox("Show All Column Names"):
			data = get_data(raw)
			st.text("Columns:")
			st.write(data.columns)

		#Show summary
		if st.checkbox("Show Summary of Dataset"):
			data = get_data(raw)
			st.write(data.describe())

		#Show plots
		if st.checkbox("Show Most Popular Tags"):
			st.image("resources/Most_Popular_Tags.png")
		if st.checkbox("Show Neutral Tags"):
			st.image("resources/Neutral_Tags.png")
		if st.checkbox("Show Negative Tags"):
			st.image("resources/Negative_Tags.png")
		if st.checkbox("Show News Tags"):
			st.image("resources/News_Tags.png")
		if st.checkbox("Show Number Of Messages Per Sentiment"):
			st.image("resources/Number_of_Messages_Per_Sentiment.png")
		if st.checkbox("Show Numerial Distribution"):
			st.image("resources/Numerical Distribution.png")
		if st.checkbox("Show Positive Tags"):
			st.image("resources/Positive_Tags.png")
		
		#Show Wordcloud
		if st.checkbox("Show Negative Word cloud"):
			st.image("resources/Negative_Cloud.png")
		if st.checkbox("Show Neutral Word Cloud"):
			st.image("resources/Neutral_Cloud.png")
		if st.checkbox("Show News Word Cloud"):
			st.image("resources/News_Cloud.png")
		if st.checkbox("Show Positive Word Cloud"):
			st.image("resources/Positive_Cloud.png")
			       
	
	# Building out the predication page
	if selection == "Prediction":
		st.info("Prediction with ML Models")
		# Creating a text box for user input
		tweet_text = st.text_area("Enter Text","Type Here")

		if st.button("Classify with Logistic Regression Model"):
			# Transforming user input with vectorizer
			vect_text = tweet_cv.transform([tweet_text]).toarray()
			# Load your .pkl file with the model of your choice + make predictions
			# Try loading in multiple models to give the user a choice
			predictor = joblib.load(open(os.path.join("resources/log.pkl"),"rb"))
			prediction = predictor.predict(vect_text)

			# When model has successfully run, will print prediction
			# You can use a dictionary or similar structure to make this output
			# more human interpretable.
			st.success("Text Categorized as: {}".format(prediction))
			
		if st.button("Classify with Decision Tree Model"):
			# Transforming user input with vectorizer
			vect_text = tweet_cv.transform([tweet_text]).toarray()
			# Load your .pkl file with the model of your choice + make predictions
			# Try loading in multiple models to give the user a choice
			predictor = joblib.load(open(os.path.join("resources/dt.pkl"),"rb"))
			prediction = predictor.predict(vect_text)

			# When model has successfully run, will print prediction
			# You can use a dictionary or similar structure to make this output
			# more human interpretable.
			st.success("Text Categorized as: {}".format(prediction))
			
		if st.button("Classify with K-Nearest Neighbors Model"):
			# Transforming user input with vectorizer
			vect_text = tweet_cv.transform([tweet_text]).toarray()
			# Load your .pkl file with the model of your choice + make predictions
			# Try loading in multiple models to give the user a choice
			predictor = joblib.load(open(os.path.join("resources/rf.pkl"),"rb"))
			prediction = predictor.predict(vect_text)

			# When model has successfully run, will print prediction
			# You can use a dictionary or similar structure to make this output
			# more human interpretable.
			st.success("Text Categorized as: {}".format(prediction))


# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
	main()
