---
title: MSFT\_StorageSubSystemToStorageNode class
description: Association between a storage subsystem and a storage node.
ms.assetid: E8D27895-90A7-4A61-A1AE-79F82AF9C53E
keywords:
- MSFT_StorageSubSystemToStorageNode class Windows Storage Management API
- MSFT_StorageSubSystemToStorageNode class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToStorageNode
- MSFT_StorageSubSystemToStorageNode.StorageSubSystem
- MSFT_StorageSubSystemToStorageNode.StorageNode
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

# MSFT\_StorageSubSystemToStorageNode class

Association between a storage subsystem and a storage node.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToStorageNode
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_StorageNode      REF StorageNode;
};
```

## Members

The **MSFT\_StorageSubSystemToStorageNode** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToStorageNode** class has these properties.

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
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



 

 





