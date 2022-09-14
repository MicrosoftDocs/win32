---
title: EQUALIZERSETTINGS.gainLevel5
description: The gainLevel5 attribute specifies or retrieves the gain level of band 5.
ms.assetid: 6077a4dc-b9b8-4e00-8b29-14afe5a44321
keywords:
- EQUALIZERSETTINGS.gainLevel5 Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.gainLevel5
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# EQUALIZERSETTINGS.gainLevel5

The **gainLevel5** attribute specifies or retrieves the gain level of band 5.

``` syntax
        elementID.gainLevel5
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a value normally ranging from  20 to +20. It has a default value of zero.

## Remarks

This attribute adjusts the portion of the audio frequency spectrum centered on 500Hz.

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

 

 





