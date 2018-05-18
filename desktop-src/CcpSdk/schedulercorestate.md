---
Description: 'Defines the state of the core.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8872b42a-a2f7-4ab5-813d-17f13530a388'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: SchedulerCoreState enumeration
---

# SchedulerCoreState enumeration

Defines the state of the core.

## Syntax


```C++
typedef enum  { 
  SchedulerCoreStatee_Offline  = 0,
  SchedulerCoreState_Idle      = 1,
  SchedulerCoreState_Busy      = 2,
  SchedulerCoreState_Draining  = 3,
  SchedulerCoreState_Reserved  = 4
} SchedulerCoreState;
```



## Constants

<dl> <dt>

<span id="SchedulerCoreStatee_Offline"></span><span id="schedulercorestatee_offline"></span><span id="SCHEDULERCORESTATEE_OFFLINE"></span>**SchedulerCoreStatee\_Offline**
</dt> <dd>

The core is offline.

</dd> <dt>

<span id="SchedulerCoreState_Idle"></span><span id="schedulercorestate_idle"></span><span id="SCHEDULERCORESTATE_IDLE"></span>**SchedulerCoreState\_Idle**
</dt> <dd>

The core is idle and ready to run a job.

</dd> <dt>

<span id="SchedulerCoreState_Busy"></span><span id="schedulercorestate_busy"></span><span id="SCHEDULERCORESTATE_BUSY"></span>**SchedulerCoreState\_Busy**
</dt> <dd>

The core is running a job or task.

</dd> <dt>

<span id="SchedulerCoreState_Draining"></span><span id="schedulercorestate_draining"></span><span id="SCHEDULERCORESTATE_DRAINING"></span>**SchedulerCoreState\_Draining**
</dt> <dd>

The core is running a job but is marked to be taken offline after the current job finishes.

</dd> <dt>

<span id="SchedulerCoreState_Reserved"></span><span id="schedulercorestate_reserved"></span><span id="SCHEDULERCORESTATE_RESERVED"></span>**SchedulerCoreState\_Reserved**
</dt> <dd>

The core is reserved for a job.

</dd> </dl>

## Requirements



|                         |                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.Properties.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Enumerations](hpc-enumerations.md)
</dt> <dt>

[**ISchedulerCore.State**](ischedulercore-state.md)
</dt> </dl>

 

 




