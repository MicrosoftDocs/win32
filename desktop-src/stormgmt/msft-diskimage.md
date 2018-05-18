---
title: MSFT\_DiskImage class
description: Represents a disk image.
ms.assetid: 'A895A5DB-39C7-4633-9C8C-3DA8AE8BD81A'
keywords: ["MSFT_DiskImage class Windows Storage Management API", "MSFT_DiskImage class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_DiskImage
- MSFT_DiskImage.ImagePath
- MSFT_DiskImage.StorageType
- MSFT_DiskImage.DevicePath
- MSFT_DiskImage.FileSize
- MSFT_DiskImage.Size
- MSFT_DiskImage.LogicalSectorSize
- MSFT_DiskImage.BlockSize
- MSFT_DiskImage.Attached
- MSFT_DiskImage.Number
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_DiskImage class

Represents a disk image.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_DiskImage
{
  String  ImagePath;
  UInt32  StorageType;
  String  DevicePath;
  UInt64  FileSize;
  UInt64  Size;
  UInt64  LogicalSectorSize;
  UInt64  BlockSize;
  Boolean Attached;
  UInt32  Number;
};
```

## Members

The **MSFT\_DiskImage** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DiskImage** class has these methods.



| Method                                      | Description                          |
|:--------------------------------------------|:-------------------------------------|
| [**Dismount**](msft-diskimage-dismount.md) | Dismounts the disk image.<br/> |
| [**Mount**](msft-diskimage-mount.md)       | Mounts the disk image.<br/>    |



 

### Properties

The **MSFT\_DiskImage** class has these properties.

<dl> <dt>

**Attached**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if the disk image is attached.

</dd> <dt>

**BlockSize**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Units** (Bytes)
</dt> </dl>

Block size of the disk image, in bytes.

</dd> <dt>

**DevicePath**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The device path for the disk image.

</dd> <dt>

**FileSize**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Units** (Bytes)
</dt> </dl>

The file size, in bytes, of the disk image.

</dd> <dt>

**ImagePath**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The path to the disk image.

</dd> <dt>

**LogicalSectorSize**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Units** (Bytes)
</dt> </dl>

Logical sector size of the disk image, in bytes.

</dd> <dt>

**Number**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The disk number of the disk image.

</dd> <dt>

**Size**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Units** (Bytes)
</dt> </dl>

The size, in bytes, of the disk image.

</dd> <dt>

**StorageType**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Values** ( "Unknown", "ISO", "VHD", "VHDX" ), **ValueMap** ("0", "1", "2", "3")
</dt> </dl>

The type of the disk image.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



 

 





