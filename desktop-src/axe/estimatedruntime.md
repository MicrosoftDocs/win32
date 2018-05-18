---
title: EstimatedRunTime element
description: Describes the estimated run time of the assessment.
ms.assetid: '45BB4259-D6D9-49BE-B1D7-23A561417692'
keywords: ["EstimatedRunTime element Access Execution Engine"]
topic_type:
- apiref
api_name:
- EstimatedRunTime
api_type:
- Schema
---

# EstimatedRunTime element

Describes the estimated run time of the assessment.

## Usage

``` syntax
<EstimatedRunTime>
  text
</EstimatedRunTime>
```

## Attributes

There are no attributes.

## Text value

Describes the estimated run time of the assessment in seconds.

## Child elements

There are no child elements.

## Parent elements



| Element                                     | Description                                            |
|---------------------------------------------|--------------------------------------------------------|
| [**Properties**](properties.md)<br/> | This node describes properties.<br/> <br/> |



## Remarks

This value is optional and is used only to set expectations for the user. It is not used by the framework or tools to limit the amount of time that the assessment will be allowed to run.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> <dt>

[**WatchDogTimeOut**](watchdogtimeout.md)
</dt> </dl>

 

 





