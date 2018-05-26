---
title: CommandLine element
description: Contains the command line that is passed to the assessment process.
ms.assetid: BF4631F0-6FAC-4B1A-97B8-8F7FDDCBBE14
keywords:
- CommandLine element Access Execution Engine
topic_type:
- apiref
api_name:
- CommandLine
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CommandLine element

Contains the command line that is passed to the assessment process.

## Usage

``` syntax
<CommandLine>
  text
</CommandLine>
```

## Attributes

There are no attributes.

## Text value

This command line is created by the AXE assessment management object model. One line (32K).

## Child elements

There are no child elements.

## Parent elements



| Element                                           | Description                                                                 |
|---------------------------------------------------|-----------------------------------------------------------------------------|
| [**AssessmentRun**](assessmentrun.md)<br/> | Defines the instance of an assessment for execution.<br/> <br/> |



## Remarks

The assessment process is created using the method described in the Assessment s &lt;Execution&gt; node.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Job Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449330)
</dt> </dl>

 

 





