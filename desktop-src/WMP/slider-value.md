---
title: SLIDER.value
description: The value attribute specifies or retrieves the current position of the slider. | SLIDER.value
ms.assetid: '2cd2f8b2-d3f1-4897-98b0-af551d6693e6'
keywords:
- SLIDER.value Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.value
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SLIDER.value

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **value** attribute specifies or retrieves the current position of the slider.

``` syntax
        elementID.value
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a default value of **min**.

## Remarks

The **value** should always be greater than or equal to **min** and less than or equal to **max**. If you specify a value outside this range, **value** and the position of the slider are not changed.

See the **CUSTOMSLIDER**.[positionImage](customslider-positionimage.md) attribute for a sample illustrating how the attributes of the **SLIDER** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**SLIDER Element**](slider-element.md)
</dt> <dt>

[**SLIDER.min**](slider-min.md)
</dt> </dl>

 

 





