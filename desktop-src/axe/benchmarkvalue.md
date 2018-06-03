---
title: BenchmarkValue element
description: Contains a benchmark value.
ms.assetid: 355C7B39-7786-40FB-A931-6A39AE54E5E9
keywords:
- BenchmarkValue element Access Execution Engine
topic_type:
- apiref
api_name:
- BenchmarkValue
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BenchmarkValue element

Contains a benchmark value.

## Usage

``` syntax
<BenchmarkValue>
  text
</BenchmarkValue>
```

## Attributes

There are no attributes.

## Text value

The parameter s benchmark value. If the user runs the assessment is to be run in benchmark mode, AXE will only populate the jobs s corresponding parameter value with this value.

## Child elements

There are no child elements.

## Parent elements



| Element                                                       | Description                                                                       |
|---------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [**ParameterDefinition**](parameterdefinition.md)<br/> | Information that fully describes an assessment parameter. <br/> <br/> |



## Remarks

If a parameter has a benchmark value and the assessment is specified to run in benchmark mode in the job then the parameter must be present and use this value. An optional parameter with a benchmark value becomes mandatory when an assessment is run in benchmark mode.

Reporting tools can use this data to verify that the assessment was run in benchmark mode.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





