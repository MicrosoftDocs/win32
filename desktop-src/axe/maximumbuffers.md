---
title: MaximumBuffers element
description: Specifies the maximum number of buffers ETW subsystem should create for tracing the assessment.
ms.assetid: '97DF4B9B-B03A-4730-9E33-54942E7F91AA'
keywords: ["MaximumBuffers element Access Execution Engine"]
topic_type:
- apiref
api_name:
- MaximumBuffers
api_type:
- Schema
---

# MaximumBuffers element

Specifies the maximum number of buffers ETW subsystem should create for tracing the assessment.

## Usage

``` syntax
<MaximumBuffers>
  text
</MaximumBuffers>
```

## Attributes

There are no attributes.

## Text value

The maximum number of buffers ETW should create for tracing the assessment. By default, the AXE requests 4 times the minimum buffer count. The value must be consistent with the requirements of the **MaximumBuffers** member of the [**EVENT\_TRACE\_PROPERTIES**](https://msdn.microsoft.com/library/windows/desktop/aa363784) structure.

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

 

 





