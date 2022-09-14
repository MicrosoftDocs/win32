---
description: This class is the event type class for sampled profile events. The following syntax is simplified from MOF code.
ms.assetid: 75ea1e5e-2554-40bb-aa9d-c6d4942c5801
title: SampledProfile class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SampledProfile
- SampledProfile.InstructionPointer
- SampledProfile.ThreadId
- SampledProfile.Count
api_type: 
- NA
api_location: 
---

# SampledProfile class

This class is the event type class for sampled profile events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{46}, EventTypeName{"SampleProfile"}]
class SampledProfile : PerfInfo
{
  uint32 InstructionPointer;
  uint32 ThreadId;
  uint32 Count;
};
```

## Members

The **SampledProfile** class has these types of members:

-   [Properties](#properties)

### Properties

The **SampledProfile** class has these properties.

<dl> <dt>

**Count**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3)
</dt> </dl>

Not used.

</dd> <dt>

**InstructionPointer**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Pointer
</dt> </dl>

Address of the image that was running at the time the processor was sampled.

</dd> <dt>

**ThreadId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2)
</dt> </dl>

Thread identifier of the thread that was running at the time the processor was sampled.

</dd> </dl>

## Remarks

These events provide a sampled execution profile. The event records what was being executed on the processor. You can use the Image events to identify the binary module containing that instruction. You can then use this information to produce an execution profile for the duration of the trace.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




