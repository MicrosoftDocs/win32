---
title: Rotate element
description: Defines a three-dimensional (3-D) rotation for a specified object.
ms.assetid: 'f6b543c0-e150-486e-9b1d-5a6a4783ee9b'
keywords: ["Rotate element Windows Movie Maker and DVD Maker"]
topic_type:
- apiref
api_name:
- Rotate
api_type:
- Schema
---

# Rotate element

Defines a three-dimensional (3-D) rotation for a specified object.

## Usage

``` syntax
<Rotate/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                             |
|-----------------------------------------------------|
| [**Properties**](PropertiesElement_MFGV)<br/> |



## Remarks

You may also apply key-frame animation to properties such as **Rotate**. For example, the following excerpt from the provided custom XML file demonstrates how to linearly interpolate the value of the **Rotate** property. In this case, the **Rotate** element takes on several [Point](point.md) child elements.


```XML
...
  <Rotate type="float3" evaluation="Linear" >
    <Point time="0.000000" value="-0.174533, 0.000000, 0.000000" />
    <Point time="0.900000" value="0.000000, 0.000000, 0.000000" />
    <Point time="1.000000" value="0.000000, 0.000000, 0.000000" />
  </Rotate>
...

```



## Element information



|                                     |               |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



## See also

<dl> <dt>

[**Alpha Element**](alpha-element.md)
</dt> <dt>

[**Elements**](elements.md)
</dt> <dt>

[**Offset Element**](offset.md)
</dt> <dt>

[**Scale Element**](scale.md)
</dt> </dl>

 

 





