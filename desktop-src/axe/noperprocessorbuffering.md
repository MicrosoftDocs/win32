---
title: NoPerProcessorBuffering element
description: Configures ETW to write all ETW events to a shared buffer regardless of which processor generated the event.
ms.assetid: '57C5EA06-D074-4683-981D-609B4C3E15D5'
keywords: ["NoPerProcessorBuffering element Access Execution Engine"]
topic_type:
- apiref
api_name:
- NoPerProcessorBuffering
api_type:
- Schema
---

# NoPerProcessorBuffering element

Configures ETW to write all ETW events to a shared buffer regardless of which processor generated the event.

## Usage

``` syntax
<NoPerProcessorBuffering>
  text
</NoPerProcessorBuffering>
```

## Attributes

There are no attributes.

## Text value

This node maps to the **EVENT\_TRACE\_NO\_PER\_PROCESSOR\_BUFFERING** constant in the [Logging Mode Constants](https://msdn.microsoft.com/library/windows/desktop/aa364080) for the **LogFileMode** member of the [**EVENT\_TRACE\_PROPERTIES**](https://msdn.microsoft.com/library/windows/desktop/aa363784) structure

## Child elements

There are no child elements.

## Parent elements



| Element                                       | Description                                                                                |
|-----------------------------------------------|--------------------------------------------------------------------------------------------|
| [**LoggingMode**](loggingmode.md)<br/> | Modifies the logging modes used by ETW for tracing the assessment. <br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





