---
description: The FileIo\_V0\_Name class is an older version of the event type class for file I/O events. The following syntax is simplified from MOF code.
ms.assetid: dcbe37f2-6df0-41a5-b85f-dcd06cbd5901
title: FileIo_V0_Name class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FileIo_V0_Name
- FileIo_V0_Name.FileObject
- FileIo_V0_Name.FileName
api_type: 
- NA
api_location: 
---

# FileIo\_V0\_Name class

The **FileIo\_V0\_Name** class is an older version of the event type class for file I/O events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(0), EventTypeName("Name")]
class FileIo_V0_Name : FileIo_V0
{
  uint32 FileObject;
  string FileName;
};
```

## Members

The **FileIo\_V0\_Name** class has these types of members:

-   [Properties](#properties)

### Properties

The **FileIo\_V0\_Name** class has these properties.

<dl> <dt>

FileName
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2), StringTermination("NullTerminated"), Format("w")
</dt> </dl>

Full path to the file, not including the drive letter.

</dd> <dt>

FileObject
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Pointer
</dt> </dl>

Match the value of this pointer to the **FileObject** pointer value in a [**DiskIo\_TypeGroup1**](diskio-typegroup1.md) event to determine the type of I/O operation.

</dd> </dl>

## Remarks

**Windows Server 2003:** To retrieve the drive letter for the file name path, use the **FileObject** property value to map to the corresponding [**DiskIo\_TypeGroup1**](diskio-typegroup1.md) event. From the **DiskIo\_TypeGroup1** event, use the **DiskNumber** and **ByteOffset** property values to map to the corresponding [**SystemConfig\_LogDisk**](systemconfig-logdisk.md) event. The **DriveLetterString** property contains the drive letter.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[**FileIo\_V0**](fileio-v0.md)
</dt> </dl>

 

 




