---
Description: Represents the common file system metadata about a file or directory in the Offline Files cache.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: beaa2bb0-b7f7-4344-85fd-2fa993cec602
ms.prod: windows-server-dev
ms.technology: offline-files
ms.tgt_platform: multiple
title: Win32\_OfflineFilesFileSysInfo class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_OfflineFilesFileSysInfo class

Represents the common file system metadata about a file or directory in the Offline Files cache. Examples are attributes, size, and time values.

The original copy of the item represents the state of the item following the last successful sync of that item, which is the most recent time when the remote copy and local copy were identical.

An instance of this class is obtained through the **FileSysInfo** property of the [**Win32\_OfflineFilesItem**](win32-offlinefilesitem.md) object.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[dynamic, provider("Win32_OfflineFilesProvider"), AMENDMENT]
class Win32_OfflineFilesFileSysInfo
{
  uint32   LocalAttributes;
  sint64   LocalSize;
  DATETIME LocalCreationTime;
  DATETIME LocalLastWriteTime;
  DATETIME LocalChangeTime;
  DATETIME LocalLastAccessTime;
  uint32   OriginalAttributes;
  sint64   OriginalSize;
  DATETIME OriginalCreationTime;
  DATETIME OriginalLastWriteTime;
  DATETIME OriginalChangeTime;
  DATETIME OriginalLastAccessTime;
  uint32   RemoteAttributes;
  sint64   RemoteSize;
  DATETIME RemoteCreationTime;
  DATETIME RemoteLastWriteTime;
  DATETIME RemoteChangeTime;
  DATETIME RemoteLastAccessTime;
};
```

## Members

The **Win32\_OfflineFilesFileSysInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_OfflineFilesFileSysInfo** class has these properties.

<dl> <dt>

**LocalAttributes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The file attribute mask for the local copy of the item. One or more of FILE\_ATTRIBUTE\_XXXXXX as defined in the Windows SDK. For more information, see the [**GetFileAttributes**](https://msdn.microsoft.com/library/windows/desktop/aa364944) function.

</dd> <dt>

**LocalChangeTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [DATETIME](https://msdn.microsoft.com/library/aa389799) value that represents the last-change time, in UTC, of the local copy of the item. This is the time the item's data or attributes were last changed.

</dd> <dt>

**LocalCreationTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [DATETIME](https://msdn.microsoft.com/library/aa389799) value that represents the creation time of the local copy of the item, expressed in Universal Time Coordinates (UTC).

</dd> <dt>

**LocalLastAccessTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [DATETIME](https://msdn.microsoft.com/library/aa389799) value that represents the last-access time, in UTC, of the local copy of the item. This is the time the item was last read from or written to.

</dd> <dt>

**LocalLastWriteTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [DATETIME](https://msdn.microsoft.com/library/aa389799) value that represents the last-write time, in UTC, of the local copy of the item. This is the time the item's data was last written to.

</dd> <dt>

**LocalSize**
</dt> <dd> <dl> <dt>

Data type: **sint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A 64-bit signed integer value that contains the size, in bytes, of the local copy of the item.

</dd> <dt>

**OriginalAttributes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The file attribute mask for the original copy of the item. One or more of FILE\_ATTRIBUTE\_XXXXXX as defined in the Windows SDK. For more information, see the [**GetFileAttributes**](https://msdn.microsoft.com/library/windows/desktop/aa364944) function.

</dd> <dt>

**OriginalChangeTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [DATETIME](https://msdn.microsoft.com/library/aa389799) value that represents the last-change time, in UTC, of the original copy of the item. This is the time the item's data or attributes were last changed.

</dd> <dt>

**OriginalCreationTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [DATETIME](https://msdn.microsoft.com/library/aa389799) value that represents the creation time, in UTC, of the original copy of the item.

</dd> <dt>

**OriginalLastAccessTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [DATETIME](https://msdn.microsoft.com/library/aa389799) value that represents the last-access time, in UTC, of the original copy of the item. This is the time the item was last read from or written to.

</dd> <dt>

**OriginalLastWriteTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [DATETIME](https://msdn.microsoft.com/library/aa389799) value that represents the last-write time, in UTC, of the original copy of the item. This is the time the item's data was last written to.

</dd> <dt>

**OriginalSize**
</dt> <dd> <dl> <dt>

Data type: **sint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A 64-bit signed integer value that contains the size, in bytes, of the original copy of the item.

</dd> <dt>

**RemoteAttributes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for future use.

</dd> <dt>

**RemoteChangeTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for future use.

</dd> <dt>

**RemoteCreationTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for future use.

</dd> <dt>

**RemoteLastAccessTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for future use.

</dd> <dt>

**RemoteLastWriteTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for future use.

</dd> <dt>

**RemoteSize**
</dt> <dd> <dl> <dt>

Data type: **sint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for future use.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                 |
| MOF<br/>                      | <dl> <dt>OfflineFilesWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CscObj.dll</dt> </dl>                  |



## See also

<dl> <dt>

[Offline Files WMI Provider Reference](offline-files-wmi-provider-reference.md)
</dt> </dl>

 

 




