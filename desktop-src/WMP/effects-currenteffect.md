---
title: EFFECTS.currentEffect
description: The currentEffect attribute specifies or retrieves the current visualization.
ms.assetid: d6b0e77d-2872-420a-b5f5-36fd23243648
keywords:
- EFFECTS.currentEffect Windows Media Player
topic_type:
- apiref
api_name:
- EFFECTS.currentEffect
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# EFFECTS.currentEffect

The **currentEffect** attribute specifies or retrieves the current visualization.

``` syntax
        elementID.currentEffect
```

## Possible Values

This attribute is a read/write **object**. The default value is the first visualization in the authoring order. If there are no visualizations authored in the skin, the default is the first visualization in the registry.

## Remarks

You can use this object to access custom visualizations you have created. For example, you could expose a property through the **IDispatch** interface in your visualization. You can then change the property value from your skin by making your visualization the current effect, and then using the **currentEffect** object to set a new value for the property. For example, if your visualization exposes a property named backgroundColor, the following JScript code specifies a new value:


```JScript
// The EFFECTS element ID is MyEffects.
MyEffects.currentEffect.backgroundColor = "blue";
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**EFFECTS Element**](effects-element.md)
</dt> <dt>

[**EFFECTS.currentEffectTitle**](effects-currenteffecttitle.md)
</dt> <dt>

[**EFFECTS.currentEffectType**](effects-currenteffecttype.md)
</dt> </dl>

 

 





