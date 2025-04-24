#!/bin/bash

echo "🔨 Building the workspace..."
colcon build --symlink-install

if [ $? -eq 0 ]; then
    echo "✅ Build successful."
    # 'source install/setup.bash' komutunu panoya kopyala
    echo "source install/setup.bash" | xclip -selection clipboard
    echo "ℹ️ Now the source command has been copied to your clipboard."

else
    echo "❌ Build failed."
fi
