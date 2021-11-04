---
description: The group element defines a group, the top-level object in a timeline.
ms.assetid: db2f1fdd-bcb1-4401-91f4-5e167e4da215
title: group Element (DirectShow)
ms.topic: reference
ms.date: 05/31/2018
---

# group Element

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The **group** element defines a group, the top-level object in a timeline.

## Attributes

[**bitdepth**](bitdepth-attribute.md), [**buffering**](buffering-attribute.md), [**framerate**](framerate-attribute.md), [**height**](height-attribute.md), [**lock**](lock-attribute.md), [**mute**](mute-attribute.md), [**name**](name-attribute.md), [**previewmode**](previewmode-attribute.md), [**samplingrate**](samplingrate-attribute.md), [**type**](type-attribute.md), [**userdata**](userdata-attribute.md), [**userid**](userid-attribute.md), [**username**](username-attribute.md), [**width**](width-attribute.md)

## Parent/Child Information



| Label | Value |
|----------|----------------------------------------------------------------------------------------------------------|
| Parent   | [**timeline**](timeline-element.md)                                                                     |
| Children | [**composite**](composite-element.md), [**effect**](effect-element.md), [**track**](track-element.md) |



 

## Remarks

Within a `group` element, the priority of nested layers is determined implicitly by the order they appear within the element. The first layer has priority 0, and subsequent layers have increasing priority values.

## Examples


```XML
<group type="video" width="640" height="480" framerate="30"> </group>
```



## See also

<dl> <dt>

[XTL Elements](xtl-elements.md)
</dt> </dl>

 

 



