# train_model.py
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
from pathlib import Path
# 加載Iris數據集
iris = load_iris()
X = iris['data']
y = iris['target']

# 數據標準化
scaler = StandardScaler()
X = scaler.fit_transform(X)

# 劃分訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 轉換為PyTorch的張量
X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.long)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.long)

# 定義一個簡單的全連接神經網絡
class IrisModel(nn.Module):
    def __init__(self):
        super(IrisModel, self).__init__()
        self.fc1 = nn.Linear(4, 64)
        self.fc2 = nn.Linear(64, 3)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 初始化模型、損失函數和優化器
model = IrisModel()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 訓練模型
def train_model():
    for epoch in range(100):  # 訓練100個epoch
        optimizer.zero_grad()
        output = model(X_train)
        loss = criterion(output, y_train)
        loss.backward()
        optimizer.step()

        if epoch % 10 == 0:
            print(f'Epoch {epoch}, Loss: {loss.item()}')

     # 儲存模型到腳本所在目錄
    save_path = Path(__file__).parent / 'iris_model.pth' # 獲取當前腳本文件所在的目錄，添加iris_model.pth文件名到路徑。
    torch.save(model.state_dict(), save_path)
    print(model.state_dict())# fc2.weight 和 fc2.bias：第二個全連接層的權重和偏置
    print(f"Model saved to {save_path}")

if __name__ == "__main__":
    train_model()
