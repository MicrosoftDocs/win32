---
title: PresentationHints element
description: The root node of the presentation hints section.
ms.assetid: BD18FE9A-DED3-42CE-8D3A-D6CAA89AEF56
keywords:
- PresentationHints element Access Execution Engine
topic_type:
- apiref
api_name:
- PresentationHints
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PresentationHints element

The root node of the presentation hints section. Presentation hints provide information on how to display the results of the assessment in a meaningful way.

## Usage

``` syntax
<PresentationHints>
  child elements
</PresentationHints>
```

## Attributes

There are no attributes.

## Child elements



| Element                                 | Description                                                                                    |
|-----------------------------------------|------------------------------------------------------------------------------------------------|
| [**Columns**](columns.md)<br/>   | A collection of the most important metrics gathered by the assessment. <br/> <br/> |
| [**PageLink**](pagelink.md)<br/> | This node is the main page of the report.<br/> <br/>                               |
| [**Pages**](pages.md)<br/>       | A collection of Page nodes describing all pages in the report.<br/> <br/>          |



### Child element sequence

``` syntax
ColumnsPageLinkPages
```

## Parent elements



| Element                                                           | Description                                                             |
|-------------------------------------------------------------------|-------------------------------------------------------------------------|
| [**AXEAssessmentManifest**](axeassessmentmanifest.md)<br/> | This is the root node of an assessment manifest.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





