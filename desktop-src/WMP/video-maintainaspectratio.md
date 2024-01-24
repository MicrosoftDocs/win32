---
title: VIDEO.maintainAspectRatio
description: The maintainAspectRatio attribute specifies or retrieves a value indicating whether the video will maintain its aspect ratio when trying to fit within the width and height defined for the control.
ms.assetid: 42ac2196-b747-48d5-868d-7f7e5eb8dabb
keywords:
- VIDEO.maintainAspectRatio Windows Media Player
topic_type:
- apiref
api_name:
- VIDEO.maintainAspectRatio
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VIDEO.maintainAspectRatio

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **maintainAspectRatio** attribute specifies or retrieves a value indicating whether the video will maintain its aspect ratio when trying to fit within the width and height defined for the control.

``` syntax
        elementID.maintainAspectRatio
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                                              |
|-------|----------------------------------------------------------|
| true  | Default. Video maintains its aspect ratio when resizing. |
| false | Video does not maintain its aspect ratio when resizing.  |



 

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**VIDEO Element**](video-element.md)
</dt> </dl>

 

 





