---
title: MSFT\_StorageSubSystemToDisk class
description: Association between MSFT\_StorageSubSystem and MSFT\_Disk.
ms.assetid: '3028CC6E-0F50-4E50-AE91-0ACD063CE21C'
keywords: ["MSFT_StorageSubSystemToDisk class Windows Storage Management API", "MSFT_StorageSubSystemToDisk class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToDisk
- MSFT_StorageSubSystemToDisk.StorageSubSystem
- MSFT_StorageSubSystemToDisk.Disk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_StorageSubSystemToDisk class

Association between [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) and [**MSFT\_Disk**](msft-disk.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToDisk
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_Disk             REF Disk;
};
```

## Members

The **MSFT\_StorageSubSystemToDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToDisk** class has these properties.

<dl> <dt>

**Disk**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_Disk**](msft-disk.md)**
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
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Disk**](msft-disk.md)
</dt> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





