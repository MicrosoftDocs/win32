---
title: Button Location
description: Button Location
ms.assetid: aaab7461-1694-4913-a97b-71dde9592dbe
keywords:
- Windows Media Player Mobile skins,button location
- skins,button location
- reference for skins,buttons
- buttons in skins,location
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Button Location

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You must define the location for each Button image. To do this, you provide four positive integers separated by commas. The numbers define the coordinates of the top-left corner, the width, and height of a button, in pixels.

If you are using region buttons (PushHit, ToggleHit, and 2PushHit), you still must enter these four numbers. The values are used to determine the locations for the secondary images such as Pushed and Disabled.

> [!Note]  
> Button types are deprecated in skins for Windows Media Player 10 Mobile or later.

 

## Related topics

<dl> <dt>

[**Buttons**](buttons.md)
</dt> </dl>

 

 




