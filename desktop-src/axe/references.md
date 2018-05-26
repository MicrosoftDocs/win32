---
title: References element
description: Holds the MetricReference, IssueReference and ActivityReference element.
ms.assetid: BBB8A867-D1D3-4769-89AB-9524449CD2D5
keywords:
- References element Access Execution Engine
topic_type:
- apiref
api_name:
- References
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# References element

Holds the [**MetricReference**](metricreference.md), [**IssueReference**](issuereference.md) and [**ActivityReference**](activityreference.md) element.

## Usage

``` syntax
<References>
  child elements
</References>
```

## Attributes

There are no attributes.

## Child elements



| Element                                               | Description                                                                                 |
|-------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [**IssueReference**](issuereference.md)<br/>   | Relates the impact of the activity back to the issue.<br/> <br/>                |
| [**MetricReference**](metricreference.md)<br/> | This element holds a reference to a metric related to this activity.<br/> <br/> |



### Child element sequence

``` syntax
(
  MetricReference, 
  IssueReference
)
```

## Parent elements



| Element                                 | Description                                                                               |
|-----------------------------------------|-------------------------------------------------------------------------------------------|
| [**Activity**](activity.md)<br/> | This element holds information about a category of related issues.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





