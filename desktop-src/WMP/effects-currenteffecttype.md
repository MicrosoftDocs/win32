---
title: EFFECTS.currentEffectType
description: The currentEffectType attribute specifies or retrieves the registry name of the current visualization. This name is a unique ID defined by the visualization author.
ms.assetid: 29469272-468d-49b4-a934-e7dc00583efa
keywords:
- EFFECTS.currentEffectType Windows Media Player
topic_type:
- apiref
api_name:
- EFFECTS.currentEffectType
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# EFFECTS.currentEffectType

The **currentEffectType** attribute specifies or retrieves the registry name of the current visualization. This name is a unique ID defined by the visualization author.

``` syntax
        elementID.currentEffectType
```

## Possible Values

This attribute is a read/write **String**.

## Remarks

You can use this attribute at run time to change the currently displayed effect. To do this, follow these steps:

1.  Use **effectCount** to retrieve the count of registered effects.
2.  In a loop, retrieve the name of each registered effect by using **effectType**.
3.  Specify one of the names you retrieved for **currentEffectType** to set the current effect.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**EFFECTS Element**](effects-element.md)
</dt> <dt>

[**EFFECTS.currentEffect**](effects-currenteffect.md)
</dt> <dt>

[**EFFECTS.effectCount**](effects-effectcount.md)
</dt> <dt>

[**EFFECTS.effectType**](effects-effecttype.md)
</dt> </dl>

 

 





