---
title: MSFT\_StorageSubSystemToPhysicalDisk class
description: Association between StorageSubSystem and PhysicalDisk.
ms.assetid: a5340475-0b88-4f74-b721-bf32dc7ab398
keywords:
- MSFT_StorageSubSystemToPhysicalDisk class Windows Storage Management API
- MSFT_StorageSubSystemToPhysicalDisk class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToPhysicalDisk
- MSFT_StorageSubSystemToPhysicalDisk.StorageSubSystem
- MSFT_StorageSubSystemToPhysicalDisk.PhysicalDisk
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

# MSFT\_StorageSubSystemToPhysicalDisk class

Association between [**StorageSubSystem**](msft-storagesubsystem.md) and [**PhysicalDisk**](msft-physicaldisk.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToPhysicalDisk
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_PhysicalDisk     REF PhysicalDisk;
};
```

## Members

The **MSFT\_StorageSubSystemToPhysicalDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToPhysicalDisk** class has these properties.

<dl> <dt>

**PhysicalDisk**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_PhysicalDisk**
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

[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)
</dt> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





