---
title: InitiateFailover method of the Msvm\_CollectionReplicationService class
description: Sets the failover for collection to application or crash consistent image.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 00d6b32e-ee7f-4d5e-9cb3-828b4a5ab306
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- InitiateFailover method
- InitiateFailover method, Msvm_CollectionReplicationService class
- Msvm_CollectionReplicationService class, InitiateFailover method
topic_type:
- apiref
api_name:
- Msvm_CollectionReplicationService.InitiateFailover
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# InitiateFailover method of the Msvm\_CollectionReplicationService class

Sets the failover for collection to application or crash consistent image.

## Syntax


```mof
uint32 InitiateFailover(
  [in]  CIM_CollectionOfMSEs         REF Collection,
  [in]  Msvm_CollectionRecoveryPoint REF CollectionRecoveryPoint,
  [out] CIM_ConcreteJob              REF Job
);
```



## Parameters

<dl> <dt>

*Collection* \[in\]
</dt> <dd>

A reference to the [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) instance for which to prepare failover.

</dd> <dt>

*CollectionRecoveryPoint* \[in\]
</dt> <dd>

The [**Msvm\_CollectionRecoveryPoint**](msvm-collectionrecoverypoint.md) instance that represents the collection recovery point used for failover.

Pass NULL if failover is to be performed to the latest point in time.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

An optional reference that is returned if the operation is executed asynchronously. If present, the returned reference to an instance of [**CIM\_ConcreteJob**](cim-concretejob.md) can be used to monitor progress and to obtain the result of the method.

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

 

 





