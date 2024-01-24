---
title: VIDEO.stretchToFit
description: The stretchToFit attribute specifies a value indicating whether the video will stretch to the width and height defined for the Video control.
ms.assetid: 257f5f01-a447-4637-aa73-e5800b263ba5
keywords:
- VIDEO.stretchToFit Windows Media Player
topic_type:
- apiref
api_name:
- VIDEO.stretchToFit
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VIDEO.stretchToFit

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **stretchToFit** attribute specifies a value indicating whether the video will stretch to the width and height defined for the Video control.

``` syntax
        elementID.stretchToFit
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                                             |
|-------|---------------------------------------------------------|
| true  | The video will stretch to fit the control.              |
| false | Default. The video will not stretch to fit the control. |



 

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

 

 





