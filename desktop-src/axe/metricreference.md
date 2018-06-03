---
title: MetricReference element
description: This element holds a reference to a metric related to this activity.
ms.assetid: 68B75CD4-5BE1-4D12-B38B-BDBA403427A1
keywords:
- MetricReference element Access Execution Engine
topic_type:
- apiref
api_name:
- MetricReference
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MetricReference element

This element holds a reference to a metric related to this activity.

## Usage

``` syntax
<MetricReference>
  text
</MetricReference>
```

## Attributes

There are no attributes.

## Text value

The text of this element refers to the [**ProgrammaticName**](programmaticname.md) of the metric to associated with this activity. This elements can appear more than once.

## Child elements

There are no child elements.

## Parent elements



| Element                                               | Description                                                              |
|-------------------------------------------------------|--------------------------------------------------------------------------|
| [**AffectedMetrics**](affectedmetrics.md)<br/> | Enables a metric value to be related to an issue.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





