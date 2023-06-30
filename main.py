from flask import Flask, request, render_template
from collections import Counter
import jieba

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    token_freqs = []
    if request.method == 'POST':
        text = request.form.get('elements')
        tokens = tokenize_chinese(text)
        token_counter = Counter(tokens)
        token_freqs = sorted(token_counter.items(), key=lambda x: x[1], reverse=True)
    return render_template('index.html', token_freqs=token_freqs)

def tokenize_chinese(text):
    seg_list = jieba.cut(text, cut_all=False)
    return list(seg_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
