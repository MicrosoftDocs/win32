---
title: BufferSize element
description: Specifies the size of each ETW buffer.
ms.assetid: 2E8BD24C-F7A3-4056-B028-35833C402812
keywords:
- BufferSize element Access Execution Engine
topic_type:
- apiref
api_name:
- BufferSize
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BufferSize element

Specifies the size of each ETW buffer.

## Usage

``` syntax
<BufferSize>
  text
</BufferSize>
```

## Attributes

There are no attributes.

## Text value

Specifies the size of each ETW buffer in kilobytes. By default, the AXE core uses 64KB buffers. The value must be consistent with the requirements for the **BufferSize** member of the [**EVENT\_TRACE\_PROPERTIES**](https://msdn.microsoft.com/library/windows/desktop/aa363784) structure.

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

 

 





