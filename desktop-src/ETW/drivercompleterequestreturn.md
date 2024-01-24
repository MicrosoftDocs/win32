---
description: This class is the event type class for driver complete request return events. The following syntax is simplified from MOF code.
ms.assetid: 04505f8c-a11e-4bf7-91c0-fca1b5846d80
title: DriverCompleteRequestReturn class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DriverCompleteRequestReturn
- DriverCompleteRequestReturn.Irp
- DriverCompleteRequestReturn.UniqMatchId
api_type: 
- NA
api_location: 
---

# DriverCompleteRequestReturn class

This class is the event type class for driver complete request return events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{53}, EventTypeName{"DrvComplReqRet"}]
class DriverCompleteRequestReturn : DiskIo
{
  uint32 Irp;
  uint32 UniqMatchId;
};
```

## Members

The **DriverCompleteRequestReturn** class has these types of members:

-   [Properties](#properties)

### Properties

The **DriverCompleteRequestReturn** class has these properties.

<dl> <dt>

**Irp**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Pointer
</dt> </dl>

IO request packet.

</dd> <dt>

**UniqMatchId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2)
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

 

 




