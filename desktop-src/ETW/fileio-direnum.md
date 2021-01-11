---
description: This class is the event type class for the enumerate directory and directory notification events. The following syntax is simplified from MOF code.
ms.assetid: 08458385-6066-4523-a053-aceb5e5d6f10
title: FileIo_DirEnum class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FileIo_DirEnum
- FileIo_DirEnum.IrpPtr
- FileIo_DirEnum.TTID
- FileIo_DirEnum.FileObject
- FileIo_DirEnum.FileKey
- FileIo_DirEnum.Length
- FileIo_DirEnum.InfoClass
- FileIo_DirEnum.FileIndex
- FileIo_DirEnum.FileName
api_type: 
- NA
api_location: 
---

# FileIo\_DirEnum class

This class is the event type class for the enumerate directory and directory notification events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{72, 77}, EventTypeName{"DirEnum", "DirNotify"}]
class FileIo_DirEnum : FileIo
{
  uint32 IrpPtr;
  uint32 TTID;
  uint32 FileObject;
  uint32 FileKey;
  uint32 Length;
  uint32 InfoClass;
  uint32 FileIndex;
  string FileName;
};
```

## Members

The **FileIo\_DirEnum** class has these types of members:

-   [Properties](#properties)

### Properties

The **FileIo\_DirEnum** class has these properties.

<dl> <dt>

**FileIndex**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(7)
</dt> </dl>

File index from which to continue directory enumeration.

</dd> <dt>

**FileKey**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4), Pointer
</dt> </dl>

To determine the directory name, match the value of this property to the **FileObject** property of a [**FileIo\_Name**](fileio-name.md) event.

</dd> <dt>

**FileName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(8), StringTermination("NullTerminated"), Format("w")
</dt> </dl>

Pattern specified for directory enumeration.

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

Qualifiers: WmiDataId(6), Pointer
</dt> </dl>

Requested directory enumeration information class.

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

**Length**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(5)
</dt> </dl>

Size of the query buffer, in bytes.

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

Directory enumeration and directory notification events are recorded when a directory is enumerated or a directory change notification is sent to registered listeners, respectively.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**FileIo**](fileio.md)
</dt> </dl>

 

 




