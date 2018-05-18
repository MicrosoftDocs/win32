---
Description: 'Defines the types of jobs that run in the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '213ba4b8-2983-4b00-8682-d5993dbd125c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: JobType enumeration
---

# JobType enumeration

Defines the types of jobs that run in the cluster.

## Syntax


```C++
typedef enum  { 
  JobType_Batch    = 1,
  JobType_Admin    = 2,
  JobType_Service  = 4,
  JobType_Broker   = 8
} JobType;
```



## Constants

<dl> <dt>

<span id="JobType_Batch"></span><span id="jobtype_batch"></span><span id="JOBTYPE_BATCH"></span>**JobType\_Batch**
</dt> <dd>

A normally scheduled job (see [**IScheduler::CreateJob**](ischeduler-createjob.md)).

</dd> <dt>

<span id="JobType_Admin"></span><span id="jobtype_admin"></span><span id="JOBTYPE_ADMIN"></span>**JobType\_Admin**
</dt> <dd>

A job that contains a command that runs immediately (see [**IScheduler::CreateCommand**](ischeduler-createcommand.md)).

</dd> <dt>

<span id="JobType_Service"></span><span id="jobtype_service"></span><span id="JOBTYPE_SERVICE"></span>**JobType\_Service**
</dt> <dd>

A service job based on the service-oriented architecture (SOA) programming model.

</dd> <dt>

<span id="JobType_Broker"></span><span id="jobtype_broker"></span><span id="JOBTYPE_BROKER"></span>**JobType\_Broker**
</dt> <dd>

A broker job that routes requests from a SOA-based client to an instance of a service job.

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

[**ISchedulerNode.JobType**](ischedulernode-jobtype.md)
</dt> <dt>

[**PropId**](propid.md)
</dt> </dl>

 

 




