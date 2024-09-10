# app.py
from flask import Flask, request, jsonify, render_template
import torch
import torch.nn as nn
from train_model import IrisModel
import numpy as np
from pathlib import Path
# 初始化Flask應用
app = Flask(__name__)

# 定義模型文件的路徑
current_dir = Path(__file__).parent
model_path = current_dir / 'iris_model.pth'
# 加載訓練好的模型
model = IrisModel()
model.load_state_dict(torch.load(model_path))
model.eval()  # 設置為評估模式
print(model.eval())

# 預處理函數，用於將輸入數據轉換為模型可以接受的格式
def preprocess_input(data):
    data = np.array(data).reshape(1, -1)  # 將輸入數據轉換為1行
    data = torch.tensor(data, dtype=torch.float32)
    return data

# 定義主頁面
@app.route('/')
def index():
    return render_template('index.html')

# 設置API路由，處理POST請求
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        # 獲取輸入值
        sepal_length = float(data['sepal_length'])
        sepal_width = float(data['sepal_width'])
        petal_length = float(data['petal_length'])
        petal_width = float(data['petal_width'])
        
        # 預處理數據
        input_tensor = preprocess_input([sepal_length, sepal_width, petal_length, petal_width])

        # 模型預測
        with torch.no_grad():
            output = model(input_tensor)
            _, predicted = torch.max(output, 1)

        # 將結果轉換為標簽
        iris_classes = ['setosa', 'versicolor', 'virginica']
        prediction = iris_classes[predicted.item()]

        # 返回預測結果
        return jsonify({'prediction': prediction})
    
    except (KeyError, TypeError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400

# 啟動Flask應用
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
