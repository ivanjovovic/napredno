from flask import Flask, render_template, jsonify, request
import processor


application = Flask(__name__)

application.config['SECRET_KEY'] = 'n067592548'


@application.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())



@application.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():

    if request.method == 'POST':
        the_question = request.form['question']

        response = processor.chatbot_response(the_question)

    return jsonify({"response": response })



if __name__ == '__main__':
    application.run(host='0.0.0.0', port='8888', debug=True)
