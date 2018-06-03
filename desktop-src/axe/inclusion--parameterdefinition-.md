---
title: Inclusion (ParameterDefinition) element
description: Sets the condition for including a ParameterValue defined by the ParameterDefinition in an assessment run.
ms.assetid: FA06B9FC-D8A9-46CF-A9A8-55F4D7DC86D6
keywords:
- Inclusion (ParameterDefinition) element Access Execution Engine
topic_type:
- apiref
api_name:
- Inclusion (ParameterDefinition)
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Inclusion (ParameterDefinition) element

Sets the condition for including a [**ParameterValue**](parametervalue.md) defined by the [**ParameterDefinition**](parameterdefinition.md) in an assessment run.

## Usage

``` syntax
<Inclusion (ParameterDefinition)>
  child elements
</Inclusion (ParameterDefinition)>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                 | Description                                                                                                                                                                                                                                                                                           |
|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Optional**](optional.md)<br/>                 | The parameter will only be included if the user or script specifies a parameter value.<br/> <br/>                                                                                                                                                                                         |
| [**OptionalIncluded**](optionalincluded.md)<br/> | The parameter is automatically included in an assessment run when the assessment run is added to a job. The automatically created [**ParameterValue**](parametervalue.md) is then treated as optional and can be removed by the user, script or program that creates the job.<br/> <br/> |
| [**Required**](required.md)<br/>                 | This parameter is included as a named parameter. It cannot be removed from the assessment run.<br/> <br/>                                                                                                                                                                                 |



### Child element sequence

``` syntax
OptionalOptionalIncludedRequired
```

## Parent elements



| Element                                                       | Description                                                                |
|---------------------------------------------------------------|----------------------------------------------------------------------------|
| [**ParameterDefinition**](parameterdefinition.md)<br/> | Information that describes an assessment parameter.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





