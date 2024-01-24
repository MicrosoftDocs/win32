---
title: SLIDER.max
description: The max attribute specifies or retrieves the maximum value of the range defined by the slider control.
ms.assetid: 'c38e7868-d144-4e40-871a-e70181a6dfb5'
keywords:
- SLIDER.max Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.max
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SLIDER.max

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **max** attribute specifies or retrieves the maximum value of the range defined by the slider control.

``` syntax
        elementID.max
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a default value of 100.

## Remarks

The value specified for **max** must be greater than the one for **min**.

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
</dt> <dt>

[**SLIDER.value**](slider-value.md)
</dt> </dl>

 

 





