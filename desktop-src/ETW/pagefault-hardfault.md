---
description: This class is the event type class for hard page fault events. The following syntax is simplified from MOF code.
ms.assetid: 9837cc45-6485-46c3-a5d9-0d33e443cd32
title: PageFault_HardFault class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PageFault_HardFault
- PageFault_HardFault.InitialTime
- PageFault_HardFault.ReadOffset
- PageFault_HardFault.VirtualAddress
- PageFault_HardFault.FileObject
- PageFault_HardFault.TThreadId
- PageFault_HardFault.ByteCount
api_type: 
- NA
api_location: 
---

# PageFault\_HardFault class

This class is the event type class for hard page fault events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{32}, EventTypeName{"HardFault"}]
class PageFault_HardFault : PageFault_V2
{
  object InitialTime;
  uint64 ReadOffset;
  uint32 VirtualAddress;
  uint32 FileObject;
  uint32 TThreadId;
  uint32 ByteCount;
};
```

## Members

The **PageFault\_HardFault** class has these types of members:

-   [Properties](#properties)

### Properties

The **PageFault\_HardFault** class has these properties.

<dl> <dt>

**ByteCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(6)
</dt> </dl>

Amount of data read from ReadOffset to satisfy the fault.

</dd> <dt>

**FileObject**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4), Pointer
</dt> </dl>

Match the value of this pointer to the **FileObject** pointer value in a [**FileIo\_Name**](fileio-name.md) event to determine the name of the file.

</dd> <dt>

**InitialTime**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Extension("WmiTime")
</dt> </dl>

Start time stamp at which page fault occurred.

</dd> <dt>

**ReadOffset**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2), Format("x")
</dt> </dl>

File offset from which data was read to satisfy fault.

</dd> <dt>

**TThreadId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(5), Format("x")
</dt> </dl>

Thread identifier of the thread that encountered the page fault.

</dd> <dt>

**VirtualAddress**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3), Pointer
</dt> </dl>

Faulting address.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**PageFault\_V2**](pagefault-v2.md)
</dt> </dl>

 

 




