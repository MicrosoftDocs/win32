---
title: Offset element
description: Defines a three-dimensional (3-D) translation for the specified object.
ms.assetid: 739935b6-aee6-4ac8-af3e-f16efc6f35ab
keywords:
- Offset element Windows Movie Maker and DVD Maker
topic_type:
- apiref
api_name:
- Offset
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Offset element

Defines a three-dimensional (3-D) translation for the specified object.

## Usage

``` syntax
<Offset/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                             |
|-----------------------------------------------------|
| [**Properties**](https://www.bing.com/search?q=**Properties**)<br/> |



## Remarks

You may also apply key-frame animation to properties such as **Offset**. For example, the following excerpt from the provided custom XML file demonstrates how to linearly interpolate the value of the **Offset** property. In this case, the **Offset** element takes on several [Point](point.md) child elements.


```XML
...
  <Offset type="float3" evaluation="Linear" >
    <Point time="0.000000" value="-0.209169, 0.114583, 0.000000" />
    <Point time="0.900000" value="-0.209169, 0.114583, 0.000000" />
    <Point time="1.000000" value="-0.209169, 0.114583, 0.000000" />
  </Offset>
...

```



## Element information



|                                     |               |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



## See also

<dl> <dt>

[**Alpha Element**](alpha-element.md)
</dt> <dt>

[**Elements**](elements.md)
</dt> <dt>

[**Rotate Element**](rotate.md)
</dt> <dt>

[**Scale Element**](scale.md)
</dt> </dl>

 

 





