---
title: "VLC Dark Mode"
date: "2025-05-12"
description: "Installing Dark Mode for VLC 3.0+"
categories: [
    reference
]
tags: [
    windows, pc, pc setup, vlc, ui, theme, personalisation, dark mode
]
---

> [!NOTE]
> - This is a copy of a `README` that should be in the folder alognside the files mentioned below

# Installing Dark Mode for VLC 3.0+
There are two files accompanying this `README` file, `libqt_plugin.dll` and `libskins2_plugin.dll`. They were both downloaded from a comment on a `Reddit` thread that can be found [here](https://www.reddit.com/r/VLC/comments/1f03nhz/comment/lqlu9ah/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button), the text of the comment will be in the code block below

```text
You DO NOT need to re-install VLC to get dark mode. I'll make it easy for you. Here is what you need to do (assuming you have VLC v3.0+ 64-bit already installed on Windows. At the time of this writing, it works for v3.0.21. This should work for any VLC version that is at least v3):

Download the required dark mode files found at this google drive link (the author has removed these dill files from his github page so i had to re-upload them). The link has two .dll files: libqt_plugin.dll and libskins2_plugin.dll

Close VLC if it's currently running on your pc.

Now, on your local pc, go to your VLC directory (typically its installed at: "C:\Program Files\VideoLan\VLC", but your location may be different) and then navigate into this sub-directory: "plugins\gui" (this directory SHOULD already exist if you're in the correct location).

Place the two dll files mentioned in step 1 inside the sub-directory mentioned in step 3. Take note these dll files ONLY work with the 64-bit version of VLC. If you try using them with the 32-bit version of VLC, the player will not launch and instead will show a terminal (command prompt) window. Not what you want. Install VLC 64-bit if this happens to you.

Now, start your VLC player and go to: "Tools > Preferences > Interface > Look and Feel". You should now see a new option: "Use Dark Mode". Select it and click the "Save" button. Restart VLC to make the dark mode take effect.

Enjoy! ❤️

Alternate Download Mirrors (for vlc.3.0.21-dark.zip -- contains the two dll files):

https://www.mediafire.com/file/qn5ay1qeomvh7rz/vlc.3.0.21-dark.zip/file

https://file.io/W2uHR3iLcF5n

https://bunkr.site/d/dbfvWbhEIlSA9
```

# Miscellaneous
- This was tested in `VLC 3.0.21 Vetinari`