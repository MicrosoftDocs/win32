---
title: EQUALIZERSETTINGS.gainLevel1
description: The gainLevel1 attribute specifies or retrieves the gain level of band 1.
ms.assetid: 3d681ade-3fd4-432d-ae92-c083d927346f
keywords:
- EQUALIZERSETTINGS.gainLevel1 Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.gainLevel1
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# EQUALIZERSETTINGS.gainLevel1

The **gainLevel1** attribute specifies or retrieves the gain level of band 1.

``` syntax
        elementID.gainLevel1
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a value normally ranging from  20 to +20. It has a default value of zero.

## Remarks

This attribute adjusts the portion of the audio frequency spectrum centered on 31Hz.

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

 

 





