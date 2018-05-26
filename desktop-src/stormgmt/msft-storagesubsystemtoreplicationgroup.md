---
title: MSFT\_StorageSubSystemToReplicationGroup class
description: Association between a MSFT\_StorageSubSystem and MSFT\_ReplicationGroup.
ms.assetid: FBADE666-2039-4C76-ACBC-E5804EFFF11C
keywords:
- MSFT_StorageSubSystemToReplicationGroup class Windows Storage Management API
- MSFT_StorageSubSystemToReplicationGroup class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToReplicationGroup
- MSFT_StorageSubSystemToReplicationGroup.StorageSubSystem
- MSFT_StorageSubSystemToReplicationGroup.ReplicationGroup
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_StorageSubSystemToReplicationGroup class

Association between a [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) and [**MSFT\_ReplicationGroup**](msft-replicationgroup.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToReplicationGroup
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_ReplicationGroup REF ReplicationGroup;
};
```

## Members

The **MSFT\_StorageSubSystemToReplicationGroup** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToReplicationGroup** class has these properties.

<dl> <dt>

**ReplicationGroup**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_ReplicationGroup**](msft-replicationgroup.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**StorageSubSystem**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ReplicationGroup**](msft-replicationgroup.md)
</dt> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





