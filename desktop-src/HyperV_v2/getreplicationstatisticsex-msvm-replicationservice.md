---
description: Retrieves the replication statistics that are associated with the specified replication relationship of the virtual machine.
ms.assetid: AB46894A-CBED-40DF-86B9-B578603B0341
title: Msvm_ReplicationService::GetReplicationStatisticsEx method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ReplicationService.GetReplicationStatisticsEx
api_type: 
- COM
api_location: 
- vmms.exe
---

# Msvm\_ReplicationService::GetReplicationStatisticsEx method

Retrieves the replication statistics that are associated with the specified replication relationship of the virtual machine.

## Syntax


```C++
uint32 GetReplicationStatisticsEx(
  [in]  CIM_ComputerSystem ComputerSystem,
  [in]  string                 ReplicationRelationship,
  [out] string                 ReplicationStatistics[],
  [out] string                 ReplicationHealthIssues[],
  [out] CIM_ConcreteJob    Job
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

A reference to a [**CIM\_ComputerSystem**](/windows/desktop/CIMWin32Prov/cim-computersystem) instance that represents the virtual machine for which to retrieve the replication statistics.

</dd> <dt>

*ReplicationRelationship* \[in\]
</dt> <dd>

A string representation of an embedded instance of the [**Msvm\_ReplicationRelationship**](msvm-replicationrelationship.md) class that defines the replication relationship for which to retrieve the replication statistics.

</dd> <dt>

*ReplicationStatistics* \[out\]
</dt> <dd>

If successful, receives an embedded instance of the [**Msvm\_ReplicationStatistics**](msvm-replicationstatistics.md) class that contains the replication statistics for the requested replication relationship.

</dd> <dt>

*ReplicationHealthIssues* \[out\]
</dt> <dd>

If successful, receives an array of embedded instances of the [**Msvm\_Error**](msvm-error.md) class that indicate any replication warnings or errors for the requested virtual machine.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If the operation is performed asynchronously, this method will return 4096, and this parameter will contain a reference to an object derived from [**CIM\_ConcreteJob**](/previous-versions//cc136808(v=vs.85)). This reference can be **NULL** if the task is complete.

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

**System is in used** (32774)
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
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | \\\\Root\\Virtualization\\V2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_ReplicationService**](msvm-replicationservice.md)
</dt> <dt>

[**ResetReplicationStatisticsEx**](resetreplicationstatisticsex-msvm-replicationservice.md)
</dt> </dl>

 

