// 獲取容器
const container = document.getElementById('particle-container');

// 生成100個粒子
for (let i = 0; i < 100; i++) {
    const particle = document.createElement('div');
    particle.classList.add('particle');

    // 隨機設置粒子的顏色
    const hue = Math.random() * 360; // 生成隨機色相
    particle.style.backgroundColor = `hsl(${hue}, 80%, 80%)`; // 使用HSL設置顏色

    // 隨機設置粒子的大小，範圍從 40px 到 100px
    const size = Math.random() * 60 + 40; // 生成40到100px之間的大小
    particle.style.width = `${size}px`;
    particle.style.height = `${size}px`;

    // 設置粒子的最終位置（隨機方向發散）
    const angle = Math.random() * 360; // 隨機角度
    const distance = Math.random() * 800 + 300; // 將發散距離範圍調整到300到1100px
    const x = Math.cos(angle * (Math.PI / 180)) * distance; // 計算X方向的位移
    const y = Math.sin(angle * (Math.PI / 180)) * distance; // 計算Y方向的位移

    // 使用CSS自定義屬性設置變換的目標值
    particle.style.setProperty('--x', `${x}px`);
    particle.style.setProperty('--y', `${y}px`);

    // 將粒子添加到容器中
    container.appendChild(particle);
}
