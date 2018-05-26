---
title: SecondaryStatistic element
description: Describes the secondary descriptive statistic for the metric recommended by the assessment author.
ms.assetid: EF96DA29-2DA3-477A-99EC-9378DB10338B
keywords:
- SecondaryStatistic element Access Execution Engine
topic_type:
- apiref
api_name:
- SecondaryStatistic
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SecondaryStatistic element

Describes the secondary descriptive statistic for the metric recommended by the assessment author.

## Usage

``` syntax
<SecondaryStatistic>
  child elements
</SecondaryStatistic>
```

## Attributes

There are no attributes.

## Child elements



| Element                                     | Description                                                            |
|---------------------------------------------|------------------------------------------------------------------------|
| [**Mean**](mean.md)<br/>             | The secondary statistic is the arithmetic mean.<br/> <br/> |
| [**Median**](median.md)<br/>         | The secondary statistic is the median.<br/> <br/>          |
| [**None**](none--statistic-.md)<br/> | No secondary statistic.<br/> <br/>                         |



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

 

 





