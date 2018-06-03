---
Description: Determines whether an item is suspended or not and, if so, if it is a suspended root or not.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 61cb896c-b8dd-4514-a28b-02b59b3cfb3a
ms.prod: windows-server-dev
ms.technology: offline-files
ms.tgt_platform: multiple
title: Win32\_OfflineFilesSuspendInfo class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_OfflineFilesSuspendInfo class

Determines whether an item is suspended or not and, if so, if it is a suspended root or not. An instance of this class is obtained through the **SuspendInfo** property of the [**Win32\_OfflineFilesItem**](win32-offlinefilesitem.md) object.

Only share, directory, and file items can be suspended. Server items cannot be suspended.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[dynamic, provider("Win32_OfflineFilesProvider"), AMENDMENT]
class Win32_OfflineFilesSuspendInfo
{
  boolean Suspended;
  boolean SuspendedRoot;
};
```

## Members

The **Win32\_OfflineFilesSuspendInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_OfflineFilesSuspendInfo** class has these properties.

<dl> <dt>

**Suspended**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if the item is suspended, or **FALSE** otherwise.

</dd> <dt>

**SuspendedRoot**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if the item is a suspended root, or **FALSE** otherwise. If the item is not suspended, this value is always **FALSE**.

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

 

 




