---
description: The composite element defines a composition, a container object for tracks and other nested compositions.
ms.assetid: 7551da3a-1da6-426a-ba9d-f715df53718f
title: composite Element
ms.topic: reference
ms.date: 05/31/2018
---

# composite Element

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `composite` element defines a composition, a container object for tracks and other nested compositions.

## Attributes

[**lock**](lock-attribute.md), [**mute**](mute-attribute.md), [**userdata**](userdata-attribute.md), [**userid**](userid-attribute.md), [**username**](username-attribute.md)

## Parent/Child Information



| Label | Value |
|----------|-------------------------------------------------------------------------------------------------------------------------|
| Parent   | `composite`, [**group**](group-element.md)                                                                             |
| Children | `composite`, [**effect**](effect-element.md), [**track**](track-element.md), [**transition**](transition-element.md) |



 

## Remarks

Within a `composite` element, the priority of nested layers is determined implicitly by the order in which they appear within the element. The first layer has priority 0, and subsequent layers have increasing priority values.

## Examples


```XML
<composite> </composite>
```



## See also

<dl> <dt>

[XTL Elements](xtl-elements.md)
</dt> </dl>

 

 



