---
title: MSFT\_VirtualDiskToReplicaPeer class
description: Association between replicated virtual disks (MSFT\_VirtualDisk to MSFT\_ReplicaPeer).
ms.assetid: 751166F2-07D4-4E69-AE8D-38EAFAF78DE3
keywords:
- MSFT_VirtualDiskToReplicaPeer class Windows Storage Management API
- MSFT_VirtualDiskToReplicaPeer class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_VirtualDiskToReplicaPeer
- MSFT_VirtualDiskToReplicaPeer.VirtualDisk
- MSFT_VirtualDiskToReplicaPeer.ReplicaPeer
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

# MSFT\_VirtualDiskToReplicaPeer class

Association between replicated virtual disks ([**MSFT\_VirtualDisk**](msft-virtualdisk.md) to [**MSFT\_ReplicaPeer**](msft-replicapeer.md))

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_VirtualDiskToReplicaPeer : MSFT_Synchronized
{
  MSFT_VirtualDisk REF VirtualDisk;
  MSFT_ReplicaPeer REF ReplicaPeer;
};
```

## Members

The **MSFT\_VirtualDiskToReplicaPeer** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_VirtualDiskToReplicaPeer** class has these properties.

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

**VirtualDisk**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_VirtualDisk**](msft-virtualdisk.md)**
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

[**MSFT\_ReplicaPeer**](msft-replicapeer.md)
</dt> <dt>

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
</dt> </dl>

 

 





