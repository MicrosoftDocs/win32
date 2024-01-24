---
description: An abstract class from which all event trace classes are derived.
ms.assetid: 03eea902-5050-4ab2-8a72-9bff7777e234
title: EventTrace class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EventTrace
- EventTrace.EventSize
- EventTrace.ReservedHeaderField
- EventTrace.EventType
- EventTrace.TraceLevel
- EventTrace.TraceVersion
- EventTrace.ThreadId
- EventTrace.TimeStamp
- EventTrace.EventGuid
- EventTrace.KernelTime
- EventTrace.UserTime
- EventTrace.InstanceId
- EventTrace.ParentGuid
- EventTrace.ParentInstanceId
- EventTrace.MofData
- EventTrace.MofLength
api_type: 
- NA
api_location: 
---

# EventTrace class

An abstract class from which all event trace classes are derived.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[abstract]
class EventTrace
{
  uint16 EventSize;
  uint16 ReservedHeaderField;
  uint8  EventType;
  uint8  TraceLevel;
  uint16 TraceVersion;
  uint64 ThreadId;
  uint64 TimeStamp;
  uint8  EventGuid[];
  uint32 KernelTime;
  uint32 UserTime;
  uint32 InstanceId;
  uint8  ParentGuid[];
  uint32 ParentInstanceId;
  uint32 MofData;
  uint32 MofLength;
};
```

## Members

The **EventTrace** class has these types of members:

-   [Properties](#properties)

### Properties

The **EventTrace** class has these properties.

<dl> <dt>

**EventGuid**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (8), **Max** (16)
</dt> </dl>

Event trace class GUID of this event.

</dd> <dt>

**EventSize**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (1)
</dt> </dl>

Total number of bytes of the event.

</dd> <dt>

**EventType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (3)
</dt> </dl>

Provider-defined event type. Tells you which event type class to use to decipher the provider-defined event data (the data pointed to by **MofData**.

</dd> <dt>

**InstanceId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (11)
</dt> </dl>

Identifier of this event instance.

</dd> <dt>

**KernelTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (9)
</dt> </dl>

Elapsed execution time for kernel-mode instructions, in CPU ticks.

</dd> <dt>

**MofData**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (14), **Pointer**
</dt> </dl>

Pointer to the provider-specific event data.

</dd> <dt>

**MofLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (15)
</dt> </dl>

Length of the provider-specific event data.

</dd> <dt>

**ParentGuid**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (12), **Max** (16)
</dt> </dl>

Event trace class GUID of the parent instance.

</dd> <dt>

**ParentInstanceId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (13)
</dt> </dl>

Identifier of the parent instance data.

</dd> <dt>

**ReservedHeaderField**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (2)
</dt> </dl>

Reserved.

</dd> <dt>

**ThreadId**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (6), **Pointer**
</dt> </dl>

Identifies the thread that generated the event.

</dd> <dt>

**TimeStamp**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (7)
</dt> </dl>

Contains the date and time when the event occurred.

</dd> <dt>

**TraceLevel**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (4)
</dt> </dl>

Provider-defined value that defines the severity level used to generate the event.

</dd> <dt>

**TraceVersion**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (5)
</dt> </dl>

Provider-defined version number of the event trace class used to generate the event.

</dd> <dt>

**UserTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (10)
</dt> </dl>

Elapsed execution time for user-mode instructions, in CPU ticks.

</dd> </dl>

## Remarks

Do not use these properties.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| MOF<br/>                      | <dl> <dt>Wmi.mof</dt> </dl> |



 

 




