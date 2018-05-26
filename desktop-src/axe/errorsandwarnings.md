---
title: ErrorsAndWarnings element
description: A container to hold assessment errors and warnings.
ms.assetid: F2E9FC0F-F6F2-4176-8ABF-1760B0B3DB73
keywords:
- ErrorsAndWarnings element Access Execution Engine
topic_type:
- apiref
api_name:
- ErrorsAndWarnings
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ErrorsAndWarnings element

A container to hold assessment errors and warnings.

## Usage

``` syntax
<ErrorsAndWarnings>
  child elements
</ErrorsAndWarnings>
```

## Attributes

There are no attributes.

## Child elements



| Element                               | Description                                              |
|---------------------------------------|----------------------------------------------------------|
| [**Error**](error.md)<br/>     | This element describes an error.<br/> <br/>  |
| [**Warning**](warning.md)<br/> | This element describes a warning.<br/> <br/> |



### Child element sequence

``` syntax
(
  Error, 
  Warning
)
```

## Parent elements



| Element                                                 | Description                                                                |
|---------------------------------------------------------|----------------------------------------------------------------------------|
| [**AssessmentResult**](assessmentresult.md)<br/> | Describes the results for an individual assessment.<br/> <br/> |



## Remarks

This element may contain zero or more child elements.

It is possible for an assessment to produce only errors, warnings or messages and no metric values. Solutions should be prepared to handle this condition.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





