---
title: AmbientAttributes.right
description: The right attribute specifies or retrieves the right coordinate of the control.
ms.assetid: 32f6c9ff-9b2f-4e24-abbb-548a0601d3d7
keywords:
- AmbientAttributes.right Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.right
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AmbientAttributes.right

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **right** attribute specifies or retrieves the right coordinate of the control.

``` syntax
        elementID.right
```

## Possible Values

This attribute is a read/write **Number** (**long**) representing the distance in pixels from the control to the right edge of the parent **VIEW** or **SUBVIEW**. The behavior for negative values, or when [AmbientAttributes.width](ambientattributes-width.md) is not specified, is undefined.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------|
| Version<br/> | Windows Media Player 11<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> <dt>

[**AmbientAttributes.id**](ambientattributes-id.md)
</dt> </dl>

 

 





