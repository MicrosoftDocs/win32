---
title: MSFT\_SMStorageGroup class
description: Represents a storage group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e1b1002d-3e75-4cd0-b406-46ce9eaf79d3'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMStorageGroup class", "MSFT_SMStorageGroup class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMStorageGroup
- MSFT_SMStorageGroup.ObjectId
- MSFT_SMStorageGroup.Identifier
- MSFT_SMStorageGroup.Name
- MSFT_SMStorageGroup.DisplayName
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMStorageGroup class

Represents a storage group.

**Windows Server 2012 R2 and Windows Server 2012:** This class does not inherit from [**MSFT\_SMStorageObject**](msft-smstorageobject.md) before Windows Server 2016.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("WMIStorage"), AMENDMENT]
class MSFT_SMStorageGroup : MSFT_SMStorageObject
{
  String ObjectId;
  String Identifier;
  String Name;
  String DisplayName;
};
```

## Members

The **MSFT\_SMStorageGroup** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SMStorageGroup** class has these methods.



| Method                                                                   | Description                                                            |
|:-------------------------------------------------------------------------|:-----------------------------------------------------------------------|
| [**AddInitiator**](addinitiator-msft-smstoragegroup.md)                 | Adds an initiator ID to a storage group.<br/>                    |
| [**AddInitiators**](addinitiators-msft-smstoragegroup.md)               | Adds initiator IDs to a storage group.<br/>                      |
| [**AddStorageVolumes**](addstoragevolumes-msft-smstoragegroup.md)       | Adds storage volumes to a storage group.<br/>                    |
| [**AddTargetPorts**](addtargetports-msft-smstoragegroup.md)             | Adds target ports to a storage group.<br/>                       |
| [**Delete**](delete-msft-smstoragegroup.md)                             | Deletes a storage group.<br/>                                    |
| [**RemoveInitiators**](removeinitiators-msft-smstoragegroup.md)         | Removes the specified initiators from the storage group.<br/>    |
| [**RemoveStorageVolumes**](removestoragevolumes-msft-smstoragegroup.md) | Removes the specified logical units from the storage group.<br/> |
| [**RemoveTargetPorts**](removetargetports-msft-smstoragegroup.md)       | Removes the specified target ports from the storage group.<br/>  |
| [**Rename**](rename-msft-smstoragegroup.md)                             | Renames a storage group.<br/>                                    |



 

### Properties

The **MSFT\_SMStorageGroup** class has these properties.

<dl> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user-friendly name of the storage group.

</dd> <dt>

**Identifier**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The ID of the logical instance of the object. This ID must be unique within the scope of the storage system.

This property is inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The system defined name of the storage group.

</dd> <dt>

**ObjectId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The ID of this class instance. This ID must be unique within the scope of the Windows Storage Management server that hosts the provider object.

This property is inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md).

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMStorageObject**](msft-smstorageobject.md)
</dt> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





