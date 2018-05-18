---
title: WatchDogTimeOut element
description: Describes a time limit for when a solution should cancel or terminate an assessment.
ms.assetid: 'DDB832DC-CFFC-41F1-B663-F85189E52493'
keywords: ["WatchDogTimeOut element Access Execution Engine"]
topic_type:
- apiref
api_name:
- WatchDogTimeOut
api_type:
- Schema
---

# WatchDogTimeOut element

Describes a time limit for when a solution should cancel or terminate an assessment. This value is only used by Windows Assessment Services (WAS.)

## Usage

``` syntax
<WatchDogTimeOut>
  text
</WatchDogTimeOut>
```

## Attributes

There are no attributes.

## Text value

The duration of the time limit for the assessment in seconds.

## Child elements

There are no child elements.

## Parent elements



| Element                                     | Description                                                          |
|---------------------------------------------|----------------------------------------------------------------------|
| [**Properties**](properties.md)<br/> | This element describes assessment properties.<br/> <br/> |



## Remarks

Windows Assessment Services (WAS) uses this value to limit the amount of time an assessment can run. If the assessment exceeds the value while running under WAS, it will cancel the assessment and run the next assessment in the queue.

The developer should set this value to the maximum amount of time (in seconds) that the assessment should run, and adding sufficient buffer time to accommodate external factors such as processor performance and low memory situations. In most cases developers can start by doubling or tripling the **EstimatedRunTime** value, testing on slower machines, and then adjusting accordingly.

Note that neither the framework, Assessment Launcher or AXE.EXE utilize this value to limit the run time of the assessment.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





