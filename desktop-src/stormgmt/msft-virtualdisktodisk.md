---
title: MSFT\_VirtualDiskToDisk class
description: Association between VirtualDisk and Disk.
ms.assetid: 661e8d56-ac91-4b94-a951-8577b7a26d2e
keywords:
- MSFT_VirtualDiskToDisk class Windows Storage Management API
- MSFT_VirtualDiskToDisk class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_VirtualDiskToDisk
- MSFT_VirtualDiskToDisk.VirtualDisk
- MSFT_VirtualDiskToDisk.Disk
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

# MSFT\_VirtualDiskToDisk class

Association between [**VirtualDisk**](msft-virtualdisk.md) and [**Disk**](msft-disk.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_VirtualDiskToDisk
{
  MSFT_VirtualDisk REF VirtualDisk;
  MSFT_Disk        REF Disk;
};
```

## Members

The **MSFT\_VirtualDiskToDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_VirtualDiskToDisk** class has these properties.

<dl> <dt>

**Disk**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_Disk**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**VirtualDisk**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_VirtualDisk**
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

[**MSFT\_Disk**](msft-disk.md)
</dt> <dt>

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
</dt> </dl>

 

 





