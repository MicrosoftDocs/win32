---
title: MSFT\_SMDiskDriveToPool class
description: Represents a relationship between a disk drive and a storage pool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d000491a-b636-42b2-9f5b-04d8acbe54e3
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMDiskDriveToPool class
- MSFT_SMDiskDriveToPool class, described
topic_type:
- apiref
api_name:
- MSFT_SMDiskDriveToPool
- MSFT_SMDiskDriveToPool.Parent
- MSFT_SMDiskDriveToPool.Child
api_location:
- StorageService.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SMDiskDriveToPool class

Represents a relationship between a disk drive and a storage pool.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMDiskDriveToPool
{
  MSFT_SMDiskDrive REF Parent;
  MSFT_SMPool      REF Child;
};
```

## Members

The **MSFT\_SMDiskDriveToPool** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMDiskDriveToPool** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMPool**](msft-smpool.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The [**MSFT\_SMPool**](msft-smpool.md) object that represents the storage pool in the relationship.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMDiskDrive**](msft-smdiskdrive.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The [**MSFT\_SMDiskDrive**](msft-smdiskdrive.md) object that represents the disk drive in the relationship.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





