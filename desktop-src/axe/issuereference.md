---
title: IssueReference element
description: Relates the impact of the activity back to the issue.
ms.assetid: 2C68D5F7-664E-46E8-A876-44ED22675719
keywords:
- IssueReference element Access Execution Engine
topic_type:
- apiref
api_name:
- IssueReference
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IssueReference element

Relates the impact of the activity back to the issue. Source for this element is the assessment. This elements can appear more than once.

## Usage

``` syntax
<IssueReference
  IssueID = "ID"/>
```

## Attributes



| Attribute              | Type          | Required      | Description                                          |
|------------------------|---------------|---------------|------------------------------------------------------|
| **IssueID**<br/> | ID<br/> | No<br/> | The ID attribute of an issue.<br/> <br/> |



## Child elements

There are no child elements.

## Parent elements



| Element                                     | Description                                                                                                                                                   |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**References**](references.md)<br/> | Holds the [**MetricReference**](metricreference.md), **IssueReference** and [**ActivityReference**](activityreference.md) elements. <br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





