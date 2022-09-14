---
title: EQUALIZERSETTINGS.gainLevel7
description: The gainLevel7 attribute specifies or retrieves the gain level of band 7.
ms.assetid: f39e1475-b0c8-4204-b2d8-943bc8b4f830
keywords:
- EQUALIZERSETTINGS.gainLevel7 Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.gainLevel7
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# EQUALIZERSETTINGS.gainLevel7

The **gainLevel7** attribute specifies or retrieves the gain level of band 7.

``` syntax
        elementID.gainLevel7
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a value normally ranging from  20 to +20. It has a default value of zero.

## Remarks

This attribute adjusts the portion of the audio frequency spectrum centered on 2kHz.

If this attribute is not specified, the previous value will be retained.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**EQUALIZERSETTINGS Element**](equalizersettings-element.md)
</dt> <dt>

[**EQUALIZERSETTINGS. gainLevels**](equalizersettings-gainlevels.md)
</dt> </dl>

 

 





