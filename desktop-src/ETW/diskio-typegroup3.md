---
description: This class is the event type class for disk I/O flush events. The following syntax is simplified from MOF code.
ms.assetid: 7f0c9bd4-e4d3-49c1-ae72-f6bdf938099f
title: DiskIo_TypeGroup3 class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DiskIo_TypeGroup3
- DiskIo_TypeGroup3.DiskNumber
- DiskIo_TypeGroup3.IrpFlags
- DiskIo_TypeGroup3.HighResResponseTime
- DiskIo_TypeGroup3.Irp
- DiskIo_TypeGroup3.IssuingThreadId
api_type: 
- NA
api_location: 
---

# DiskIo\_TypeGroup3 class

This class is the event type class for disk I/O flush events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{14}, EventTypeName{"FlushBuffers"}]
class DiskIo_TypeGroup3 : DiskIo
{
  uint32 DiskNumber;
  uint32 IrpFlags;
  uint64 HighResResponseTime;
  uint32 Irp;
  uint32 IssuingThreadId;
};
```

## Members

The **DiskIo\_TypeGroup3** class has these types of members:

-   [Properties](#properties)

### Properties

The **DiskIo\_TypeGroup3** class has these properties.

<dl> <dt>

**DiskNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](event-tracing-mof-qualifiers.md) (1)
</dt> </dl>

Number that identifies the physical disk.

</dd> <dt>

**HighResResponseTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](event-tracing-mof-qualifiers.md) (3)
</dt> </dl>

CPU tick count from the beginning of the operation to the end of the operation.

</dd> <dt>

**Irp**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](event-tracing-mof-qualifiers.md) (4), [**Pointer**](event-tracing-mof-qualifiers.md)
</dt> </dl>

I/O request packet. This property identifies the I/O activity.

</dd> <dt>

**IrpFlags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](event-tracing-mof-qualifiers.md) (2), [**Format**](event-tracing-mof-qualifiers.md) ("x")
</dt> </dl>

Can contain one or more of the following I/O request packet flags (defined in Ntddk.h, which is a DDK header file):

<dl><span id="__IRP_NOCACHE"></span><span id="__irp_nocache"></span><dt>

 **IRP\_NOCACHE**
</dt><span id="__IRP_PAGING_IO"></span><span id="__irp_paging_io"></span><dt>

 **IRP\_PAGING\_IO**
</dt><span id="__IRP_MOUNT_COMPLETION"></span><span id="__irp_mount_completion"></span><dt>

 **IRP\_MOUNT\_COMPLETION**
</dt><span id="__IRP_SYNCHRONOUS_API"></span><span id="__irp_synchronous_api"></span><dt>

 **IRP\_SYNCHRONOUS\_API**
</dt><span id="__IRP_ASSOCIATED_IRP"></span><span id="__irp_associated_irp"></span><dt>

 **IRP\_ASSOCIATED\_IRP**
</dt><span id="__IRP_BUFFERED_IO"></span><span id="__irp_buffered_io"></span><dt>

 **IRP\_BUFFERED\_IO**
</dt><span id="IRP_DEALLOCATE_BUFFER"></span><span id="irp_deallocate_buffer"></span><dt>

**IRP\_DEALLOCATE\_BUFFER**
</dt><span id="__IRP_INPUT_OPERATION"></span><span id="__irp_input_operation"></span><dt>

 **IRP\_INPUT\_OPERATION**
</dt><span id="__IRP_SYNCHRONOUS_PAGING_IO"></span><span id="__irp_synchronous_paging_io"></span><dt>

 **IRP\_SYNCHRONOUS\_PAGING\_IO**
</dt><span id="__IRP_CREATE_OPERATION"></span><span id="__irp_create_operation"></span><dt>

 **IRP\_CREATE\_OPERATION**
</dt><span id="IRP_READ_OPERATION"></span><span id="irp_read_operation"></span><dt>

**IRP\_READ\_OPERATION**
</dt><span id="__IRP_WRITE_OPERATION"></span><span id="__irp_write_operation"></span><dt>

 **IRP\_WRITE\_OPERATION**
</dt><span id="__IRP_CLOSE_OPERATION"></span><span id="__irp_close_operation"></span><dt>

 **IRP\_CLOSE\_OPERATION**
</dt><span id="__IRP_DEFER_IO_COMPLETION"></span><span id="__irp_defer_io_completion"></span><dt>

 **IRP\_DEFER\_IO\_COMPLETION**
</dt> </dl>

</dd> <dt>

**IssuingThreadId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](event-tracing-mof-qualifiers.md) (5)
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

 

 




