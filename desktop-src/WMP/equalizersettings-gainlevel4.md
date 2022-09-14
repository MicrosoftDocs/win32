---
title: EQUALIZERSETTINGS.gainLevel4
description: The gainLevel4 attribute specifies or retrieves the gain level of band 4.
ms.assetid: 01383171-f991-4d09-858a-ce21ce93e14e
keywords:
- EQUALIZERSETTINGS.gainLevel4 Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.gainLevel4
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# EQUALIZERSETTINGS.gainLevel4

The **gainLevel4** attribute specifies or retrieves the gain level of band 4.

``` syntax
        elementID.gainLevel4
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a value normally ranging from  20 to +20. It has a default value of zero.

## Remarks

This attribute adjusts the portion of the audio frequency spectrum centered on 250Hz.

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

 

 





