---
description: The HWConfig\_CPU class is the event type class for CPU configuration events. The following syntax is simplified from MOF code.
ms.assetid: a94714c6-009c-4300-a0a0-b7b3ce94f91e
title: HWConfig_CPU class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- HWConfig_CPU
- HWConfig_CPU.MHz
- HWConfig_CPU.NumberOfProcessors
- HWConfig_CPU.MemSize
- HWConfig_CPU.PageSize
- HWConfig_CPU.AllocationGranularity
- HWConfig_CPU.ComputerName
api_type: 
- NA
api_location: 
---

# HWConfig\_CPU class

The **HWConfig\_CPU** class is the event type class for CPU configuration events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(10), EventTypeName("CPU")]
class HWConfig_CPU : HWConfig
{
  uint32 MHz;
  uint32 NumberOfProcessors;
  uint32 MemSize;
  uint32 PageSize;
  uint32 AllocationGranularity;
  string ComputerName;
};
```

## Members

The **HWConfig\_CPU** class has these types of members:

-   [Properties](#properties)

### Properties

The **HWConfig\_CPU** class has these properties.

<dl> <dt>

AllocationGranularity
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(5)
</dt> </dl>

Granularity with which virtual memory is allocated.

</dd> <dt>

ComputerName
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(6), StringTermination("NullTerminated"), Format("w")
</dt> </dl>

Name of the computer.

</dd> <dt>

MemSize
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3)
</dt> </dl>

Total amount of physical memory available to the operating system.

</dd> <dt>

MHz
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1)
</dt> </dl>

Maximum speed of the processor, in megahertz.

</dd> <dt>

NumberOfProcessors
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2)
</dt> </dl>

Number of processors on the computer.

</dd> <dt>

PageSize
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4)
</dt> </dl>

Size of a swap page, in bytes.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                   |



## See also

<dl> <dt>

[**HWConfig**](hwconfig.md)
</dt> </dl>

 

 




