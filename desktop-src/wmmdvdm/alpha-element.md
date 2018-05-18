---
title: Alpha Element
description: The Alpha element defines the transparency of the specified object.
ms.assetid: '13301252-9daa-43f8-9cd4-fed45dfb6e74'
keywords: ["Alpha Element Windows Movie Maker and DVD Maker"]
topic_type:
- apiref
api_name:
- Alpha Element
api_type:
- NA
---

# Alpha Element

The **Alpha** element defines the transparency of the specified object.

``` syntax
<Alpha;
    value="1.000000"/>
      
```

## Attributes

**value**

Value between 0.000000 (transparent) and 1.000000 (opaque).

## Parent/Child Elements



| Hierarchy | Elements       |
|-----------|----------------|
| Parent    | **Properties** |
| Child     | None           |



 

## Remarks

You may also apply key-frame animation to properties such as Alpha. For example, the following excerpt from the provided custom XML file demonstrates how to linearly interpolate the value of the Alpha property. In this case, the Alpha element takes on several [**Point**](point.md) child elements.

``` syntax
...
  <Alpha type="float" evaluation="Linear">
    <Point time="0.000000" value="1.000000" />
    <Point time="0.966667" value="0.000000" />
    <Point time="1.000000" value="0.000000" />
  </Alpha>
...
```

## See also

<dl> <dt>

[**Elements**](elements.md)
</dt> <dt>

[**Offset Element**](offset.md)
</dt> <dt>

[**Rotate Element**](rotate.md)
</dt> <dt>

[**Scale Element**](scale.md)
</dt> </dl>

 

 




