---
title: Impact element
description: Describes the impact of the issue.
ms.assetid: 0BF03CD6-DCF6-4108-88A0-7EE8A565FEAA
keywords:
- Impact element Access Execution Engine
topic_type:
- apiref
api_name:
- Impact
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Impact element

Describes the impact of the issue. Source for this element is the assessment.

## Usage

``` syntax
<Impact
  Severity  = "text">
  child elements
</Impact>
```

## Attributes



| Attribute                | Type            | Required      | Description                                                                                                                                                             |
|--------------------------|-----------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Severity** <br/> | text<br/> | No<br/> | Describes how serious the issue is. The attribute is a numeric value between 0 and 3 inclusive. Zero is the most severe. 3 is the least severe. <br/> <br/> |



## Child elements



| Element                                                   | Description                                                                                                         |
|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [**RelatedActivities**](relatedactivities.md)<br/> | A container element for one or more [**ActivityReference**](activityreference.md) elements.<br/> <br/> |



### Child element sequence

``` syntax
(
  RelatedActivities
)
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

 

 





