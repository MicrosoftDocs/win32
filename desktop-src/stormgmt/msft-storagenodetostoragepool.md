---
title: MSFT\_StorageNodeToStoragePool class
description: Association between a storage node and a storage pool.
ms.assetid: 701C6089-46CB-4A26-B5A7-83316DFF49B5
keywords:
- MSFT_StorageNodeToStoragePool class Windows Storage Management API
- MSFT_StorageNodeToStoragePool class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageNodeToStoragePool
- MSFT_StorageNodeToStoragePool.StorageNode
- MSFT_StorageNodeToStoragePool.StoragePool
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

# MSFT\_StorageNodeToStoragePool class

Association between a storage node and a storage pool.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association]
class MSFT_StorageNodeToStoragePool
{
  MSFT_StorageNode REF StorageNode;
  MSFT_StoragePool REF StoragePool;
};
```

## Members

The **MSFT\_StorageNodeToStoragePool** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageNodeToStoragePool** class has these properties.

<dl> <dt>

**StorageNode**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageNode**](msft-storagenode.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**StoragePool**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StoragePool**](msft-storagepool.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



 

 





