---
title: MetricThresholds element
description: Contains one or more metric thresholds.
ms.assetid: 48242467-76C2-49DF-BE5B-C3E6E1DB3FD3
keywords:
- MetricThresholds element Access Execution Engine
topic_type:
- apiref
api_name:
- MetricThresholds
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MetricThresholds element

Contains one or more metric thresholds.

## Usage

``` syntax
<MetricThresholds>
  child elements
</MetricThresholds>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                               | Description                                                                               |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [**GreenYellowRedThreshold**](https://msdn.microsoft.com/library/windows/desktop/hh437597)<br/> | Thresholds used to generate Green/Yellow/Red reports. <br/> <br/>             |
| [**MetricThreshold**](metricthreshold.md)<br/>                 | Each metric threshold describes how a metric value is interpreted.<br/> <br/> |



### Child element sequence

``` syntax
(
  GreenYellowRedThreshold, 
  MetricThreshold
)
```

## Parent elements



| Element                                                     | Description                                                                           |
|-------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [**AssessmentManifest**](https://msdn.microsoft.com/library/windows/desktop/hh449288)<br/> | The root node of the assessment.<br/> <br/>                               |
| [**AssessmentRun**](assessmentrun.md)<br/>           | This node defines the instance of an assessment for execution.<br/> <br/> |



## Remarks

These are used to generate Green/Yellow/Red reports. This element should be treated as blank if it is empty.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> <dt>

[AXE Job Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449330)
</dt> </dl>

 

 





