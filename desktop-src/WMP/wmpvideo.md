---
title: WMPVIDEO
description: This is a predefined VIDEO element with the following default values.
ms.assetid: c9423aea-2d21-4c5d-8941-dd156dd07eb7
keywords:
- WMPVIDEO Windows Media Player
topic_type:
- apiref
api_name:
- WMPVIDEO
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# WMPVIDEO

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This is a predefined **VIDEO** element with the following default values.

``` syntax
backgroundColor="black"
horizontalAlignment="stretch"
verticalAlignment="stretch"
```

## Remarks

This will create a **VIDEO** element that will stretch the video window when the skin is resized. Digital video displayed in this window will stretch to fit the available space or will be scaled up or down according to the settings on the Player **View** menu under **Video Size**. The **View** menu is displayed in the full mode of the Player or when the **VIEW.titleBar** attribute is set to true in a skin.

All properties of this **VIDEO** element can be overridden by explicitly specifying them.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------|
| Version<br/> | Windows Media Player 7.0 or later<br/> |



## See also

<dl> <dt>

[**VIDEO Element**](video-element.md)
</dt> </dl>

 

 





