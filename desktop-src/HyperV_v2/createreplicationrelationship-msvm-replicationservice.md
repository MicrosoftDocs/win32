---
description: Creates a new replication relationship for a virtual machine. When a client calls this method for a replica virtual machine, it extends the replication relationship to the specified provider.
ms.assetid: 44d3b5aa-46c2-4fe9-9a1d-6ee699d3640d
title: CreateReplicationRelationship method of the Msvm_ReplicationService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ReplicationService.CreateReplicationRelationship
api_type: 
- COM
api_location: 
- vmms.exe
---

# CreateReplicationRelationship method of the Msvm\_ReplicationService class

Creates a new replication relationship for a virtual machine. When a client calls this method for a replica virtual machine, it extends the replication relationship to the specified provider.

## Syntax


```mof
uint32 CreateReplicationRelationship(
  [in]  CIM_ComputerSystem REF ComputerSystem,
  [in]  string                 ReplicationSettingData,
  [out] CIM_ConcreteJob    REF Job
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

A reference to a [**CIM\_ComputerSystem**](/windows/desktop/CIMWin32Prov/cim-computersystem) instance that represents the virtual machine for which the replication should be enabled.

</dd> <dt>

*ReplicationSettingData* \[in\]
</dt> <dd>

A string representation of an instance of the [**Msvm\_ReplicationSettingData**](msvm-replicationsettingdata.md) class that defines the replication settings for the new replication relationship to be created for the virtual machine.

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

## Remarks

**CreateReplicationRelationship** takes an [**Msvm\_ReplicationSettingData**](msvm-replicationsettingdata.md) instance (FRSD) as input. The associated FRSD for the virtual machine as host-to-host provider is the default choice. Input FRSD is validated for valid settings for each property for the default provider. This table summarizes the validation differences with respect to the external provider.



| Property                                             | External providers                                 |
|------------------------------------------------------|----------------------------------------------------|
| ReplicationProvider                                  | Same as default provider                           |
| AuthenticationType                                   | Ignored                                            |
| CertificateThumbPrint                                | Ignored                                            |
| RootCertificateThumbPrint (RO)                       | Ignored                                            |
| CompressionEnabled                                   | Same as default provider                           |
| BypassProxyServer                                    | Same as default provider                           |
| RecoveryConnectionPoint                              | Ignored\* (may change if provider has requirement) |
| RecoveryHostSystem (RO)                              | Ignored                                            |
| PrimaryConnectionPoint (RO)                          | Same as default provider                           |
| PrimaryHostSystem (RO)                               | Same as default provider                           |
| RecoveryServerPortNumber                             | Ignored\* (may change if provider has requirement) |
| ReplicateHostKvpItems                                | Ignored                                            |
| ApplicationConsistentSnapshotInterval                | Same as default provider                           |
| RecoveryHistory                                      | Same as default provider                           |
| IncludedDisks\[\]                                    | Same as default provider                           |
| AutoResynchronizeEnabled                             | Same as default provider                           |
| AutoResynchronizeIntervalStart                       | Same as default provider                           |
| AutoResynchronizeIntervalEnd                         | Same as default provider                           |
| EnableWriteOrderPreservationAcrossDisks (Deprecated) | Same as default provider                           |
| ReplicationInterval                                  | Same as default provider                           |



 

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
</dt> <dt>

[**RemoveReplicationRelationshipEx**](removereplicationrelationshipex-msvm-replicationservice.md)
</dt> </dl>

 

