---
title: MSFT\_VirtualDiskToPhysicalDisk class
description: Association between VirtualDisk and PhysicalDisk.A virtual disk and a physical disk are associated when the virtual disk has data residing on the physical disk.
ms.assetid: F2B91FCD-81BF-44D8-B6D1-CDECC765726F
keywords:
- MSFT_VirtualDiskToPhysicalDisk class Windows Storage Management API
- MSFT_VirtualDiskToPhysicalDisk class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_VirtualDiskToPhysicalDisk
- MSFT_VirtualDiskToPhysicalDisk.VirtualDisk
- MSFT_VirtualDiskToPhysicalDisk.PhysicalDisk
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

# MSFT\_VirtualDiskToPhysicalDisk class

Association between [**VirtualDisk**](msft-virtualdisk.md) and [**PhysicalDisk**](msft-physicaldisk.md).

A virtual disk and a physical disk are associated when the virtual disk has data residing on the physical disk.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_VirtualDiskToPhysicalDisk
{
  MSFT_VirtualDisk  REF VirtualDisk;
  MSFT_PhysicalDisk REF PhysicalDisk;
};
```

## Members

The **MSFT\_VirtualDiskToPhysicalDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_VirtualDiskToPhysicalDisk** class has these properties.

<dl> <dt>

**PhysicalDisk**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)**
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
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
</dt> <dt>

[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)
</dt> </dl>

 

 





