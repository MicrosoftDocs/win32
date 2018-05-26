---
title: Link element
description: A hyperlink to more information about this solution.
ms.assetid: 2BBF6382-514E-4F04-AA2A-C62C7C824F05
keywords:
- Link element Access Execution Engine
topic_type:
- apiref
api_name:
- Link
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Link element

A hyperlink to more information about this solution.

## Usage

``` syntax
<Link>
  text
  child elements
</Link>
```

## Attributes

There are no attributes.

## Text value

A hyperlink to more information about this solution. Source for this element is the assessment.

## Child elements



| Element                                       | Description                                                    |
|-----------------------------------------------|----------------------------------------------------------------|
| [**LinkTitle**](linktitle.md)<br/>     | Text to be displayed for the hyperlink.<br/> <br/> |
| [**LinkToolTip**](linktooltip.md)<br/> | A tool tip for the hyperlink.<br/> <br/>           |
| [**LinkURI**](linkuri.md)<br/>         | The path to an executable or web page.<br/> <br/>  |



### Child element sequence

``` syntax
(
  LinkTitle, 
  LinkToolTip, 
  LinkURI
)
```

## Parent elements



| Element                                             | Description                                                                             |
|-----------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**AnalysisLinks**](https://msdn.microsoft.com/library/windows/desktop/hh449264)<br/> | A container for **Link** elements used to launch analysis tools.<br/> <br/> |
| [**SolutionLinks**](https://msdn.microsoft.com/library/windows/desktop/hh449557)<br/>   | A container for one or more **Link** elements.<br/> <br/>                   |
| [**Trace**](trace.md)<br/>                   | An optional trace file associated with this iteration.<br/> <br/>           |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





