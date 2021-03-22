---
title: EQUALIZERSETTINGS.gainLevels
description: The gainLevels attribute specifies or retrieves the gain level of the band corresponding to the index provided.
ms.assetid: fb70e2ef-4cee-457e-a06b-7a1ae6930986
keywords:
- EQUALIZERSETTINGS.gainLevels Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.gainLevels
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# EQUALIZERSETTINGS.gainLevels

The **gainLevels** attribute specifies or retrieves the gain level of the band corresponding to the index provided.

``` syntax
        elementID.gainLevels(theBand)
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a value normally ranging from  20 to +20.

## Parameters

<dl> <dt>

<span id="theBand"></span><span id="theband"></span><span id="THEBAND"></span>*theBand*
</dt> <dd>

**Number**(**long**) between 1 and 10 indicating the index of the band.

</dd> </dl>

## Remarks

This attribute takes a parameter, but its value is specified in script code the same way as other attribute values. It cannot be specified in the EQUALIZERSETTINGS element, nor can it be used with the **wmpprop** listening attribute. Instead, the numbered gain level attributes are provided for these situations.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**EQUALIZERSETTINGS Element**](equalizersettings-element.md)
</dt> <dt>

[**Listening Attributes**](listening-attributes.md)
</dt> </dl>

 

 





