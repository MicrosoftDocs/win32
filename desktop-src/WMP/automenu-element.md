---
title: AUTOMENU Element
description: AUTOMENU Element
ms.assetid: 670c9d85-6362-4068-b283-e4ca17ed43b3
keywords:
- Windows Media Player skins,AUTOMENU element
- skins,AUTOMENU element
- AUTOMENU element
- reference for skins,AUTOMENU element
- elements,AUTOMENU
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AUTOMENU Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **AUTOMENU** element provides a way to display the **Quick Access Panel** in a skin. This is a menu that appears in the full mode of the Player when you click the arrow to the right of the **Now Playing** button. It provides immediate access to digital media files organized in various ways, such as in playlists or by album, artist, or genre. Use the **left** and **top** attributes to specify the location at which the menu should appear when the **show** method is called.

The **AUTOMENU** element supports the following method.



| Method                    | Description                          |
|---------------------------|--------------------------------------|
| [show](automenu-show.md) | Displays the **Quick Access Panel**. |



 

The **AUTOMENU** element supports the following ambient attributes: left and top.

> [!Note]  
> This element requires Windows Media Player 9 Series or later.

 

## Related topics

<dl> <dt>

[**Skin Programming Reference**](skin-programming-reference.md)
</dt> </dl>

 

 




