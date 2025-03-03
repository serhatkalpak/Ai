#!/data/data/com.termux/files/usr/bin/bash
pkg update -y
pkg install python git -y
pip install --upgrade pip
pip install -r requirements.txt
echo 'alias ai-tool="python ~/termux-ai-tool/main.py"' >> ~/.bashrc
source ~/.bashrc
echo "✅ Kurulum tamamlandı! 'ai-tool' yazarak başlatın."