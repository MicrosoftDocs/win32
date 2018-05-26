---
title: ActivityReference element
description: This element holds a reference to another related activity.
ms.assetid: 5C3EC828-56D9-4962-B235-F7224B6173C4
keywords:
- ActivityReference element Access Execution Engine
topic_type:
- apiref
api_name:
- ActivityReference
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ActivityReference element

This element holds a reference to another related activity.

## Usage

``` syntax
<ActivityReference
  ActivityID = "ID">
  text
</ActivityReference>
```

## Attributes



| Attribute                 | Type          | Required      | Description                                                         |
|---------------------------|---------------|---------------|---------------------------------------------------------------------|
| **ActivityID**<br/> | ID<br/> | No<br/> | Indicates the primary activity of the issue.<br/> <br/> |



## Text value

The text of this element refers to the **ID** attribute of another [**Activity**](activity.md) element. Source for this element is the assessment. This elements can appear more than once.

## Child elements

There are no child elements.

## Parent elements



| Element                                                   | Description                                                                                |
|-----------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [**RelatedActivities**](relatedactivities.md)<br/> | A container element for one or more **ActivityReference** elements.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





