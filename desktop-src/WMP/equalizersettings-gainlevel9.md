---
title: EQUALIZERSETTINGS.gainLevel9
description: The gainLevel9 attribute specifies or retrieves the gain level of band 9.
ms.assetid: 2bed7486-4d4c-4c71-8bab-8dd0c4f56911
keywords:
- EQUALIZERSETTINGS.gainLevel9 Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.gainLevel9
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# EQUALIZERSETTINGS.gainLevel9

The **gainLevel9** attribute specifies or retrieves the gain level of band 9.

``` syntax
        elementID.gainLevel9
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a value normally ranging from  20 to +20. It has a default value of zero.

## Remarks

This attribute adjusts the portion of the audio frequency spectrum centered on 8kHz.

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

 

 





