---
description: The at element defines the value of a param element at a particular time, relative to the start of the transition or effect that contains the parameter.
ms.assetid: 523aa25c-790b-4532-9c69-76544235bdfe
title: at Element
ms.topic: reference
ms.date: 05/31/2018
---

# at Element

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `at` element defines the value of a [**param**](param-element.md) element at a particular time, relative to the start of the transition or effect that contains the parameter. The `at` element causes the parameter to jump abruptly to the new value at the given time. For a smooth progression to a new value, use the [**linear**](linear-element.md) element.

## Attributes

[**time**](time-attribute.md), [**value**](value-attribute.md)

## Parent/Child Information



| Label | Value |
|----------|--------------------------------|
| Parent   | [**param**](param-element.md) |
| Children | None                           |



 

## Examples


```XML
<at time="1" value="0.5" />
```



## See also

<dl> <dt>

[XTL Elements](xtl-elements.md)
</dt> </dl>

 

 



