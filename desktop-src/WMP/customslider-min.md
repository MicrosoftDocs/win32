---
title: CUSTOMSLIDER.min
description: The min attribute specifies or retrieves the minimum value of the range defined by the custom slider.
ms.assetid: a152cf9f-7383-47da-a9b2-dedd13749964
keywords:
- CUSTOMSLIDER.min Windows Media Player
topic_type:
- apiref
api_name:
- CUSTOMSLIDER.min
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CUSTOMSLIDER.min

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **min** attribute specifies or retrieves the minimum value of the range defined by the custom slider.

``` syntax
        elementID.min
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a default value of zero.

## Remarks

The value of **min** must be less than **max**.

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

[**CUSTOMSLIDER.max**](customslider-max.md)
</dt> </dl>

 

 





