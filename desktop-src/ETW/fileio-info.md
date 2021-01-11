---
description: This class is the event type class for file information event. The following syntax is simplified from MOF code.
ms.assetid: 41ae1f8a-a90f-43d0-a848-a2c095f046d4
title: FileIo_Info class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FileIo_Info
- FileIo_Info.IrpPtr
- FileIo_Info.TTID
- FileIo_Info.FileObject
- FileIo_Info.FileKey
- FileIo_Info.ExtraInfo
- FileIo_Info.InfoClass
api_type: 
- NA
api_location: 
---

# FileIo\_Info class

This class is the event type class for file information event.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{69, 70, 71, 74, 75}, EventTypeName{"SetInfo", "Delete", "Rename", "QueryInfo", "FSControl"}]
class FileIo_Info : FileIo
{
  uint32 IrpPtr;
  uint32 TTID;
  uint32 FileObject;
  uint32 FileKey;
  uint32 ExtraInfo;
  uint32 InfoClass;
};
```

## Members

The **FileIo\_Info** class has these types of members:

-   [Properties](#properties)

### Properties

The **FileIo\_Info** class has these properties.

<dl> <dt>

**ExtraInfo**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(5), Pointer
</dt> </dl>

For FileDispositionInformation requests, this field contains the requested disposition. For FileEndOfFileInformation and FileAllocationInformation requests, this field contains the specified file size.

</dd> <dt>

**FileKey**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4), Pointer
</dt> </dl>

To determine the file name, match the value of this property to the **FileObject** property of a [**FileIo\_Name**](fileio-name.md) event.

</dd> <dt>

**FileObject**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3), Pointer
</dt> </dl>

Identifier that can be used for correlating operations to the same opened file object instance between file create and close events.

</dd> <dt>

**InfoClass**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(6)
</dt> </dl>

Requested file information class.

</dd> <dt>

**IrpPtr**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Pointer
</dt> </dl>

IO request packet. This property identifies the IO activity.

</dd> <dt>

**TTID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2), Pointer
</dt> </dl>

Thread identifier of the thread that is performing the operation.

</dd> </dl>

## Remarks

Set information and query information events indicate that the file attributes were set or queried. A file system control (FSControl) event is recorded when a FSCTL command is issued.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**FileIo**](fileio.md)
</dt> </dl>

 

 




