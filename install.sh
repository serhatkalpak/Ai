#!/data/data/com.termux/files/usr/bin/bash
echo "📦 Gereksinimler yükleniyor..."
pkg update -y
pkg install python git -y
pip install --upgrade pip
pip install -r requirements.txt
echo 'alias ai-tool="python $HOME/termux-ai-tool/main.py"' >> $HOME/.bashrc
source $HOME/.bashrc
echo "✅ Kurulum tamamlandı! 'ai-tool' yazarak başlatın."