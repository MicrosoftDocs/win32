---
title: DefaultValue element
description: Contains a default value for the parameter.
ms.assetid: '0C2B145A-3CC8-48CC-AF85-021AD4AA2825'
keywords: ["DefaultValue element Access Execution Engine"]
topic_type:
- apiref
api_name:
- DefaultValue
api_type:
- Schema
---

# DefaultValue element

Contains a default value for the parameter. If blank, the default value is the default value for the parameter's data type.

## Usage

``` syntax
<DefaultValue>
  text
</DefaultValue>
```

## Attributes

There are no attributes.

## Text value

The default value for the parameter. If blank, the default value is the default value for the parameter's data type. AXE uses the CLR rules to determine missing default values. For example, the default value for integral and floating point types is zero, for Boolean values it is false, for strings it is the empty string.  

## Child elements

There are no child elements.

## Parent elements



| Element                                                       | Description                                                                       |
|---------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [**ParameterDefinition**](parameterdefinition.md)<br/> | Information that fully describes an assessment parameter. <br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





