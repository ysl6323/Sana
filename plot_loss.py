import re
import matplotlib.pyplot as plt

log_file = '/data/shanglinyuan/pretrained_weights/best_version_wd0.02_lr2e-5/debug/train_log.log'
steps = []
losses = []

# 正则表达式提取Global Step和loss
pattern = re.compile(r'Global Step: (\d+).*?loss:([0-9\.]+)')

with open(log_file, 'r', encoding='utf-8') as f:
    for line in f:
        match = pattern.search(line)
        if match:
            if int(match.group(1)) < 40000:
                steps.append(int(match.group(1)))
                losses.append(float(match.group(2)))

plt.figure(figsize=(10,6))
plt.plot(steps, losses, label='Training Loss')
plt.xlabel('Global Step')
plt.ylabel('Loss')
plt.title('Training Loss Curve')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("/data/shanglinyuan/pretrained_weights/best_version_wd0.02_lr2e-5/debug/loss_curve.png", dpi=300)
plt.show()
