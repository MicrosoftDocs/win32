---
title: VMVMState enumeration
description: Specifies the state of a virtual machine.
ms.assetid: 65d293f6-c59b-44c8-adb1-84e95e365184
keywords:
- VMVMState enumeration Virtual Server
topic_type:
- apiref
api_name:
- VMVMState
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
api_location:
- VsComInterfaces.h
api_type:
- HeaderDef
---

# VMVMState enumeration

The **VMVMState** enumeration specifies the state of a virtual machine.

## Syntax


```C++
typedef enum  { 
  vmVMState_Invalid        = 0,
  vmVMState_TurnedOff      = 1,
  vmVMState_Saved          = 2,
  vmVMState_TurningOn      = 3,
  vmVMState_Restoring      = 4,
  vmVMState_Running        = 5,
  vmVMState_Paused         = 6,
  vmVMState_Saving         = 7,
  vmVMState_TurningOff     = 8,
  vmVMState_MergingDrives  = 9,
  vmVMState_DeleteMachine  = 10
} VMVMState;
```



## Constants

<dl> <dt>

<span id="vmVMState_Invalid"></span><span id="vmvmstate_invalid"></span><span id="VMVMSTATE_INVALID"></span>**vmVMState\_Invalid**
</dt> <dd>

Invalid virtual machine state. If the virtual machine exists, this state should not occur.

</dd> <dt>

<span id="vmVMState_TurnedOff"></span><span id="vmvmstate_turnedoff"></span><span id="VMVMSTATE_TURNEDOFF"></span>**vmVMState\_TurnedOff**
</dt> <dd>

The virtual machine is off and the guest was not previously saved.

</dd> <dt>

<span id="vmVMState_Saved"></span><span id="vmvmstate_saved"></span><span id="VMVMSTATE_SAVED"></span>**vmVMState\_Saved**
</dt> <dd>

The virtual machine is off but the guest is saved.

</dd> <dt>

<span id="vmVMState_TurningOn"></span><span id="vmvmstate_turningon"></span><span id="VMVMSTATE_TURNINGON"></span>**vmVMState\_TurningOn**
</dt> <dd>

The virtual machine is turning on or restoring.

</dd> <dt>

<span id="vmVMState_Restoring"></span><span id="vmvmstate_restoring"></span><span id="VMVMSTATE_RESTORING"></span>**vmVMState\_Restoring**
</dt> <dd>

The virtual machine is restoring the previous state of the virtual machine.

</dd> <dt>

<span id="vmVMState_Running"></span><span id="vmvmstate_running"></span><span id="VMVMSTATE_RUNNING"></span>**vmVMState\_Running**
</dt> <dd>

The virtual machine is restored and turned on, not suspended.

</dd> <dt>

<span id="vmVMState_Paused"></span><span id="vmvmstate_paused"></span><span id="VMVMSTATE_PAUSED"></span>**vmVMState\_Paused**
</dt> <dd>

The virtual machine is turned on but has paused execution.

</dd> <dt>

<span id="vmVMState_Saving"></span><span id="vmvmstate_saving"></span><span id="VMVMSTATE_SAVING"></span>**vmVMState\_Saving**
</dt> <dd>

The virtual machine is saving the current state of the virtual machine.

</dd> <dt>

<span id="vmVMState_TurningOff"></span><span id="vmvmstate_turningoff"></span><span id="VMVMSTATE_TURNINGOFF"></span>**vmVMState\_TurningOff**
</dt> <dd>

The virtual machine is turning off.

</dd> <dt>

<span id="vmVMState_MergingDrives"></span><span id="vmvmstate_mergingdrives"></span><span id="VMVMSTATE_MERGINGDRIVES"></span>**vmVMState\_MergingDrives**
</dt> <dd>

The virtual machine is merging undo drives.

</dd> <dt>

<span id="vmVMState_DeleteMachine"></span><span id="vmvmstate_deletemachine"></span><span id="VMVMSTATE_DELETEMACHINE"></span>**vmVMState\_DeleteMachine**
</dt> <dd>

The virtual machine is being deleted.

</dd> </dl>

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[Virtual Server Enumerations](enumerations.md)
</dt> <dt>

[**IVMVirtualMachine.State**](ivmvirtualmachine-state.md)
</dt> <dt>

[**IVMVirtualMachineEvents::OnStateChange**](ivmvirtualmachineevents-onstatechange.md)
</dt> <dt>

[**IVMVirtualServerEvents::OnVMStateChange**](ivmvirtualserverevents-onvmstatechange.md)
</dt> </dl>

 

 





