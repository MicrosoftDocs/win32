---
title: GetErrorEx method of the Msvm\_CollectionReferencePointExportJob class
description: When the job is executing or has terminated without error, then this method returns no Msvm\_Error instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 08d765fb-30c7-49fe-9715-2dd06589cca6
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetErrorEx method
- GetErrorEx method, Msvm_CollectionReferencePointExportJob class
- Msvm_CollectionReferencePointExportJob class, GetErrorEx method
topic_type:
- apiref
api_name:
- Msvm_CollectionReferencePointExportJob.GetErrorEx
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetErrorEx method of the Msvm\_CollectionReferencePointExportJob class

When the job is executing or has terminated without error, then this method returns no [**Msvm\_Error**](msvm-error.md) instance. However, if the job has failed because of some internal problem or because the job has been terminated by a client, then one or more **Msvm\_Error** instances are returned.

## Syntax


```mof
uint32 GetErrorEx(
  [out] string Errors[]
);
```



## Parameters

<dl> <dt>

*Errors* \[out\]
</dt> <dd>

An array of embedded [**Msvm\_Error**](msvm-error.md) instances if the job fails; otherwise **NULL**.

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Failed** (32768)
</dt> <dt>

**Access Denied** (32769)
</dt> <dt>

**Not Supported** (32770)
</dt> <dt>

**Status is unknown** (32771)
</dt> <dt>

**Timeout** (32772)
</dt> <dt>

**Invalid parameter** (32773)
</dt> <dt>

**System is in used** (32774)
</dt> <dt>

**Invalid state for this operation** (32775)
</dt> <dt>

**Incorrect data type** (32776)
</dt> <dt>

**System is not available** (32777)
</dt> <dt>

**Out of memory** (32778)
</dt> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_CollectionReferencePointExportJob**](msvm-collectionreferencepointexportjob.md)
</dt> </dl>

 

 





