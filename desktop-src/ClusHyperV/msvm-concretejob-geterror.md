---
title: GetError method of the Msvm\_ConcreteJob class
description: Retrieves an error for a failed job.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bd4a4722-e55d-46c1-a0b7-fe9d6fa77412'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetError method", "GetError method, Msvm_ConcreteJob class", "Msvm_ConcreteJob class, GetError method"]
topic_type:
- apiref
api_name:
- Msvm_ConcreteJob.GetError
api_location:
- VMMS.exe
api_type:
- COM
---

# GetError method of the Msvm\_ConcreteJob class

Retrieves an error for a failed job.

## Syntax


```mof
uint32 GetError(
  [out] string Error
);
```



## Parameters

<dl> <dt>

*Error* \[out\]
</dt> <dd>

Returns a [**CIM\_Error**](cim-error.md) instance in CIM-XML format if the operational status of the job is not "2" (ok). Otherwise, if the job is 2 (OK), **NULL** is returned.

</dd> </dl>

## Return value

The possible return values are:

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
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_ConcreteJob**](msvm-concretejob.md)
</dt> </dl>

 

 





