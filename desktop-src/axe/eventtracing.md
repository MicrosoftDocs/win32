---
title: EventTracing element
description: Specifies a configuration for the use of Event Tracing for Windows (ETW) by AXE.
ms.assetid: 8DD866D6-0EFE-4A73-8F3D-9264468DAC0E
keywords:
- EventTracing element Access Execution Engine
topic_type:
- apiref
api_name:
- EventTracing
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EventTracing element

Specifies a configuration for the use of Event Tracing for Windows (ETW) by AXE.

The values for the child nodes must be consistent with the requirements for the corresponding members of the [**EVENT\_TRACE\_PROPERTIES**](https://msdn.microsoft.com/library/windows/desktop/aa363784) structure.

## Usage

``` syntax
<EventTracing>
  child elements
</EventTracing>
```

## Attributes

There are no attributes.

## Child elements



| Element                                             | Description                                                                                                            |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**BufferSize**](buffersize.md)<br/>         | Specifies the size of each ETW buffer.<br/> <br/>                                                          |
| [**LoggingMode**](loggingmode.md)<br/>       | Modifies the logging modes used by ETW for tracing the assessment. <br/> <br/>                             |
| [**MaximumBuffers**](maximumbuffers.md)<br/> | Specifies the maximum number of buffers ETW subsystem should create for tracing the assessment.<br/> <br/> |
| [**MinimumBuffers**](minimumbuffers.md)<br/> | Specifies the minimum number of buffers ETW should create for tracing the assessment.<br/> <br/>           |



### Child element sequence

``` syntax
BufferSizeLoggingModeMaximumBuffersMinimumBuffers
```

## Parent elements



| Element                                     | Description                                                          |
|---------------------------------------------|----------------------------------------------------------------------|
| [**Properties**](properties.md)<br/> | This element describes assessment properties.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





