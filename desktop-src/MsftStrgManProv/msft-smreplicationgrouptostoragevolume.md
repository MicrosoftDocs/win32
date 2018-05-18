---
title: MSFT\_SMReplicationGroupToStorageVolume class
description: Represents an association between a replication group and a storage volume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '41309c10-8787-4e6f-9fce-0ea00f8624e1'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMReplicationGroupToStorageVolume class", "MSFT_SMReplicationGroupToStorageVolume class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMReplicationGroupToStorageVolume
- MSFT_SMReplicationGroupToStorageVolume.Parent
- MSFT_SMReplicationGroupToStorageVolume.Child
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMReplicationGroupToStorageVolume class

Represents an association between a replication group and a storage volume.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("WMIStorage"), AMENDMENT]
class MSFT_SMReplicationGroupToStorageVolume
{
  MSFT_SMReplicationGroup REF Parent;
  MSFT_SMStorageVolume    REF Child;
};
```

## Members

The **MSFT\_SMReplicationGroupToStorageVolume** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMReplicationGroupToStorageVolume** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_SMStorageVolume**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The [**MSFT\_SMReplicaPeer**](msft-smreplicapeer.md) object that represents the replication group.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_SMReplicationGroup**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The [**MSFT\_SMReplicationGroup**](msft-smreplicationgroup.md) object that represents the replication group.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





