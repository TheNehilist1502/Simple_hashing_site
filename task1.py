from flask import Flask, render_template, request
import hashlib
app = Flask(__name__)
@app.route("/")
def home():
    return render_template ('Hashing.html')
@app.route("/Hash", methods=["POST"])
def Hash():
    message= request.form['msg']
    encoded_msg=hashlib.md5(message.encode())
    encoded_hex_msg=encoded_msg.hexdigest()
    text_file = open("Encryption_md5.txt", "a")
    text_file.write('%s, '%encoded_hex_msg)
    text_file.close()
    return render_template('Hashing.html',result=encoded_hex_msg)
if __name__ == "__main__":
    app.run()