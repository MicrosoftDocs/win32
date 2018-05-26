---
title: LoggingMode element
description: Modifies the logging modes used by ETW for tracing the assessment.
ms.assetid: 2DC62A46-B1E6-4968-BF25-0A434629FD05
keywords:
- LoggingMode element Access Execution Engine
topic_type:
- apiref
api_name:
- LoggingMode
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LoggingMode element

Modifies the logging modes used by ETW for tracing the assessment.

## Usage

``` syntax
<LoggingMode>
  text
  child elements
</LoggingMode>
```

## Attributes

There are no attributes.

## Text value

The value must be consistent with the requirements for the **LogFileMode** member of the [**EVENT\_TRACE\_PROPERTIES**](https://msdn.microsoft.com/library/windows/desktop/aa363784) structure. Solutions use a user-mode private session.

## Child elements



| Element                                                               | Description                                                                                                                         |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [**NoPerProcessorBuffering**](noperprocessorbuffering.md)<br/> | Configures ETW to write all ETW events to a shared buffer regardless of which processor generated the event.<br/> <br/> |



### Child element sequence

``` syntax
NoPerProcessorBuffering
```

## Parent elements



| Element                                         | Description                                                                                             |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [**EventTracing**](eventtracing.md)<br/> | Specifies a configuration for the use of Event Tracing for Windows (ETW) by AXE.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





