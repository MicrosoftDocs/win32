---
title: CommandLineFormat element
description: Describes how a parameter is formatted for the assessment command line.
ms.assetid: B55E2AB8-5590-4F14-99AB-E19AD4A4E20F
keywords:
- CommandLineFormat element Access Execution Engine
topic_type:
- apiref
api_name:
- CommandLineFormat
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CommandLineFormat element

Describes how a parameter is formatted for the assessment command line. AXE only includes parameters on an assessments command line if the parameter definition has this **CommandLineFormat** element.

## Usage

``` syntax
<CommandLineFormat>
  text
</CommandLineFormat>
```

## Attributes

There are no attributes.

## Text value

This element must contain a non-empty string that is a valid .NET formatting string.

## Child elements

There are no child elements.

## Parent elements



| Element                                                       | Description                                                                       |
|---------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [**ParameterDefinition**](parameterdefinition.md)<br/> | Information that fully describes an assessment parameter. <br/> <br/> |



## Remarks

This element describes how an assessment parameter is formatted for the assessment command line. This feature is designed to support existing tools that cannot be updated to use the AXE Engine assessment API s to retrieve parameters by name in a type safe manner.

The command line is created by AXE and passed to the root process of the assessment.

## Examples

This node must contain a non-empty string that is a valid .NET formatting string. The assessment parameter value will be the only object passed to the formatter. This means the formatting string must contain one and only one composite formatting item with index zero. Examples are:

``` syntax
-input {0}
/affinity:0x{0,X}
-InputFile=  {0}  
```

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





