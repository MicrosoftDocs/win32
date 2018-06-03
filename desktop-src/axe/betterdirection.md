---
title: BetterDirection element
description: Defines which sense of relative change of a metric is to be considered improvement.
ms.assetid: 97D15CC6-1678-4BCC-AC53-3C943343C2AA
keywords:
- BetterDirection element Access Execution Engine
topic_type:
- apiref
api_name:
- BetterDirection
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BetterDirection element

Defines which sense of relative change of a metric is to be considered improvement. For some metrics "higher" is better, for other metrics lower is better. This element must contain exactly one of the following empty tags.

## Usage

``` syntax
<BetterDirection>
  child elements
</BetterDirection>
```

## Attributes

There are no attributes.

## Child elements



| Element                                           | Description                                                                |
|---------------------------------------------------|----------------------------------------------------------------------------|
| [**Higher**](higher.md)<br/>               | Indicates that higher values are better than lower.<br/> <br/> |
| [**Lower**](lower.md)<br/>                 | Indicates that lower values are better than higher.<br/> <br/> |
| [**None**](none--betterdirection-.md)<br/> | Neither higher nor lower values are better.<br/> <br/>         |



### Child element sequence

``` syntax
NoneLowerHigher
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

 

 





