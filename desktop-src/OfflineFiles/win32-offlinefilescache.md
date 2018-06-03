---
Description: Represents the Offline Files cache.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0b894883-14a0-444d-9109-550a4e02eae8
ms.prod: windows-server-dev
ms.technology: offline-files
ms.tgt_platform: multiple
title: Win32\_OfflineFilesCache class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_OfflineFilesCache class

Represents the Offline Files cache. Each computer contains only one Offline Files cache. Thus, each computer creates only one instance of this [*singleton class*](https://msdn.microsoft.com/library/aa390836#wmi-gloss-singleton-class).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Singleton, dynamic, provider("Win32_OfflineFilesProvider"), AMENDMENT]
class Win32_OfflineFilesCache
{
  boolean Enabled;
  boolean Active;
  string  Location;
};
```

## Members

The **Win32\_OfflineFilesCache** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_OfflineFilesCache** class has these methods.



| Method                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                               |
|:-----------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DeleteItems**](win32-offlinefilescache-deleteitems.md)             | Deletes one or more items from the Offline Files cache.<br/>                                                                                                                                                                                                                                                                                                                        |
| [**Enable**](win32-offlinefilescache-enable.md)                       | Enables or disables the Offline Files feature.<br/>                                                                                                                                                                                                                                                                                                                                 |
| [**Encrypt**](win32-offlinefilescache-encrypt.md)                     | Encrypts or unencrypts files in the Offline Files cache.<br/>                                                                                                                                                                                                                                                                                                                       |
| [**Pin**](win32-offlinefilescache-pin.md)                             | Assures that an item will be available offline.<br/>                                                                                                                                                                                                                                                                                                                                |
| [**RenameItem**](win32-offlinefilescache-renameitem.md)               | Renames an item in the Offline Files cache.<br/>                                                                                                                                                                                                                                                                                                                                    |
| [**RenameItemEx**](win32-offlinefilescache-renameitem.md)             | Renames an item in the Offline Files cache. This method is identical to the [**RenameItem**](win32-offlinefilescache-renameitem.md) method, except that it will attempt to do the rename operation right away.<br/> **Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This method is not supported until Windows 8 and Windows Server 2012.<br/> |
| [**SuspendRoot**](win32-offlinefilescache-suspendroot.md)             | Suspends or un-suspends a directory tree in the Offline Files cache.<br/>                                                                                                                                                                                                                                                                                                           |
| [**Synchronize**](win32-offlinefilescache-synchronize.md)             | Synchronizes one or more items.<br/>                                                                                                                                                                                                                                                                                                                                                |
| [**TransitionOffline**](win32-offlinefilescache-transitionoffline.md) | Transitions an item offline if possible.<br/>                                                                                                                                                                                                                                                                                                                                       |
| [**TransitionOnline**](win32-offlinefilescache-transitiononline.md)   | Transitions an item online if possible.<br/>                                                                                                                                                                                                                                                                                                                                        |
| [**Unpin**](win32-offlinefilescache-unpin.md)                         | Removes the assurance that an item will be available offline.<br/>                                                                                                                                                                                                                                                                                                                  |



 

### Properties

The **Win32\_OfflineFilesCache** class has these properties.

<dl> <dt>

**Active**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the running state of the Offline Files feature. If this property is **TRUE**, the Offline Files feature is running, caching is active, and cached files will be available offline. If this property is **FALSE**, the Offline Files feature is not running, Offline Files will not cache files, and any cached files will not be available offline. Note that a system restart may be necessary before the configured state takes effect. To determine the configuration state of the feature, query the Enabled property.

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the configuration state of the Offline Files feature. If this property is **TRUE**, the Offline Files feature has been enabled and is configured to run. If this property is **FALSE**, the Offline Files feature has been disabled and is not configured to run. Note that a system restart may be necessary before the configured state takes effect. To determine the actual state of the feature, query the Active property.

</dd> <dt>

**Location**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path of the directory on the local computer where the Offline Files cache is located.

</dd> </dl>

## Remarks

The role of this object is to control the configuration of the Offline Files feature as well as manipulate the individual items that are stored within the cache. Items in the cache represent servers, shares, directories, and files that are associated with the UNC paths of remote files that are cached.

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

 

 




