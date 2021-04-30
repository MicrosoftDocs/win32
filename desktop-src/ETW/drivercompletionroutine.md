---
description: This class is the event type class for driver complete routine events. The following syntax is simplified from MOF code.
ms.assetid: deb4f0b2-d73f-4ccf-b39b-6e92b32489fb
title: DriverCompletionRoutine class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DriverCompletionRoutine
- DriverCompletionRoutine.Routine
- DriverCompletionRoutine.Irp
- DriverCompletionRoutine.UniqMatchId
api_type: 
- NA
api_location: 
---

# DriverCompletionRoutine class

This class is the event type class for driver complete routine events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{37}, EventTypeName{"DrvComplRout"}]
class DriverCompletionRoutine : DiskIo
{
  uint32 Routine;
  uint32 Irp;
  uint32 UniqMatchId;
};
```

## Members

The **DriverCompletionRoutine** class has these types of members:

-   [Properties](#properties)

### Properties

The **DriverCompletionRoutine** class has these properties.

<dl> <dt>

**Irp**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2), Pointer
</dt> </dl>

IO request packet.

</dd> <dt>

**Routine**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Pointer
</dt> </dl>

Address of the driver function being called.

</dd> <dt>

**UniqMatchId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3)
</dt> </dl>

Identifier that uniquely identifies request. Use this identifier to correlate with the other driver events, for example, the [**DriverCompleteRequest**](drivercompleterequest.md) event.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**DiskIo**](diskio.md)
</dt> </dl>

 

 




