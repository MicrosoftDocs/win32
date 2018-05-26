---
title: MSFT\_SMJobToPool class
description: Represents an association between a job and a storage pool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b4764fae-03bc-45c8-bfb5-e92baf250a88
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMJobToPool class
- MSFT_SMJobToPool class, described
topic_type:
- apiref
api_name:
- MSFT_SMJobToPool
- MSFT_SMJobToPool.Job
- MSFT_SMJobToPool.AffectedPool
api_location:
- StorageService.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SMJobToPool class

Represents an association between a job and a storage pool.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMJobToPool
{
  MSFT_SMJob  REF Job;
  MSFT_SMPool REF AffectedPool;
};
```

## Members

The **MSFT\_SMJobToPool** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMJobToPool** class has these properties.

<dl> <dt>

**AffectedPool**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMPool**](msft-smpool.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMPool**](msft-smpool.md) object that represents the pool.

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

 

 





