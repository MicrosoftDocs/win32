---
title: AmbientAttributes.top
description: The top attribute specifies or retrieves the top coordinate of the control.
ms.assetid: 869abbc4-7e78-4e6b-980e-9b967c61fe19
keywords:
- AmbientAttributes.top Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.top
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AmbientAttributes.top

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **top** attribute specifies or retrieves the top coordinate of the control.

``` syntax
        elementID.top
```

## Possible Values

This attribute is a read/write **Number** (**long**) representing the distance in pixels from the control to the top edge of the parent **VIEW** or **SUBVIEW**. It has a default value of zero. Negative numbers are allowed, in which case the top border of the **VIEW** or **SUBVIEW** clips the control.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> <dt>

[**AmbientAttributes.id**](ambientattributes-id.md)
</dt> </dl>

 

 





