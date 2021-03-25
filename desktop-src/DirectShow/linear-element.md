---
description: The linear element defines the value of a param element at a particular time, relative to the start of the transition or effect that contains the param element.
ms.assetid: f6af4bf1-fc2d-439c-b1e3-8e095ecad503
title: linear Element (Camerauicontrol.h)
ms.topic: reference
ms.date: 05/31/2018
---

# linear Element

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The linear element defines the value of a [**param**](param-element.md) element at a particular time, relative to the start of the transition or effect that contains the **param** element. The `linear` element causes the parameter to make a smooth transition from its previous value to the new value. For an instantaneous jump to a new value, use the [**at**](at-element.md) element.

## Attributes

[**time**](time-attribute.md), [**value**](value-attribute.md)

## Parent/Child Information



|          |                                |
|----------|--------------------------------|
| Parent   | [**param**](param-element.md) |
| Children | None                           |



 

## Examples


```XML
<linear time="6" value="0.0" />
```



## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Camerauicontrol.h</dt> </dl> |



## See also

<dl> <dt>

[XTL Elements](xtl-elements.md)
</dt> </dl>

 

 




