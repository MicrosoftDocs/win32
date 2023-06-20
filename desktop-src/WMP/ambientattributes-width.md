---
title: AmbientAttributes.width
description: The width attribute specifies or retrieves the width of the control.
ms.assetid: f246958a-563c-40c0-8a74-4511103b95b2
keywords:
- AmbientAttributes.width Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.width
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AmbientAttributes.width

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **width** attribute specifies or retrieves the width of the control.

``` syntax
        elementID.width
```

## Possible Values

This attribute is a read/write 16-bit **Integer** (0 to 32,767) representing the width of the control in pixels. The default value is zero or the width of the image specified in the control's **image** attribute.

## Remarks

If the width specified is narrower than the width of the image provided, then the image will be clipped. If the width is wider than the width of the image, then the click region will go beyond the image boundary. No matter what value is given to this attribute, the image cannot grow beyond its parent **VIEW** or **SUBVIEW**.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> </dl>

 

 





