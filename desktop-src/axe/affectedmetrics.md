---
title: AffectedMetrics element
description: Enables a metric value to be related to an issue.
ms.assetid: A7DB5724-F68C-4713-8BEE-D092D687CBA2
keywords:
- AffectedMetrics element Access Execution Engine
topic_type:
- apiref
api_name:
- AffectedMetrics
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AffectedMetrics element

Enables a metric value to be related to an issue.

## Usage

``` syntax
<AffectedMetrics>
  child elements
</AffectedMetrics>
```

## Attributes

There are no attributes.

## Child elements



| Element                                               | Description                                                                                 |
|-------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [**MetricReference**](metricreference.md)<br/> | This element holds a reference to a metric related to this activity.<br/> <br/> |



### Child element sequence

``` syntax
MetricReference
```

## Parent elements



| Element                           | Description                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| [**Issue**](issue.md)<br/> | This element holds information about a single issue.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





