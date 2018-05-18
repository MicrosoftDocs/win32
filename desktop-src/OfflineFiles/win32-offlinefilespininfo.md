---
Description: 'Represents the pinned status of an item in the Offline Files cache.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '364cc71f-3b85-4c11-b19b-3e6f06757a9e'
ms.prod: 'windows-server-dev'
ms.technology: 'offline-files'
ms.tgt_platform: multiple
title: 'Win32\_OfflineFilesPinInfo class'
---

# Win32\_OfflineFilesPinInfo class

Represents the pinned status of an item in the Offline Files cache. When an item is pinned in the Offline Files cache, it is protected from automatic eviction and is guaranteed to be available offline.

An instance of this class is obtained through the **PinInfo** property of the [**Win32\_OfflineFilesItem**](win32-offlinefilesitem.md) object.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[dynamic, provider("Win32_OfflineFilesProvider"), AMENDMENT]
class Win32_OfflineFilesPinInfo
{
  boolean Pinned;
  uint32  PinnedForUser;
  uint32  PinnedForUserByPolicy;
  uint32  PinnedForComputer;
  uint32  PinnedForFolderRedirection;
};
```

## Members

The **Win32\_OfflineFilesPinInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_OfflineFilesPinInfo** class has these properties.

<dl> <dt>

**Pinned**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if the item is pinned for any reason, or **FALSE** otherwise.

</dd> <dt>

**PinnedForComputer**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the file is pinned for all users on the computer by Group Policy and, if it is pinned, whether its pinned state is inherited by new child items.

<dt>

<span id="Not_pinned"></span><span id="not_pinned"></span><span id="NOT_PINNED"></span>

**Not pinned** (0)


</dt> <dd></dd> <dt>

<span id="Pinned"></span><span id="pinned"></span><span id="PINNED"></span>

**Pinned** (1)


</dt> <dd></dd> <dt>

<span id="Pinned_inherit"></span><span id="pinned_inherit"></span><span id="PINNED_INHERIT"></span>

**Pinned inherit** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**PinnedForFolderRedirection**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the file is pinned for users on the computer by Folder Redirection and, if it is pinned, whether its pinned state is inherited by new child items.

<dt>

<span id="Not_pinned"></span><span id="not_pinned"></span><span id="NOT_PINNED"></span>

**Not pinned** (0)


</dt> <dd></dd> <dt>

<span id="Pinned"></span><span id="pinned"></span><span id="PINNED"></span>

**Pinned** (1)


</dt> <dd></dd> <dt>

<span id="Pinned_inherit"></span><span id="pinned_inherit"></span><span id="PINNED_INHERIT"></span>

**Pinned inherit** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**PinnedForUser**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the file is pinned by a user and, if it is pinned, whether its pinned state is inherited by new child items.

<dt>

<span id="Not_pinned"></span><span id="not_pinned"></span><span id="NOT_PINNED"></span>

**Not pinned** (0)


</dt> <dd></dd> <dt>

<span id="Pinned"></span><span id="pinned"></span><span id="PINNED"></span>

**Pinned** (1)


</dt> <dd></dd> <dt>

<span id="Pinned_inherit"></span><span id="pinned_inherit"></span><span id="PINNED_INHERIT"></span>

**Pinned inherit** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**PinnedForUserByPolicy**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the file is pinned for users by Group Policy and, if it is pinned, whether its pinned state is inherited by new child items.

<dt>

<span id="Not_pinned"></span><span id="not_pinned"></span><span id="NOT_PINNED"></span>

**Not pinned** (0)


</dt> <dd></dd> <dt>

<span id="Pinned"></span><span id="pinned"></span><span id="PINNED"></span>

**Pinned** (1)


</dt> <dd></dd> <dt>

<span id="Pinned_inherit"></span><span id="pinned_inherit"></span><span id="PINNED_INHERIT"></span>

**Pinned inherit** (2)


</dt> <dd></dd> </dl>

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

 

 




