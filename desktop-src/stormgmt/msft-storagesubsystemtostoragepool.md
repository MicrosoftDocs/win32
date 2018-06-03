---
title: MSFT\_StorageSubSystemToStoragePool class
description: Association between StorageSubSystem and StoragePool.
ms.assetid: 8fa2f262-3ffd-4bcb-b6a6-628e7d3fbe63
keywords:
- MSFT_StorageSubSystemToStoragePool class Windows Storage Management API
- MSFT_StorageSubSystemToStoragePool class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToStoragePool
- MSFT_StorageSubSystemToStoragePool.StorageSubSystem
- MSFT_StorageSubSystemToStoragePool.StoragePool
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

# MSFT\_StorageSubSystemToStoragePool class

Association between [**StorageSubSystem**](msft-storagesubsystem.md) and [**StoragePool**](msft-storagepool.md)

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToStoragePool
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_StoragePool      REF StoragePool;
};
```

## Members

The **MSFT\_StorageSubSystemToStoragePool** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToStoragePool** class has these properties.

<dl> <dt>

**StoragePool**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_StoragePool**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**StorageSubSystem**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_StorageSubSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StoragePool**](msft-storagepool.md)
</dt> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





