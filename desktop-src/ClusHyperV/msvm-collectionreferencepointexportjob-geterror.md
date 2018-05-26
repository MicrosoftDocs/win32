---
title: GetError method of the Msvm\_CollectionReferencePointExportJob class
description: Retrieves error information for the operational status of a concrete job. This method returns a CIM\_Error instance if job fails; otherwise it returns NULL.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f0ab4133-c39b-4bc0-bd5b-911512ceff3a
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetError method
- GetError method, Msvm_CollectionReferencePointExportJob class
- Msvm_CollectionReferencePointExportJob class, GetError method
topic_type:
- apiref
api_name:
- Msvm_CollectionReferencePointExportJob.GetError
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetError method of the Msvm\_CollectionReferencePointExportJob class

Retrieves error information for the operational status of a concrete job. This method returns a [**CIM\_Error**](cim-error.md) instance if job fails; otherwise it returns **NULL**.

## Syntax


```mof
uint32 GetError(
  [out] string Error
);
```



## Parameters

<dl> <dt>

*Error* \[out\]
</dt> <dd>

An embedded [**CIM\_Error**](cim-error.md) instance if the job fails; otherwise **NULL**.

</dd> </dl>

## Return value

This function returns one of the following values.

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

 

 





