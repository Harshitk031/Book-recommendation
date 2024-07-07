from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Loading pickle files
with open(r'pickle_files\book_df.pkl', 'rb') as f:
    book_df = pickle.load(f)

with open(r'pickle_files\book_pt.pkl', 'rb') as f:
    book_pt = pickle.load(f)

with open(r'pickle_files\similarity_score.pkl', 'rb') as f:
    similarity_score = pickle.load(f)

with open(r'pickle_files\top_books.pkl', 'rb') as f:
    top_books = pickle.load(f)
    

book_name = list(top_books['Title'].values)
author=list(top_books['Author'].values)
image=list(top_books['Image_URL'].values)

def recommend_books(book_name):
  book_index = np.where(np.array(list(book_pt.index)) == book_name)
  similar_books = list(enumerate(similarity_score[book_index]))
  similar_books = sorted(similar_books, key=lambda x:x[1], reverse=True)[1:7]

  for i in similar_books:
    # print(book_pt.index[i[0]])
    books = []

    for i in similar_books:
        data = []
        recommended_book = book_df[book_df['Book-Title'] == book_pt.index[i[0]]]
        data.extend(list(recommended_book.drop_duplicates('Book-Title')['Book-Title'].values))
        data.extend(list(recommended_book.drop_duplicates('Book-Title')['Book-Author'].values))
        data.extend(list(recommended_book.drop_duplicates('Book-Title')['Image-URL-M'].values))

        books.append(data)
    return books

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend')
def recommend_ui():
    return render_template('recommendations.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    book_name = request.form.get('user_input')
    book_index = np.where(np.array(list(book_pt.index)) == book_name)
    
    if len(book_index[0]) == 0:
        return render_template('recommendations.html', data=[])
    
    book_index = book_index[0][0]
    similar_books = list(enumerate(similarity_score[book_index]))
    similar_books = sorted(similar_books, key=lambda x:x[1], reverse=True)[1:7]
    
    
    books = []
    for i in similar_books:
        data = []
        recommended_book = book_df[book_df['Book-Title'] == book_pt.index[i[0]]]
        data.extend(list(recommended_book.drop_duplicates('Book-Title')['Book-Title'].values))
        data.extend(list(recommended_book.drop_duplicates('Book-Title')['Book-Author'].values))
        data.extend(list(recommended_book.drop_duplicates('Book-Title')['Image-URL-M'].values))

        books.append(data)

    return render_template('recommendations.html', data=books)

@app.route('/popular')
def popular():
    # Your existing code for popular books
    return render_template('popular_books.html', book_name=book_name, author=author, image=image)

if __name__ == '__main__':
    app.run(debug=True)