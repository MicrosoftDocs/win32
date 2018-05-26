---
title: MSFT\_SMJobToStorageGroup class
description: Represents an association between a job and a storage group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7221e31a-ffd7-4743-b20a-e1e71caeb611
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMJobToStorageGroup class
- MSFT_SMJobToStorageGroup class, described
topic_type:
- apiref
api_name:
- MSFT_SMJobToStorageGroup
- MSFT_SMJobToStorageGroup.Job
- MSFT_SMJobToStorageGroup.AffectedStorageGroup
api_location:
- StorageService.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SMJobToStorageGroup class

Represents an association between a job and a storage group.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMJobToStorageGroup
{
  MSFT_SMJob          REF Job;
  MSFT_SMStorageGroup REF AffectedStorageGroup;
};
```

## Members

The **MSFT\_SMJobToStorageGroup** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMJobToStorageGroup** class has these properties.

<dl> <dt>

**AffectedStorageGroup**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMStorageGroup**](msft-smstoragegroup.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMStorageGroup**](msft-smstoragegroup.md) object that represents the storage group.

</dd> <dt>

**Job**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMJob**](msft-smjob.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMJob**](msft-smjob.md) object that represents the job.

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

 

 





