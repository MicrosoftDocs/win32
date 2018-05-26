---
title: MSFT\_SMJobToStorageVolume class
description: Represents a relationship between a job and a storage volume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 194aa481-7fce-4484-935a-12b25a148e63
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMJobToStorageVolume class
- MSFT_SMJobToStorageVolume class, described
topic_type:
- apiref
api_name:
- MSFT_SMJobToStorageVolume
- MSFT_SMJobToStorageVolume.Job
- MSFT_SMJobToStorageVolume.AffectedStorageVolume
api_location:
- StorageService.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SMJobToStorageVolume class

Represents a relationship between a job and a storage volume.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMJobToStorageVolume
{
  MSFT_SMJob           REF Job;
  MSFT_SMStorageVolume REF AffectedStorageVolume;
};
```

## Members

The **MSFT\_SMJobToStorageVolume** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMJobToStorageVolume** class has these properties.

<dl> <dt>

**AffectedStorageVolume**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMStorageVolume**](msft-smstoragevolume.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMStorageVolume**](msft-smstoragevolume.md) object that represents the storage volume in the relationship.

</dd> <dt>

**Job**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMJob**](msft-smjob.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMJob**](msft-smjob.md) object that represents the job in the relationship.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





