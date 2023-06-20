---
title: Sample Bitmap Section
description: Sample Bitmap Section
ms.assetid: 51b84b34-3cbb-4863-b7dc-e33e80d6ba23
keywords:
- Windows Media Player Mobile skins,bitmaps
- skins,bitmaps
- reference for skins,bitmaps
- bitmaps in skins,Bitmaps section
- skin definition files,Bitmaps section
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Sample Bitmap Section

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following lines show a typical Bitmaps section of a skin definition file:


```C++
[ Bitmaps ]

//  <Type>      <File name>     <X,Y>
//  ------      -----------     -----
    Background  Background.bmp  0,0
    Disabled    Disabled.bmp    0,0
    Pushed      Pushed.bmp      0,0
    Region      Region.bmp      0,0
    Super       Super.bmp       0,0
    

```



This defines five bitmaps that are used to create a Background image, images for Disabled and Pushed buttons, a Region image for region buttons, and a Super image for trackbars.

> [!Note]  
> The Region and Super bitmaps are deprecated in skins for Windows Media Player 10 Mobile or later.

 

## Related topics

<dl> <dt>

[**Bitmaps**](bitmaps.md)
</dt> </dl>

 

 




