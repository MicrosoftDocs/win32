---
title: MinimumConstraint element
description: The minimum value for the parameter.
ms.assetid: '76BB27D9-3584-4897-8869-D1316AAF8B16'
keywords: ["MinimumConstraint element Access Execution Engine"]
topic_type:
- apiref
api_name:
- MinimumConstraint
api_type:
- Schema
---

# MinimumConstraint element

The minimum value for the parameter. This element is valid with any of the numeric data types.

## Usage

``` syntax
<MinimumConstraint>
  text
</MinimumConstraint>
```

## Attributes

There are no attributes.

## Text value

The minimum value for the parameter. If a minimum value is specified that is less than the minimum for the data type, the minimum for the data type will be used.

## Child elements

There are no child elements.

## Parent elements



| Element                                       | Description                                                           |
|-----------------------------------------------|-----------------------------------------------------------------------|
| [**Constraints**](constraints.md)<br/> | Constraints specified for a parameter's value.<br/> <br/> |



## Remarks

If a floating point value is for an integer data type, the value get rounded toward zero and used as the minimum.

This element is valid for these data types.

<dl> **Int**  
**Byte**  
**Sbyte**  
**Int16**  
**Int32**  
**Int64**  
**Uint16**  
**Uint32**  
**Uint64**  
**Single**  
**Double**  
**Char**  
</dl>

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





