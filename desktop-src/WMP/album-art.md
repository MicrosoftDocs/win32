---
title: Album Art
description: Album Art
ms.assetid: a5996232-e1ee-41ae-a6ca-f841321644fe
keywords:
- Windows Media Player Mobile skins,album art
- skins,album art
- reference for skins,album art
- art files for skins,album art
- album art in skins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Album Art

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When you create a skin for Windows Media Player 10 Mobile or later, you may want to display album art that relates to the currently playing media item. When you design your skin, you will want to reserve space in the Background image to contain the album art.

The Album Art section of the skin definition file must begin with the following line:


```C++
[ Album Art ]

```



You then must add information that specifies the location and size of the album art in your skin. You must enter four positive integers, separated by commas that define the left, top, width, and height of the album art, in pixels, relative to the background image. The following example shows how to specify dimensions:


```C++
//  <Location>
//  ----------
   5,37,230,155

```



If you plan on including a video section in your skin, you can use the same size and location for your album art to conserve space.

## Related topics

<dl> <dt>

[**Skin Reference**](skin-reference.md)
</dt> </dl>

 

 




