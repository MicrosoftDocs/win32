---
Description: 'Represents a single item in the Offline Files cache.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '16b3564d-8e23-41f5-9d41-b73bf5dc4f28'
ms.prod: 'windows-server-dev'
ms.technology: 'offline-files'
ms.tgt_platform: multiple
title: 'Win32\_OfflineFilesItem class'
---

# Win32\_OfflineFilesItem class

Represents a single item in the Offline Files cache. The item may be a server, share, directory or file.

## Syntax

``` syntax
[dynamic, provider("Win32_OfflineFilesProvider"), AMENDMENT]
class Win32_OfflineFilesItem
{
  string                           ItemPath;
  string                           ParentItemPath;
  string                           ItemName;
  uint32                           ItemType;
  Win32_OfflineFilesFileSysInfo    FileSysInfo;
  Win32_OfflineFilesPinInfo        PinInfo;
  Win32_OfflineFilesChangeInfo     ChangeInfo;
  Win32_OfflineFilesConnectionInfo ConnectionInfo;
  Win32_OfflineFilesSuspendInfo    SuspendInfo;
  boolean                          Encrypted;
  boolean                          Sparse;
  Win32_OfflineFilesDirtyInfo      DirtyInfo;
};
```

## Members

The **Win32\_OfflineFilesItem** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_OfflineFilesItem** class has these properties.

<dl> <dt>

**ChangeInfo**
</dt> <dd> <dl> <dt>

Data type: **Win32\_OfflineFilesChangeInfo**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_OfflineFilesChangeInfo**](win32-offlinefileschangeinfo.md) object that contains the change information for the item. Applicable to share, directory, and file items.

</dd> <dt>

**ConnectionInfo**
</dt> <dd> <dl> <dt>

Data type: **Win32\_OfflineFilesConnectionInfo**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_OfflineFilesConnectionInfo**](win32-offlinefilesconnectioninfo.md) object that contains the connection information for the item. Applicable to share, directory, and file items.

</dd> <dt>

**DirtyInfo**
</dt> <dd> <dl> <dt>

Data type: **Win32\_OfflineFilesDirtyInfo**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Dirty byte count information for item. Applicable to File items.

</dd> <dt>

**Encrypted**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if the item is encrypted in the Offline Files cache, or **FALSE** otherwise. This property is applicable only to file items. Server, share, and directory items will always report a value of **FALSE** for this property. Inspect the **ItemType** property to determine the type of an item.

</dd> <dt>

**FileSysInfo**
</dt> <dd> <dl> <dt>

Data type: **Win32\_OfflineFilesFileSysInfo**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_OfflineFilesFileSysInfo**](win32-offlinefilesfilesysinfo.md) object that contains the file system information for the item. Applicable to directory and file items.

</dd> <dt>

**ItemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Not\_null**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

The file system name of the item, not including the directory path. For example, the UNC path "\\\\server\\share\\directory\\file.ext" contains the following elements:



| Item Type | Example     |
|-----------|-------------|
| File      | "file.ext"  |
| Directory | "directory" |
| Share     | "share"     |
| Server    | "server"    |



 

</dd> <dt>

**ItemPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**Not\_null**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

A string that contains the UNC path of the item on the server.



| Item Type | Example                                               |
|-----------|-------------------------------------------------------|
| File      | "\\\\server\\share\\directory1\\directory2\\file.ext" |
| Directory | "\\\\server\\share\\directory1\\directory2"           |
| Share     | "\\\\server\\share"                                   |
| Server    | "\\\\server"                                          |



 

</dd> <dt>

**ItemType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of the item: file, directory, share, or server.

<dt>

<span id="File"></span><span id="file"></span><span id="FILE"></span>

**File** (0)


</dt> <dd></dd> <dt>

<span id="Directory"></span><span id="directory"></span><span id="DIRECTORY"></span>

**Directory** (1)


</dt> <dd></dd> <dt>

<span id="Share"></span><span id="share"></span><span id="SHARE"></span>

**Share** (2)


</dt> <dd></dd> <dt>

<span id="Server"></span><span id="server"></span><span id="SERVER"></span>

**Server** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**ParentItemPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that contains the UNC path of the parent item on the server. The string is empty if the item is a server item.



| Item Type | Parent Item Type | Example                                     |
|-----------|------------------|---------------------------------------------|
| File      | Directory        | "\\\\server\\share\\directory1\\directory2" |
| Directory | Share            | "\\\\server\\share"                         |
| Share     | Server           | "\\\\server"                                |
| Server    | none             | ""                                          |



 

</dd> <dt>

**PinInfo**
</dt> <dd> <dl> <dt>

Data type: **Win32\_OfflineFilesPinInfo**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_OfflineFilesPinInfo**](win32-offlinefilespininfo.md) object that contains pinned status information for the item. Applicable to share, directory, and file items.

</dd> <dt>

**Sparse**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if the item is sparsely cached, or **FALSE** otherwise. A sparsely-cached item exists in the Offline Files cache but not all of its contents are cached. Such items are not available offline. This property is applicable only to File items. Server, Share, and Directory items will always report a value of **False** for this property. The **ItemType** property contains the type of the item.

</dd> <dt>

**SuspendInfo**
</dt> <dd> <dl> <dt>

Data type: **Win32\_OfflineFilesSuspendInfo**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_OfflineFilesSuspendInfo**](win32-offlinefilessuspendinfo.md) object that contains the suspend state information for the item. Applicable to share, directory, and file items.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                 |
| MOF<br/>                      | <dl> <dt>OfflineFilesWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CscObj.dll</dt> </dl>                  |



## See also

<dl> <dt>

[Offline Files WMI Provider Reference](offline-files-wmi-provider-reference.md)
</dt> </dl>

 

 




