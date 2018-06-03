---
title: MSFT\_StorageSubSystemToReplicaPeer class
description: Association between an MSFT\_StorageSubSystem and MSFT\_ReplicaPeer.
ms.assetid: F0DA41D9-7EFE-4526-918A-183110D1E309
keywords:
- MSFT_StorageSubSystemToReplicaPeer class Windows Storage Management API
- MSFT_StorageSubSystemToReplicaPeer class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToReplicaPeer
- MSFT_StorageSubSystemToReplicaPeer.StorageSubSystem
- MSFT_StorageSubSystemToReplicaPeer.ReplicaPeer
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageSubSystemToReplicaPeer class

Association between an [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) and [**MSFT\_ReplicaPeer**](msft-replicapeer.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToReplicaPeer
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_ReplicaPeer      REF ReplicaPeer;
};
```

## Members

The **MSFT\_StorageSubSystemToReplicaPeer** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToReplicaPeer** class has these properties.

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

[**MSFT\_ReplicaPeer**](msft-replicapeer.md)
</dt> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





