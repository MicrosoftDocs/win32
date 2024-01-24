---
title: AmbientAttributes.height
description: The height attribute specifies or retrieves the height of the control.
ms.assetid: a5c85d86-15d4-451d-b8bc-ed3b6e0dfd7d
keywords:
- AmbientAttributes.height Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.height
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AmbientAttributes.height

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **height** attribute specifies or retrieves the height of the control.

``` syntax
        elementID.height
```

## Possible Values

This attribute is a read/write **Number** (**long**) representing the height of the control in pixels. The default value is zero or the height of the image specified in the control's **image** attribute.

## Remarks

If the height specified is smaller than the height of the image provided, then the image will be clipped. If the height is larger than the height of the image, then the click region will go beyond the image boundary. No matter what value is given to this attribute, the image cannot grow beyond its parent **VIEW** or **SUBVIEW**.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> </dl>

 

 





