---
title: MSFT\_PhysicalDiskToStorageReliabilityCounter class
description: Association between a MSFT\_PhysicalDisk object and the corresponding MSFT\_StorageReliabilityCounter object.
ms.assetid: 2900E210-F130-4DCF-B451-7EACFF04B759
keywords:
- MSFT_PhysicalDiskToStorageReliabilityCounter class Windows Storage Management API
- MSFT_PhysicalDiskToStorageReliabilityCounter class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_PhysicalDiskToStorageReliabilityCounter
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

# MSFT\_PhysicalDiskToStorageReliabilityCounter class

Association between a [**MSFT\_PhysicalDisk**](msft-physicaldisk.md) object and the corresponding [**MSFT\_StorageReliabilityCounter**](msft-storagereliabilitycounter.md) object.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_PhysicalDiskToStorageReliabilityCounter
{
  MSFT_PhysicalDisk              REF PhysicalDisk;
  MSFT_StorageReliabilityCounter REF StorageReliabilityCounter;
};
```

## Members

The **MSFT\_PhysicalDiskToStorageReliabilityCounter** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_PhysicalDiskToStorageReliabilityCounter** class has these properties.

<dl> <dt>

[**PhysicalDisk**](msft-physicaldisk.md)
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The physical disk object.

</dd> <dt>

[**StorageReliabilityCounter**](msft-storagereliabilitycounter.md)
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageReliabilityCounter**](msft-storagereliabilitycounter.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The storage reliability counter object.

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

[**MSFT\_StorageReliabilityCounter**](msft-storagereliabilitycounter.md)
</dt> </dl>

 

 





