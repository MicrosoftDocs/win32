---
title: CUSTOMSLIDER.value
description: The value attribute specifies or retrieves the current position of the slider. | CUSTOMSLIDER.value
ms.assetid: 29e17f48-1848-458d-9da4-316013b21980
keywords:
- CUSTOMSLIDER.value Windows Media Player
topic_type:
- apiref
api_name:
- CUSTOMSLIDER.value
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CUSTOMSLIDER.value

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **value** attribute specifies or retrieves the current position of the slider.

``` syntax
        elementID.value
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a default value equal to the **min** attribute.

## Remarks

The **value** must be greater than or equal to **min** and less than or equal to **max**. If the value falls outside the range, a warning is issued, and the value does not change.

## Examples

See the [positionImage](customslider-positionimage.md) attribute for a sample illustrating how the attributes of the **CUSTOMSLIDER** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**CUSTOMSLIDER Element**](customslider-element.md)
</dt> </dl>

 

 





