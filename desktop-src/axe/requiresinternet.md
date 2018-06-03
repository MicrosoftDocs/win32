---
title: RequiresInternet element
description: If present this assessment requires an working internet connection.
ms.assetid: A5CA101C-B3FF-4744-AD36-D54D6C7B7514
keywords:
- RequiresInternet element Access Execution Engine
topic_type:
- apiref
api_name:
- RequiresInternet
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RequiresInternet element

If present this assessment requires an working internet connection.

## Usage

``` syntax
<RequiresInternet/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                     | Description                                               |
|---------------------------------------------|-----------------------------------------------------------|
| [**Properties**](properties.md)<br/> | This element describes properties.<br/> <br/> |



## Remarks

This is only used as a presentation hint for programs that support the selection of assessments and the creation of jobs. No checking is done for an actual Internet connection when the assessment is executed by the AXE engine.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





