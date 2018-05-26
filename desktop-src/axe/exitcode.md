---
title: ExitCode element
description: This element holds the exit code for an assessment s process.
ms.assetid: c71c84ca-5a68-4b6e-a261-2b5d42fe1d4f
keywords:
- ExitCode element Access Execution Engine
topic_type:
- apiref
api_name:
- ExitCode
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ExitCode element

This element holds the exit code for an assessment s process. The meaning of the value contained by this element depends on meta information in the assessment manifest. AXE inserts this element at runtime. The result files written by AXE always contain this element.

## Usage

``` syntax
<ExitCode>
  text
</ExitCode>
```

## Attributes

There are no attributes.

## Text value

The exit code for an assessment s process.

## Child elements

There are no child elements.

## Parent elements



| Element                                                 | Description                                                                |
|---------------------------------------------------------|----------------------------------------------------------------------------|
| [**AssessmentResult**](assessmentresult.md)<br/> | Describes the results for an individual assessment.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





