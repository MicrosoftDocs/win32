---
title: Resynchronize method of the Msvm\_CollectionReplicationService class
description: This method performs Resynchronize operation on the given Virtual System Collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: daabd014-c15d-4cfb-ad27-03df9a309e88
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Resynchronize method
- Resynchronize method, Msvm_CollectionReplicationService class
- Msvm_CollectionReplicationService class, Resynchronize method
topic_type:
- apiref
api_name:
- Msvm_CollectionReplicationService.Resynchronize
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resynchronize method of the Msvm\_CollectionReplicationService class

This method performs Resynchronize operation on the given Virtual System Collection.

## Syntax


```mof
uint32 Resynchronize(
  [in]  CIM_CollectionOfMSEs REF Collection,
  [in]  datetime                 StartTime,
  [in]  boolean                  IncludeSuspended,
  [out] CIM_ConcreteJob      REF Job
);
```



## Parameters

<dl> <dt>

*Collection* \[in\]
</dt> <dd>

A reference to the [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) instance for which Resynchronize needs to be performed.

</dd> <dt>

*StartTime* \[in\]
</dt> <dd>

Scheduled start time for Resynchronize operation over the network connection to recovery server.

When StartTime is not specified Resynchronize operation starts immediately.

</dd> <dt>

*IncludeSuspended* \[in\]
</dt> <dd>

Indicates whether replication suspended vms should also be considered for Resynchronize operation or not.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A [**CIM\_ConcreteJob**](cim-concretejob.md)reference to the job (can be null if the task is completed).

</dd> </dl>

## Return value

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
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

**System is in use** (32774)
</dt> <dt>

**Invalid state for this operation** (32775)
</dt> <dt>

**Incorrect data type** (32776)
</dt> <dt>

**System is not available** (32777)
</dt> <dt>

**Out of memory** (32778)
</dt> <dt>

**File not found** (32779)
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

[**Msvm\_CollectionReplicationService**](msvm-collectionreplicationservice.md)
</dt> </dl>

 

 





