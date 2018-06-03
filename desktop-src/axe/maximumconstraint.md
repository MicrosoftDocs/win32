---
title: MaximumConstraint element
description: The maximum value for the parameter.
ms.assetid: 102E5DF4-C5AF-4918-BBF5-557C451F5E24
keywords:
- MaximumConstraint element Access Execution Engine
topic_type:
- apiref
api_name:
- MaximumConstraint
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MaximumConstraint element

The maximum value for the parameter.

## Usage

``` syntax
<MaximumConstraint>
  text
</MaximumConstraint>
```

## Attributes

There are no attributes.

## Text value

The maximum value for the parameter. If a maximum value is specified that is more than the maximum for the data type, the maximum for the data type will be used.

## Child elements

There are no child elements.

## Parent elements



| Element                                       | Description                                                           |
|-----------------------------------------------|-----------------------------------------------------------------------|
| [**Constraints**](constraints.md)<br/> | Constraints specified for a parameter's value.<br/> <br/> |



## Remarks

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

 

 





