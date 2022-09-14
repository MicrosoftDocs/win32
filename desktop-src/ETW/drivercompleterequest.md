---
description: This class is the event type class for driver complete request events. The following syntax is simplified from MOF code.
ms.assetid: c9c9be05-c1c6-4d77-a47a-44a61ebfcdc7
title: DriverCompleteRequest class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DriverCompleteRequest
- DriverCompleteRequest.RoutineAddr
- DriverCompleteRequest.Irp
- DriverCompleteRequest.UniqMatchId
api_type: 
- NA
api_location: 
---

# DriverCompleteRequest class

This class is the event type class for driver complete request events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{52}, EventTypeName{"DrvComplReq"}]
class DriverCompleteRequest : DiskIo
{
  uint32 RoutineAddr;
  uint32 Irp;
  uint32 UniqMatchId;
};
```

## Members

The **DriverCompleteRequest** class has these types of members:

-   [Properties](#properties)

### Properties

The **DriverCompleteRequest** class has these properties.

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

**RoutineAddr**
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

Identifier that uniquely identifies request. Use this identifier to correlate with the other driver events, for example, the [**DriverCompleteRequestReturn**](drivercompleterequestreturn.md) event.

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

 

 




