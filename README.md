# Book Recommendation System

![1](https://wallpapercave.com/wp/wp4430530.jpg)

### Objective ✍
Objective is to build an application for all Book Lovers ♥ like me out there where all you have to
do is input book name application will recommend you some books that you may **love😍 to read**.
If you are searching for top popular books then there is a section of top 100 book based on popularity where you can find the right one for you.

### Dataset 🧾
The Dataset that I used for this task is [Book-recommendation dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset). It contains over 10k books with over 1million total ratings. It consists of three files Books.csv, Ratings.csv, Users.csv.

### Features
- **Top 100 Books:** Displays the top 100 books based on popularity.
- **Book Recommendations:** Users can input a book name, and the system will recommend a few books similar to the input book.
- **User-Friendly Interface:** Easy to navigate and use.

### How It Works
- **Data Collection:** The dataset is sourced from Kaggle and includes books, ratings and users.
- **Data Preprocessing:** The data is cleaned and prepared for model training.
- **Model Training:** The collaborative filtering model is trained on the collected data.
- **Recommendations:** When a user inputs a book name, the model suggests books similar to the input book.
- **Popularity Display:** The top 100 books are displayed based on their popularity scores from the dataset.

### Technologies Used
- **Backend:** Flask
- **Frontend:** HTML, CSS
- **Machine Learning:** Collaborative Filtering using Python (Pandas, NumPy, SciKit-Learn)
