---
title: VIDEO.shrinkToFit
description: The shrinkToFit attribute specifies or retrieves a value indicating whether the video will shrink to the width and height defined for the Video control.
ms.assetid: 94ab33b0-b08c-4063-a3e6-1315bb527e1c
keywords:
- VIDEO.shrinkToFit Windows Media Player
topic_type:
- apiref
api_name:
- VIDEO.shrinkToFit
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VIDEO.shrinkToFit

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **shrinkToFit** attribute specifies or retrieves a value indicating whether the video will shrink to the width and height defined for the Video control.

``` syntax
        elementID.shrinkToFit
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                                        |
|-------|----------------------------------------------------|
| true  | Default. The video will shrink to fit the control. |
| false | The video will not shrink to fit the control.      |



 

## Remarks

If no width or height is specified, this attribute is ignored.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**VIDEO Element**](video-element.md)
</dt> </dl>

 

 





