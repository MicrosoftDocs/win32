---
title: Group element
description: A named arrangements of metric data.
ms.assetid: B8C29799-B688-4009-931F-B875FF9E4251
keywords:
- Group element Access Execution Engine
topic_type:
- apiref
api_name:
- Group
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Group element

A named arrangements of metric data.

## Usage

``` syntax
<Group>
  child elements
</Group>
```

## Attributes

There are no attributes.

## Child elements



| Element                                       | Description                                                                                                                                                                                                                                     |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Columns**](columns.md)<br/>         | A collection of the most important metrics gathered by the assessment. <br/> <br/>                                                                                                                                                  |
| [**Description**](description.md)<br/> | This node contains the description of the page. Groups do not require programmatic names, but [**Name**](name.md) and [**ToolTip**](tooltip.md) are used. The group s description is used for the header of the group.<br/> <br/> |
| [**PageLink**](pagelink.md)<br/>       | This node is the main page of the report.<br/> <br/>                                                                                                                                                                                |



### Child element sequence

``` syntax
DescriptionPageLinkColumns
```

## Parent elements



| Element                             | Description                                                             |
|-------------------------------------|-------------------------------------------------------------------------|
| [**Groups**](groups.md)<br/> | This node is a container for one or more groups.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





