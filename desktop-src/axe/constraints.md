---
title: Constraints element
description: Constraints specified for a parameter's value.
ms.assetid: 213D83E0-1833-49F6-A40E-8ABD77E9E14D
keywords:
- Constraints element Access Execution Engine
topic_type:
- apiref
api_name:
- Constraints
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Constraints element

Constraints specified for a parameter's value.

## Usage

``` syntax
<Constraints>
  text
  child elements
</Constraints>
```

## Attributes

There are no attributes.

## Text value

Constraints specified for a parameter's value. If this tag is empty or missing, the only constraints are those for the data type of the parameter.

## Child elements



| Element                                                   | Description                                                        |
|-----------------------------------------------------------|--------------------------------------------------------------------|
| [**LengthConstraint**](lengthconstraint.md)<br/>   | The maximum length of the string parameter.<br/> <br/> |
| [**MaximumConstraint**](maximumconstraint.md)<br/> | The maximum value for the parameter.<br/> <br/>        |
| [**MinimumConstraint**](minimumconstraint.md)<br/> | The minimum value for the parameter.<br/> <br/>        |



### Child element sequence

``` syntax
(
  LengthConstraint, 
  MinimumConstraint, 
  MaximumConstraint
)
```

## Parent elements



| Element                                                       | Description                                                                       |
|---------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [**ParameterDefinition**](parameterdefinition.md)<br/> | Information that fully describes an assessment parameter. <br/> <br/> |



## Remarks

These constraints add to those of the data type. For example, a **SByte** must be in the range from -128 to +127. A single precision floating point value must be from -3.4028235E+38 through -1.401298E-45 for negative values and from 1.401298E-45 through 3.4028235E+38 for positive values.

## Examples

Constraints are contained in elements like this:

``` syntax
<Constraints>
    <MinimumConstraint>1</MinimumConstraint>
    <MaximumConstraint>300</MaximumConstraint>
<Constraints>
```

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





