---
Description: 'Represents the information associated with local changes made to an item while working offline.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '1bcd0341-bd8a-4e5c-8b2c-406ab93939ec'
ms.prod: 'windows-server-dev'
ms.technology: 'offline-files'
ms.tgt_platform: multiple
title: 'Win32\_OfflineFilesChangeInfo class'
---

# Win32\_OfflineFilesChangeInfo class

Represents the information associated with local changes made to an item while working offline. An instance of this class is obtained through the ChangeInfo property of the [**Win32\_OfflineFilesItem**](win32-offlinefilesitem.md) object.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[dynamic, provider("Win32_OfflineFilesProvider"), AMENDMENT]
class Win32_OfflineFilesChangeInfo
{
  boolean Dirty;
  boolean DeletedOffline;
  boolean CreatedOffline;
  boolean ModifiedData;
  boolean ModifiedAttributes;
  boolean ModifiedTime;
};
```

## Members

The **Win32\_OfflineFilesChangeInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_OfflineFilesChangeInfo** class has these properties.

<dl> <dt>

**CreatedOffline**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if the item was created in the Offline Files cache while working offline, or **FALSE** otherwise.

</dd> <dt>

**DeletedOffline**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if the item was deleted from the Offline Files cache while working offline, or **FALSE** otherwise.

</dd> <dt>

**Dirty**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TRUE if the item was modified while working offline, or **FALSE** otherwise. When an item is modified offline, it is marked as "dirty." Such items must be synchronized to clear this "dirty" property on the item. The Offline Files service automatically synchronizes items when an offline scope transitions to online. When the item is synchronized, this property is set to **FALSE**.

</dd> <dt>

**ModifiedAttributes**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if one or more of the item's attributes were modified in the Offline Files cache while working offline, or **FALSE** otherwise.

</dd> <dt>

**ModifiedData**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if the item was modified in the Offline Files cache while working offline, or **FALSE** otherwise.

</dd> <dt>

**ModifiedTime**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if one or more of the item's time values were modified in the Offline Files cache while working offline, or **FALSE** otherwise.

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

 

 




