---
Description: 'Defines the hardware resources that the scheduler can use to determine on which nodes the job can run.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '11a7186b-a023-419c-a580-ddd7220b9d51'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: JobUnitType enumeration
---

# JobUnitType enumeration

Defines the hardware resources that the scheduler can use to determine on which nodes the job can run.

## Syntax


```C++
typedef enum  { 
  JobUnitType_Core    = 0,
  JobUnitType_Socket  = 1,
  JobUnitType_Node    = 2
} JobUnitType;
```



## Constants

<dl> <dt>

<span id="JobUnitType_Core"></span><span id="jobunittype_core"></span><span id="JOBUNITTYPE_CORE"></span>**JobUnitType\_Core**
</dt> <dd>

Use cores to schedule the job.

</dd> <dt>

<span id="JobUnitType_Socket"></span><span id="jobunittype_socket"></span><span id="JOBUNITTYPE_SOCKET"></span>**JobUnitType\_Socket**
</dt> <dd>

Use sockets to schedule the job.

</dd> <dt>

<span id="JobUnitType_Node"></span><span id="jobunittype_node"></span><span id="JOBUNITTYPE_NODE"></span>**JobUnitType\_Node**
</dt> <dd>

Use nodes to schedule the job.

</dd> </dl>

## Remarks

The least granular resource unit is the node and the most granular resource unit is the core. For example, a node can have four cores on one socket and the node can contain multiple sockets. A job can specify that it needs a minimum of four nodes to run, regardless of how many cores are on each node. The job could also specify that it needs four cores to run, so it could run on one node that had four cores or on multiple nodes with one or two cores.

## Requirements



|                         |                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.Properties.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Enumerations](hpc-enumerations.md)
</dt> <dt>

[**ISchedulerJob.UnitType**](ischedulerjob-unittype.md)
</dt> </dl>

 

 




