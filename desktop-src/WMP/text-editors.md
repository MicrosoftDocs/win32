---
title: Text Editors
description: Text Editors
ms.assetid: 93e32ac4-f387-4e39-9375-5d1aeb9d2c4e
keywords:
- Windows Media Player Mobile skins,text editors
- skins,text editors
- skin definition files,text editors
- text editors in skin definition files
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Text Editors

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You must use a text editor that does not include any formatting characters. A simple text editor such as Notepad is recommended, though development environments such as Microsoft Visual Studio offer advanced features. You should not use an editor such as Microsoft Word, because the default Word file format saves extra formatting codes that will not be useable. If you use a word processor such as Word, you must remember to save your work as unformatted text every time you save your file.

You should probably turn off word wrap if your text editor allows it, and you may want to turn on the ability to view all characters to make sure you do not accidentally add any tabs or other control characters. Remember, including tab characters in your skin definition file will cause the skin to fail.

## Related topics

<dl> <dt>

[**Skin Definition File**](skin-definition-file-mobile.md)
</dt> </dl>

 

 




