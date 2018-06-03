---
title: PrimaryStatistic element
description: Describes the primary descriptive statistic for the metric recommended by the assessment author.
ms.assetid: 9F6AFFBE-4681-48FF-8F82-5A3AE77C4752
keywords:
- PrimaryStatistic element Access Execution Engine
topic_type:
- apiref
api_name:
- PrimaryStatistic
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PrimaryStatistic element

Describes the primary descriptive statistic for the metric recommended by the assessment author. This must contain exactly one of the following empty tags.

## Usage

``` syntax
<PrimaryStatistic>
  child elements
</PrimaryStatistic>
```

## Attributes

There are no attributes.

## Child elements



| Element                                     | Description                                                          |
|---------------------------------------------|----------------------------------------------------------------------|
| [**Mean**](mean.md)<br/>             | The primary statistic is the arithmetic mean.<br/> <br/> |
| [**Median**](median.md)<br/>         | The primary statistic is the median.<br/> <br/>          |
| [**None**](none--statistic-.md)<br/> | No primary statistic.<br/> <br/>                         |



### Child element sequence

``` syntax
(
  None, 
  Mean, 
  Median
)
```

## Parent elements



| Element                                                 | Description                                                                          |
|---------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**MetricDefinition**](metricdefinition.md)<br/> | This element describes the metrics produced by an assessment.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





