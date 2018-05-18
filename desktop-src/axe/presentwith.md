---
title: PresentWith element
description: Describes other parameters that must be present for this parameter to be valid.
ms.assetid: '0F64CBDB-0802-4323-96FD-4E58E94D3DF3'
keywords: ["PresentWith element Access Execution Engine"]
topic_type:
- apiref
api_name:
- PresentWith
api_type:
- Schema
---

# PresentWith element

Describes other parameters that must be present for this parameter to be valid.

## Usage

``` syntax
<PresentWith>
  child elements
</PresentWith>
```

## Attributes

There are no attributes.

## Child elements



| Element                                         | Description                                                                                               |
|-------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [**ParameterIds**](parameterids.md)<br/> | This element must contain one or more [**ParameterId**](parameterid.md) elements.<br/> <br/> |



### Child element sequence

``` syntax
ParameterIds
```

## Parent elements



| Element                                                       | Description                                                                       |
|---------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [**ParameterDefinition**](parameterdefinition.md)<br/> | Information that fully describes an assessment parameter. <br/> <br/> |



## Remarks

Each [**ParameterId**](parameterid.md) element contains the programmatic name of a parameter and a value for that parameter.

The parent parameter is treated as present only if the parameter (or parameters) listed in the [**ParametersIds**](https://msdn.microsoft.com/library/windows/desktop/hh449479) element are present in an [**AssessmentRun**](assessmentrun.md) element.

## Examples

``` syntax
<ParametersIds>
    <ParameterId>
        <ProgrammaticName><ProgrammaticName>
    </ParameterId>
</ParametersIds> 
```

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





