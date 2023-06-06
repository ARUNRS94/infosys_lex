from flask import Flask, render_template, request, jsonify
import pyperclip
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def post_data():
    data = request.get_json()
    clipboard_data = data['data']
    soup = BeautifulSoup(clipboard_data, 'html.parser')

    # Find all elements with class="options word-break figure-image" and id="problemStatement"
    options = soup.find_all('div', {'class': 'options word-break figure-image'})
    options_text = [o.text for o in options]
    problem_statement = soup.find('div', {'id': 'problemStatement'})
    text = problem_statement.get_text()

    response = text
    response += "\n" + "Choose the best one with out explanation"
    #print(response)
    for count, i in enumerate(options_text):
        #print(count, i)
        #print(options_text)
        option_no = count + 1
        response += "\n" + str(option_no) + "." + i
        print(response)

    # Copy response to clipboard
    pyperclip.copy(response)

    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)
