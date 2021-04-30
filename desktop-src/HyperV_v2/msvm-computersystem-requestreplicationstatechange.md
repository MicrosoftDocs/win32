---
description: Requests that the replication state of the virtual machine be changed to the specified value and acts on the primary replication relationship of the virtual machine.
ms.assetid: 65FCDADD-1C50-4816-B10B-A951D1FC9C3B
title: RequestReplicationStateChange method of the Msvm_ComputerSystem class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ComputerSystem.RequestReplicationStateChange
api_type: 
- COM
api_location: 
- vmms.exe
---

# RequestReplicationStateChange method of the Msvm\_ComputerSystem class

Requests that the replication state of the virtual machine be changed to the specified value and acts on the primary replication relationship of the virtual machine. While the state change is in progress, the **ReplicationState** property is changed to the value of the *RequestedState* parameter. This method is only supported for instances of the [**Msvm\_ComputerSystem**](msvm-computersystem.md) class that represent a virtual machine.

> [!Note]  
> Starting with Windows 8.1, we recommend not to use **RequestReplicationStateChange** anymore to request changing of replication state. Instead, use [**RequestReplicationStateChangeEx**](msvm-requestreplicationstatechangeex-computersystem.md).

 

## Syntax


```mof
uint32 RequestReplicationStateChange(
  [in]  uint16              RequestedState,
  [out] CIM_ConcreteJob REF Job,
  [in]  datetime            TimeoutPeriod
);
```



## Parameters

<dl> <dt>

*RequestedState* \[in\]
</dt> <dd>

The new replication state. The must be one of the following values.

<dt>

<span id="Ready_to_start_initial_replication"></span><span id="ready_to_start_initial_replication"></span><span id="READY_TO_START_INITIAL_REPLICATION"></span>

<span id="Ready_to_start_initial_replication"></span><span id="ready_to_start_initial_replication"></span><span id="READY_TO_START_INITIAL_REPLICATION"></span>**Ready to start initial replication** (1)


</dt> <dd>

Ready to start initial replication.

</dd> <dt>

<span id="Waiting_to_complete_initial_replication"></span><span id="waiting_to_complete_initial_replication"></span><span id="WAITING_TO_COMPLETE_INITIAL_REPLICATION"></span>

<span id="Waiting_to_complete_initial_replication"></span><span id="waiting_to_complete_initial_replication"></span><span id="WAITING_TO_COMPLETE_INITIAL_REPLICATION"></span>**Waiting to complete initial replication** (2)


</dt> <dd>

Waiting to complete initial replication.

</dd> <dt>

<span id="Replicating"></span><span id="replicating"></span><span id="REPLICATING"></span>

<span id="Replicating"></span><span id="replicating"></span><span id="REPLICATING"></span>**Replicating** (3)


</dt> <dd>

Replicating.

</dd> <dt>

<span id="Synced_replication_complete"></span><span id="synced_replication_complete"></span><span id="SYNCED_REPLICATION_COMPLETE"></span>

<span id="Synced_replication_complete"></span><span id="synced_replication_complete"></span><span id="SYNCED_REPLICATION_COMPLETE"></span>**Synced replication complete** (4)


</dt> <dd>

Synced replication complete.

</dd> <dt>

<span id="Suspend"></span><span id="suspend"></span><span id="SUSPEND"></span>

<span id="Suspend"></span><span id="suspend"></span><span id="SUSPEND"></span>**Suspend** (7)


</dt> <dd>

Suspend replication.

</dd> <dt>

<span id="Cancel_Resynchronize"></span><span id="cancel_resynchronize"></span><span id="CANCEL_RESYNCHRONIZE"></span>

<span id="Cancel_Resynchronize"></span><span id="cancel_resynchronize"></span><span id="CANCEL_RESYNCHRONIZE"></span>**Cancel Resynchronize** (9)


</dt> <dd>

Cancel resynchronization.

</dd> </dl> </dd> <dt>

*Job* \[out\]
</dt> <dd>

An optional reference to a [**Msvm\_ConcreteJob**](msvm-concretejob.md) object that is returned if the operation is executed asynchronously. If present, the returned reference can be used to monitor progress and obtain the result of the method.

</dd> <dt>

*TimeoutPeriod* \[in\]
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

This method returns one of the following values.



| Return code/value                                                                                                                                                                | Description                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**Completed with No Error**</dt> <dt>0</dt> </dl>                    | Success<br/>                                                                                                          |
| <dl> <dt>**Method Parameters Checked - Job Started**</dt> <dt>4096</dt> </dl> | The transition is asynchronous.<br/>                                                                                  |
| <dl> <dt>**Failed**</dt> <dt>32768</dt> </dl>                                 |                                                                                                                             |
| <dl> <dt>**Access Denied**</dt> <dt>32769</dt> </dl>                          |                                                                                                                             |
| <dl> <dt>**Not Supported**</dt> <dt>32770</dt> </dl>                          |                                                                                                                             |
| <dl> <dt>**Status is unknown**</dt> <dt>32771</dt> </dl>                      |                                                                                                                             |
| <dl> <dt>**Timeout**</dt> <dt>32772</dt> </dl>                                |                                                                                                                             |
| <dl> <dt>**Invalid parameter**</dt> <dt>32773</dt> </dl>                      | The value specified in one of the parameters is not supported.<br/>                                                   |
| <dl> <dt>**System is in use**</dt> <dt>32774</dt> </dl>                       |                                                                                                                             |
| <dl> <dt>**Invalid state for this operation**</dt> <dt>32775</dt> </dl>       | The value specified in the *RequestedState* parameter is not supported in the current replication mode or state.<br/> |
| <dl> <dt>**Incorrect data type**</dt> <dt>32776</dt> </dl>                    |                                                                                                                             |
| <dl> <dt>**System is not available**</dt> <dt>32777</dt> </dl>                |                                                                                                                             |
| <dl> <dt>**Out of memory**</dt> <dt>32778</dt> </dl>                          |                                                                                                                             |
| <dl> <dt>**File not found**</dt> <dt>32779</dt> </dl>                         |                                                                                                                             |



 

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

[**Msvm\_ComputerSystem**](msvm-computersystem.md)
</dt> </dl>

 

 




