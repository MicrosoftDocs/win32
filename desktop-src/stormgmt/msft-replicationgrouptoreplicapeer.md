---
title: MSFT\_ReplicationGroupToReplicaPeer class
description: Association between replicated groups (MSFT\_ReplicationGroup to MSFT\_ReplicaPeer).
ms.assetid: 57DC1776-987F-491E-A063-B17824E02496
keywords:
- MSFT_ReplicationGroupToReplicaPeer class Windows Storage Management API
- MSFT_ReplicationGroupToReplicaPeer class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_ReplicationGroupToReplicaPeer
- MSFT_ReplicationGroupToReplicaPeer.ReplicationGroup
- MSFT_ReplicationGroupToReplicaPeer.ReplicaPeer
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

# MSFT\_ReplicationGroupToReplicaPeer class

Association between replicated groups ([**MSFT\_ReplicationGroup**](msft-replicationgroup.md) to [**MSFT\_ReplicaPeer**](msft-replicapeer.md)).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_ReplicationGroupToReplicaPeer : MSFT_Synchronized
{
  MSFT_ReplicationGroup REF ReplicationGroup;
  MSFT_ReplicaPeer      REF ReplicaPeer;
};
```

## Members

The **MSFT\_ReplicationGroupToReplicaPeer** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_ReplicationGroupToReplicaPeer** class has these properties.

<dl> <dt>

**ReplicaPeer**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_ReplicaPeer**](msft-replicapeer.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**ReplicationGroup**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_ReplicationGroup**](msft-replicationgroup.md)**
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

[**MSFT\_Synchronized**](msft-synchronized.md)
</dt> <dt>

[**MSFT\_ReplicationGroup**](msft-replicationgroup.md)
</dt> <dt>

[**MSFT\_ReplicaPeer**](msft-replicapeer.md)
</dt> </dl>

 

 





