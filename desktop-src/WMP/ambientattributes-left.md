---
title: AmbientAttributes.left
description: The left attribute specifies or retrieves the left coordinate of the control.
ms.assetid: fb1856f2-e286-4ba8-9ae4-b6cd8b0967b1
keywords:
- AmbientAttributes.left Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.left
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AmbientAttributes.left

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **left** attribute specifies or retrieves the left coordinate of the control.

``` syntax
        elementID.left
```

## Possible Values

This attribute is a read/write **Number** (**long**) representing the distance in pixels from the control to the left edge of the parent **VIEW** or **SUBVIEW**. It has a default value of zero. Negative numbers are allowed, in which case the left border of the **VIEW** or **SUBVIEW** clips the control.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> </dl>

 

 





