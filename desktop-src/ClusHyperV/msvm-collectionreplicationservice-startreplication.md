---
title: StartReplication method of the Msvm\_CollectionReplicationService class
description: Starts the replication service for a collection of virtual machines.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '568684ba-0df8-41e9-b25c-84ce1f74906e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["StartReplication method", "StartReplication method, Msvm_CollectionReplicationService class", "Msvm_CollectionReplicationService class, StartReplication method"]
topic_type:
- apiref
api_name:
- Msvm_CollectionReplicationService.StartReplication
api_location:
- VMMS.exe
api_type:
- COM
---

# StartReplication method of the Msvm\_CollectionReplicationService class

Starts the replication service for a collection of virtual machines.

## Syntax


```mof
uint32 StartReplication(
  [in]  CIM_CollectionOfMSEs REF Collection,
  [in]  uint16                   InitialReplicationType,
  [in]  string                   InitialReplicationExportLocation,
  [in]  datetime                 StartTime,
  [out] CIM_ConcreteJob      REF Job
);
```



## Parameters

<dl> <dt>

*Collection* \[in\]
</dt> <dd>

A reference to the [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) instance that represents the collection of virtual machines.

</dd> <dt>

*InitialReplicationType* \[in\]
</dt> <dd>

The type of transfer to use for the initial replication.

<dt>

<span id="Network_Transfer"></span><span id="network_transfer"></span><span id="NETWORK_TRANSFER"></span>

**Network Transfer** (1)


</dt> <dd></dd> <dt>

<span id="Export"></span><span id="export"></span><span id="EXPORT"></span>

**Export** (2)


</dt> <dd></dd> <dt>

<span id="Seeded_Network_Transfer"></span><span id="seeded_network_transfer"></span><span id="SEEDED_NETWORK_TRANSFER"></span>

**Seeded Network Transfer** (3)


</dt> <dd></dd> </dl> </dd> <dt>

*InitialReplicationExportLocation* \[in\]
</dt> <dd>

If the **InitialReplicationType** property is set to "2" (export), this contains the fully-qualified path of the directory to which the initial replication is exported. This method places each virtual machine replication in a separate subdirectory under.

</dd> <dt>

*StartTime* \[in\]
</dt> <dd>

The scheduled start time for the initial replication. This parameter is ignored when the **InitialReplicationType** property is set to "2" (export). When **StartTime** is not specified, initial replication starts immediately.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

An optional job to use for this operation if it is performed asynchronously.

</dd> </dl>

## Return value

The possible return values are:

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
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_CollectionReplicationService**](msvm-collectionreplicationservice.md)
</dt> </dl>

 

 





