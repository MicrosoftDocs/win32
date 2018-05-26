---
title: Solution element
description: This element holds information about a solution for a single issue.
ms.assetid: B4144705-9AF8-4A0C-8D21-AFCE729DBA3B
keywords:
- Solution element Access Execution Engine
topic_type:
- apiref
api_name:
- Solution
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Solution element

This element holds information about a solution for a single issue. Source for this element is the assessment.

## Usage

``` syntax
<Solution>
  child elements
</Solution>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                       | Description                                                                       |
|---------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [**SolutionDescription**](https://msdn.microsoft.com/library/windows/desktop/hh449554)<br/> | Describes the solution for a single issue.<br/> <br/>                 |
| [**SolutionLinks**](https://msdn.microsoft.com/library/windows/desktop/hh449557)<br/>             | A container for one or more [**Link**](link.md) elements.<br/> <br/> |



### Child element sequence

``` syntax
(
  SolutionDescription, 
  SolutionLinks
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

 

 





