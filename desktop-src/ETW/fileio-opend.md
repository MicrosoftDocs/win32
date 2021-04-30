---
description: This class is the event type class for file operation end events. The following syntax is simplified from MOF code.
ms.assetid: 3925d5bf-f412-4248-a61f-e667efa9debd
title: FileIo_OpEnd class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FileIo_OpEnd
- FileIo_OpEnd.IrpPtr
- FileIo_OpEnd.ExtraInfo
- FileIo_OpEnd.NtStatus
api_type: 
- NA
api_location: 
---

# FileIo\_OpEnd class

This class is the event type class for file operation end events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{76}, EventTypeName{"OperationEnd"}]
class FileIo_OpEnd : FileIo
{
  uint32 IrpPtr;
  uint32 ExtraInfo;
  uint32 NtStatus;
};
```

## Members

The **FileIo\_OpEnd** class has these types of members:

-   [Properties](#properties)

### Properties

The **FileIo\_OpEnd** class has these properties.

<dl> <dt>

**ExtraInfo**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2), Pointer
</dt> </dl>

Extra information returned by the file system for the operation. For example for a read request, the actual number of bytes that were read.

</dd> <dt>

**IrpPtr**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Pointer
</dt> </dl>

IO request packet. This property identifies the IO activity that is ending.

</dd> <dt>

**NtStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3)
</dt> </dl>

Return value from the operation.

</dd> </dl>

## Remarks

[**FileIo**](fileio.md) events are logged at the beginning of the operation. OpEnd events can be enabled separately to indicate the end of those operations. Irp can be used to correlate the begin and end events.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**FileIo**](fileio.md)
</dt> </dl>

 

 




