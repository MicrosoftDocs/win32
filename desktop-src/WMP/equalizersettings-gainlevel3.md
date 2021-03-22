---
title: EQUALIZERSETTINGS.gainLevel3
description: The gainLevel3 attribute specifies or retrieves the gain level of band 3.
ms.assetid: 508d00c6-2429-4f35-b7ab-bf30f774e614
keywords:
- EQUALIZERSETTINGS.gainLevel3 Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.gainLevel3
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# EQUALIZERSETTINGS.gainLevel3

The **gainLevel3** attribute specifies or retrieves the gain level of band 3.

``` syntax
        elementID.gainLevel3
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a value normally ranging from  20 to +20. It has a default value of zero.

## Remarks

This attribute adjusts the portion of the audio frequency spectrum centered on 125Hz.

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

 

 





