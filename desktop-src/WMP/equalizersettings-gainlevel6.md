---
title: EQUALIZERSETTINGS.gainLevel6
description: The gainLevel6 attribute specifies or retrieves the gain level of band 6. It has a default value of zero.
ms.assetid: da3e1df5-434b-44db-bcde-8ad9c9874627
keywords:
- EQUALIZERSETTINGS.gainLevel6 Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.gainLevel6
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# EQUALIZERSETTINGS.gainLevel6

The **gainLevel6** attribute specifies or retrieves the gain level of band 6. It has a default value of zero.

``` syntax
        elementID.gainLevel6
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a value normally ranging from  20 to +20. It has a default value of zero.

## Remarks

This attribute adjusts the portion of the audio frequency spectrum centered on 1kHz.

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

 

 





