---
description: Starts the replication of a virtual machine.
ms.assetid: 58e89329-1ad4-4473-856d-ebfd7a863fa8
title: StartReplication method of the Msvm_ReplicationService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ReplicationService.StartReplication
api_type: 
- COM
api_location: 
- vmms.exe
---

# StartReplication method of the Msvm\_ReplicationService class

Starts the replication of a virtual machine. When a client calls this method for a replica virtual machine, it starts the replication with extended replica.

## Syntax


```mof
uint32 StartReplication(
  [in]  CIM_ComputerSystem REF ComputerSystem,
  [in]  uint16                 InitialReplicationType,
  [in]  string                 InitialReplicationExportLocation,
  [in]  datetime               StartTime,
  [out] CIM_ConcreteJob    REF Job
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

A reference to a [**CIM\_ComputerSystem**](/windows/desktop/CIMWin32Prov/cim-computersystem) instance that represents the virtual machine for which the replication should be started.

</dd> <dt>

*InitialReplicationType* \[in\]
</dt> <dd>

The type of transfer to be used for performing the initial replication.

<dt>

<span id="Network_Transfer"></span><span id="network_transfer"></span><span id="NETWORK_TRANSFER"></span>

<span id="Network_Transfer"></span><span id="network_transfer"></span><span id="NETWORK_TRANSFER"></span>**Network Transfer** (1)


</dt> <dd>

Network transfer.

</dd> <dt>

<span id="Export"></span><span id="export"></span><span id="EXPORT"></span>

<span id="Export"></span><span id="export"></span><span id="EXPORT"></span>**Export** (2)


</dt> <dd>

Export.

</dd> <dt>

<span id="Seeded_Network_Transfer"></span><span id="seeded_network_transfer"></span><span id="SEEDED_NETWORK_TRANSFER"></span>

<span id="Seeded_Network_Transfer"></span><span id="seeded_network_transfer"></span><span id="SEEDED_NETWORK_TRANSFER"></span>**Seeded Network Transfer** (3)


</dt> <dd>

Seeded network transfer.

</dd> </dl> </dd> <dt>

*InitialReplicationExportLocation* \[in\]
</dt> <dd>

If *InitialReplicationType* is 2 (Export), this parameter contains the fully qualified path of the directory to which the initial replication is to be exported. This parameter is not used for other values of *InitialReplicationType*, and can be **Null**. This directory can be reused for exporting multiple virtual machine replication. This method places each virtual machine replication in a separate subdirectory under this path.

</dd> <dt>

*StartTime* \[in\]
</dt> <dd>

The scheduled start time for the initial replication over the network connection to recovery server. This parameter is ignored when *InitialReplicationType* is 2 (Export). If this parameter is **Null**, the initial replication starts immediately.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If the operation is performed asynchronously, this method will return 4096, and this parameter will contain a reference to an object derived from [**CIM\_ConcreteJob**](/previous-versions//cc136808(v=vs.85)).

</dd> </dl>

## Return value

This method returns one of the following values.

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



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_ReplicationService**](msvm-replicationservice.md)
</dt> </dl>

 

