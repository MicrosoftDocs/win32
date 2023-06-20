---
title: PLAYERAPPLICATION Element
description: PLAYERAPPLICATION Element
ms.assetid: 3b58da91-68a9-4f30-a712-3806c781cbbf
keywords:
- Windows Media Player skins,PLAYERAPPLICATION element
- skins,PLAYERAPPLICATION element
- PLAYERAPPLICATION element
- reference for skins,PLAYERAPPLICATION element
- elements,PLAYERAPPLICATION
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PLAYERAPPLICATION Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **PLAYERAPPLICATION** element can be used by certain skins to access the **PlayerApplication** object. This element provides similar functionality to the **playerApplication** global attribute. This element is only used by skins that are displayed by C++ applications that embed a remoted instance of Windows Media Player control.

The **PLAYERAPPLICATION** element supports the following attributes.



| Attribute                                              | Description                                                                                              |
|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [hasDisplay](playerapplication-hasdisplay-scr.md)     | Retrieves a value indicating whether video can display through the remoted Windows Media Player control. |
| [playerDocked](playerapplication-playerdocked-scr.md) | Retrieves a value indicating whether Windows Media Player is in a docked state.                          |



 

## Related topics

<dl> <dt>

[**Using Skins with the Windows Media Player Control**](using-skins-with-the-windows-media-player-control.md)
</dt> </dl>

 

 




