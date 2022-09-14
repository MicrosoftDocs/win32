---
description: This class is the event type class that marks the beginning of the disk I/O read, write, and flush events. The following syntax is simplified from MOF code.
ms.assetid: 96543ef9-cc2b-4d9a-86a8-f2458439e4d8
title: DiskIo_TypeGroup2 class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DiskIo_TypeGroup2
- DiskIo_TypeGroup2.Irp
- DiskIo_TypeGroup2.IssuingThreadId
api_type: 
- NA
api_location: 
---

# DiskIo\_TypeGroup2 class

This class is the event type class that marks the beginning of the disk I/O read, write, and flush events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{12, 13, 15}, EventTypeName{"ReadInit", "WriteInit", "FlushInit"}]
class DiskIo_TypeGroup2 : DiskIo
{
  uint32 Irp;
  uint32 IssuingThreadId;
};
```

## Members

The **DiskIo\_TypeGroup2** class has these types of members:

-   [Properties](#properties)

### Properties

The **DiskIo\_TypeGroup2** class has these properties.

<dl> <dt>

**Irp**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](event-tracing-mof-qualifiers.md) (1), [**Pointer**](event-tracing-mof-qualifiers.md)
</dt> </dl>

I/O request packet. This property identifies the IO activity.

</dd> <dt>

**IssuingThreadId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](event-tracing-mof-qualifiers.md) (2)
</dt> </dl>

The identifier of the issuing thread.

**Windows Server 2008 R2, Windows Server 2008, Windows 7 and Windows Vista:** This property is not supported.

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

 

 




