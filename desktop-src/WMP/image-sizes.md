---
title: Image Sizes
description: Image Sizes
ms.assetid: f639ac34-f173-4b84-95ac-360d7fc40d1b
keywords:
- Windows Media Player Mobile skins,art files
- skins,art files
- files for skins,art
- art files for skins,image sizes
- Windows Media Player Mobile skins,image sizes
- skins,image sizes
- image sizes in skins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Image Sizes

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You must take the display area size into consideration when creating artwork for skins. The following table shows the display area sizes for different screen configurations.



| DPI (mode)                    | Width in pixels | Height in pixels |
|-------------------------------|-----------------|------------------|
| 96 (portrait)                 | 240             | 320              |
| 96 (landscape)                | 320             | 240              |
| 192 (portrait)                | 480             | 640              |
| 192 (landscape)               | 640             | 220              |
| 96 (square)                   | 240             | 240              |
| 192 (square)                  | 480             | 480              |
| 96 (portrait for Smartphone)  | 176             | 220              |
| 131 (portrait for Smartphone) | 240             | 320              |



 

> [!Note]  
> Versions earlier than Windows Media Player 9 Series for Windows Mobile 2003 support only 96 DPI portrait-mode skins. Windows Media Player 10 Mobile or later supports 131 DPI portrait-mode skins on Smartphone devices, and this support is expected to continue in future versions of Windows Media Player Mobile.

 

## Related topics

<dl> <dt>

[**Art Files**](art-files-mobile.md)
</dt> </dl>

 

 




