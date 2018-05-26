---
title: MinimumBuffers element
description: Specifies the minimum number of buffers ETW should create for tracing the assessment.
ms.assetid: 32DD845E-B0D7-4527-8429-CDE766B3CB89
keywords:
- MinimumBuffers element Access Execution Engine
topic_type:
- apiref
api_name:
- MinimumBuffers
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MinimumBuffers element

Specifies the minimum number of buffers ETW should create for tracing the assessment.

## Usage

``` syntax
<MinimumBuffers>
  text
</MinimumBuffers>
```

## Attributes

There are no attributes.

## Text value

The minimum number of buffers ETW should create for tracing the assessment. By default, AXE requests 2 buffers for each processor The value must be consistent with the requirements of the **MinimumBuffers** member of the [**EVENT\_TRACE\_PROPERTIES**](https://msdn.microsoft.com/library/windows/desktop/aa363784) structure.

## Child elements

There are no child elements.

## Parent elements



| Element                                         | Description                                                                                             |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [**EventTracing**](eventtracing.md)<br/> | Specifies a configuration for the use of Event Tracing for Windows (ETW) by AXE.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





