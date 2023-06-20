---
title: Trackbar Type
description: Trackbar Type
ms.assetid: b55df7d8-56e3-4daf-8041-10fb0d71e8b1
keywords:
- Windows Media Player Mobile skins,trackbars
- skins,trackbars
- reference for skins,trackbars
- trackbars in skins,types
- thumb,trackbar type
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Trackbar Type

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You must define the type of trackbar you want to use. The following table shows the types that are valid.



| Type   | Description                                                                                                                                                                                                                                                                                                     |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Seek   | Controls the playback position. If the value is zero, the media item is at the beginning. The value increases until the end of the media item is reached. The user can slide the thumb image to change the value, and while the media item plays, the thumb image moves to match the current playback position. |
| Volume | Controls the audio volume. The value varies from 0 to 100. The user can slide the thumb image to change the volume. If the volume changes, the thumb image will move to match the new volume.                                                                                                                   |



 

## Related topics

<dl> <dt>

[**Trackbars**](trackbars.md)
</dt> </dl>

 

 




