---
description: The transition element defines a transition object. A transition is a two-input transform that results in a transition from one stream (such as a composite or track) to another.
ms.assetid: d344a29f-5b6d-44a3-b1d7-759442e229f5
title: transition Element
ms.topic: reference
ms.date: 05/31/2018
---

# transition Element

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `transition` element defines a transition object. A transition is a two-input transform that results in a transition from one stream (such as a composite or track) to another.

## Attributes

[**clsid**](clsid-attribute.md), [**cutpoint**](cutpoint-attribute.md), [**cutsonly**](cutsonly-attribute.md), [**lock**](lock-attribute.md), [**mute**](mute-attribute.md), [**start**](start-attribute.md), [**stop**](stop-attribute.md), [**swapinputs**](swapinputs-attribute.md), [**userdata**](userdata-attribute.md), [**userid**](userid-attribute.md), [**username**](username-attribute.md)

## Parent/Child Information



| Label | Value |
|----------|------------------------------------------------------------------------|
| Parent   | [**composite**](composite-element.md), [**track**](track-element.md) |
| Children | [**param**](param-element.md)                                         |



 

## Remarks

The **clsid** attribute specifies the subobject that creates the transition.

## Examples


```XML
<transition
    clsid="{2a54c913-07aa-11d2-8d6d-00c04f8ef8e0}"
    start="7"
    stop="10"
/>
```



## See also

<dl> <dt>

[XTL Elements](xtl-elements.md)
</dt> </dl>

 

 



