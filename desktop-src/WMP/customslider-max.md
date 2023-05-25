---
title: CUSTOMSLIDER.max
description: The max attribute specifies or retrieves the maximum value of the range defined by the custom slider.
ms.assetid: 2b788b13-d9a8-4cf6-9397-a2fc8d5d19e1
keywords:
- CUSTOMSLIDER.max Windows Media Player
topic_type:
- apiref
api_name:
- CUSTOMSLIDER.max
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CUSTOMSLIDER.max

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **max** attribute specifies or retrieves the maximum value of the range defined by the custom slider.

``` syntax
        elementID.max
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a default value of 100.

## Remarks

The value of **max** must be greater than that of **min**.

## Examples

See the [positionImage](customslider-positionimage.md) attribute for a sample illustrating how the attributes of the **CUSTOMSLIDER** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**CUSTOMSLIDER Element**](customslider-element.md)
</dt> <dt>

[**CUSTOMSLIDER.min**](customslider-min.md)
</dt> </dl>

 

 





