---
title: EQUALIZERSETTINGS.gainLevel10
description: The gainLevel10 attribute specifies or retrieves the gain level of band 10.
ms.assetid: 0d645719-86aa-4475-8e87-ea6c20e4fed7
keywords:
- EQUALIZERSETTINGS.gainLevel10 Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.gainLevel10
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# EQUALIZERSETTINGS.gainLevel10

The **gainLevel10** attribute specifies or retrieves the gain level of band 10.

``` syntax
        elementID.gainLevel10
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a value normally ranging from  20 to +20. It has a default value of zero.

## Remarks

This attribute adjusts the portion of the audio frequency spectrum centered on 16kHz.

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

 

 





