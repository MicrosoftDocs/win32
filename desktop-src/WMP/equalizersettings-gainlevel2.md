---
title: EQUALIZERSETTINGS.gainLevel2
description: The gainLevel2 attribute specifies or retrieves the gain level of band 2.
ms.assetid: e602d9cc-42b3-402e-9df5-8b970d878904
keywords:
- EQUALIZERSETTINGS.gainLevel2 Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.gainLevel2
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# EQUALIZERSETTINGS.gainLevel2

The **gainLevel2** attribute specifies or retrieves the gain level of band 2.

``` syntax
        elementID.gainLevel2
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a value normally ranging from  20 to +20. It has a default value of zero.

## Remarks

This attribute adjusts the portion of the audio frequency spectrum centered on 62Hz.

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

 

 





