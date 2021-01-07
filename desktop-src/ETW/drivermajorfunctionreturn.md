---
description: This class is the event type class for driver major function call return events. The following syntax is simplified from MOF code.
ms.assetid: b3358935-d6fb-49eb-bdf7-4366b4fd14c5
title: DriverMajorFunctionReturn class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DriverMajorFunctionReturn
- DriverMajorFunctionReturn.Irp
- DriverMajorFunctionReturn.UniqMatchId
api_type: 
- NA
api_location: 
---

# DriverMajorFunctionReturn class

This class is the event type class for driver major function call return events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{35}, EventTypeName{"DrvMjFnRet"}]
class DriverMajorFunctionReturn : DiskIo
{
  uint32 Irp;
  uint32 UniqMatchId;
};
```

## Members

The **DriverMajorFunctionReturn** class has these types of members:

-   [Properties](#properties)

### Properties

The **DriverMajorFunctionReturn** class has these properties.

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

 

 




