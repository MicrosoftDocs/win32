---
Description: 'Defines identifiers that uniquely identify job, task, and node properties. Use these property identifiers when specifying a filter or sort property.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f94c64ee-34e3-4422-8f93-683804f00254'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: PropId enumeration
---

# PropId enumeration

Defines identifiers that uniquely identify job, task, and node properties. Use these property identifiers when specifying a filter or sort property.

## Syntax


```C++
typedef enum  { 
  PropId_Job_AutoCalculateMax  = 1083,
  PropId_Job_AutoCalculateMin  = 1084,
  PropId_Job_CanGrow           = 1059,
  PropId_Job_CanShrink         = 1060,
  PropId_Job_ChangeTime        = 16,
  PropId_Job_CreateTime        = 11,
  PropId_Job_EndTime           = 14,
  PropId_Job_IsExclusive       = 53,
  PropId_Job_JobType           = 1007,
  PropId_Job_MaxCores          = 41,
  PropId_Job_MaxNodes          = 45,
  PropId_Job_MaxSockets        = 43,
  PropId_Job_MinCores          = 40,
  PropId_Job_MinNodes          = 44,
  PropId_Job_MinSockets        = 42,
  PropId_Job_Name              = 2,
  PropId_Job_Owner             = 1003,
  PropId_Job_PreviousState     = 1002,
  PropId_Job_Priority          = 1017,
  PropId_Job_Project           = 1006,
  PropId_Job_RequeueCount      = 1075,
  PropId_Job_RuntimeSeconds    = 51,
  PropId_Job_RunUntilCanceled  = 52,
  PropId_Job_StartTime         = 12,
  PropId_Job_State             = 1001,
  PropId_Job_SubmitTime        = 10,
  PropId_Job_UnitType          = 39,
  PropId_Job_UserName          = 1004,
  PropId_Node_CpuSpeed         = 8017,
  PropId_Node_Guid             = 8015,
  PropId_Node_JobType          = 400,
  PropId_Node_MemorySize       = 8016,
  PropId_Node_Name             = 2,
  PropId_Node_NumCores         = 8005,
  PropId_Node_NumSockets       = 8006,
  PropId_Node_OfflineTime      = 8008,
  PropId_Node_OnlineTime       = 8009,
  PropId_Node_Reachable        = 8004,
  PropId_Node_State            = 8001,
  PropId_Task_ChangeTime       = 16,
  PropId_Task_CreateTime       = 11,
  PropId_Task_EndTime          = 14,
  PropId_Task_ExitCode         = 2033,
  PropId_Task_IsExclusive      = 53,
  PropId_Task_IsParametric     = 2050,
  PropId_Task_IsRerunnable     = 2015,
  PropId_Task_MaxCores         = 41,
  PropId_Task_MaxNodes         = 45,
  PropId_Task_MaxSockets       = 43,
  PropId_Task_MinCores         = 40,
  PropId_Task_MinNodes         = 44,
  PropId_Task_MinSockets       = 42,
  PropId_Task_Name             = 2,
  PropId_Task_ParentJobId      = 2003,
  PropId_Task_PreviousState    = 2002,
  PropId_Task_RequeueCount     = 2044,
  PropId_Task_RuntimeSeconds   = 51,
  PropId_Task_StartTime        = 12,
  PropId_Task_State            = 2001,
  PropId_Task_SubmitTime       = 10,
  PropId_Task_Type             = 2080
} PropId;
```



## Constants

<dl> <dt>

<span id="PropId_Job_AutoCalculateMax"></span><span id="propid_job_autocalculatemax"></span><span id="PROPID_JOB_AUTOCALCULATEMAX"></span>**PropId\_Job\_AutoCalculateMax**
</dt> <dd>

Identifies the [**AutoCalculateMax**](ischedulerjob-autocalculatemax.md) job property.

</dd> <dt>

<span id="PropId_Job_AutoCalculateMin"></span><span id="propid_job_autocalculatemin"></span><span id="PROPID_JOB_AUTOCALCULATEMIN"></span>**PropId\_Job\_AutoCalculateMin**
</dt> <dd>

Identifies the [**AutoCalculateMin**](ischedulerjob-autocalculatemin.md) job property.

</dd> <dt>

<span id="PropId_Job_CanGrow"></span><span id="propid_job_cangrow"></span><span id="PROPID_JOB_CANGROW"></span>**PropId\_Job\_CanGrow**
</dt> <dd>

Identifies the [**CanGrow**](ischedulerjob-cangrow.md) job property.

</dd> <dt>

<span id="PropId_Job_CanShrink"></span><span id="propid_job_canshrink"></span><span id="PROPID_JOB_CANSHRINK"></span>**PropId\_Job\_CanShrink**
</dt> <dd>

Identifies the [**CanShrink**](ischedulerjob-canshrink.md) job property.

</dd> <dt>

<span id="PropId_Job_ChangeTime"></span><span id="propid_job_changetime"></span><span id="PROPID_JOB_CHANGETIME"></span>**PropId\_Job\_ChangeTime**
</dt> <dd>

Identifies the [**ChangeTime**](ischedulerjob-changetime.md) job property.

</dd> <dt>

<span id="PropId_Job_CreateTime"></span><span id="propid_job_createtime"></span><span id="PROPID_JOB_CREATETIME"></span>**PropId\_Job\_CreateTime**
</dt> <dd>

Identifies the [**CreateTime**](ischedulerjob-createtime.md) job property.

</dd> <dt>

<span id="PropId_Job_EndTime"></span><span id="propid_job_endtime"></span><span id="PROPID_JOB_ENDTIME"></span>**PropId\_Job\_EndTime**
</dt> <dd>

Identifies the [**EndTime**](ischedulerjob-endtime.md) job property.

</dd> <dt>

<span id="PropId_Job_IsExclusive"></span><span id="propid_job_isexclusive"></span><span id="PROPID_JOB_ISEXCLUSIVE"></span>**PropId\_Job\_IsExclusive**
</dt> <dd>

Identifies the [**IsExclusive**](ischedulerjob-isexclusive.md) job property.

</dd> <dt>

<span id="PropId_Job_JobType"></span><span id="propid_job_jobtype"></span><span id="PROPID_JOB_JOBTYPE"></span>**PropId\_Job\_JobType**
</dt> <dd>

The job is filtered or sorted based on its job type. For possible job type values, see the [**JobType**](jobtype.md) enumeration.

</dd> <dt>

<span id="PropId_Job_MaxCores"></span><span id="propid_job_maxcores"></span><span id="PROPID_JOB_MAXCORES"></span>**PropId\_Job\_MaxCores**
</dt> <dd>

Identifies the [**MaximumNumberOfCores**](ischedulerjob-maximumnumberofcores.md) job property.

</dd> <dt>

<span id="PropId_Job_MaxNodes"></span><span id="propid_job_maxnodes"></span><span id="PROPID_JOB_MAXNODES"></span>**PropId\_Job\_MaxNodes**
</dt> <dd>

Identifies the [**MaximumNumberOfNodes**](ischedulerjob-maximumnumberofnodes.md) job property.

</dd> <dt>

<span id="PropId_Job_MaxSockets"></span><span id="propid_job_maxsockets"></span><span id="PROPID_JOB_MAXSOCKETS"></span>**PropId\_Job\_MaxSockets**
</dt> <dd>

Identifies the [**MaximumNumberOfSockets**](ischedulerjob-maximumnumberofsockets.md) job property.

</dd> <dt>

<span id="PropId_Job_MinCores"></span><span id="propid_job_mincores"></span><span id="PROPID_JOB_MINCORES"></span>**PropId\_Job\_MinCores**
</dt> <dd>

Identifies the [**MinimumNumberOfCores**](ischedulerjob-minimumnumberofcores.md) job property.

</dd> <dt>

<span id="PropId_Job_MinNodes"></span><span id="propid_job_minnodes"></span><span id="PROPID_JOB_MINNODES"></span>**PropId\_Job\_MinNodes**
</dt> <dd>

Identifies the [**MinimumNumberOfNodes**](ischedulerjob-minimumnumberofnodes.md) job property.

</dd> <dt>

<span id="PropId_Job_MinSockets"></span><span id="propid_job_minsockets"></span><span id="PROPID_JOB_MINSOCKETS"></span>**PropId\_Job\_MinSockets**
</dt> <dd>

Identifies the [**MinimumNumberOfSockets**](ischedulerjob-minimumnumberofsockets.md) job property.

</dd> <dt>

<span id="PropId_Job_Name"></span><span id="propid_job_name"></span><span id="PROPID_JOB_NAME"></span>**PropId\_Job\_Name**
</dt> <dd>

Identifies the [**Name**](ischedulerjob-name.md) job property.

</dd> <dt>

<span id="PropId_Job_Owner"></span><span id="propid_job_owner"></span><span id="PROPID_JOB_OWNER"></span>**PropId\_Job\_Owner**
</dt> <dd>

Identifies the [**Owner**](ischedulerjob-owner.md) job property.

</dd> <dt>

<span id="PropId_Job_PreviousState"></span><span id="propid_job_previousstate"></span><span id="PROPID_JOB_PREVIOUSSTATE"></span>**PropId\_Job\_PreviousState**
</dt> <dd>

Identifies the [**PreviousState**](ischedulerjob-previousstate.md) job property.

</dd> <dt>

<span id="PropId_Job_Priority"></span><span id="propid_job_priority"></span><span id="PROPID_JOB_PRIORITY"></span>**PropId\_Job\_Priority**
</dt> <dd>

Identifies the [**Priority**](ischedulerjob-priority.md) job property.

</dd> <dt>

<span id="PropId_Job_Project"></span><span id="propid_job_project"></span><span id="PROPID_JOB_PROJECT"></span>**PropId\_Job\_Project**
</dt> <dd>

Identifies the [**Project**](ischedulerjob-project.md) job property.

</dd> <dt>

<span id="PropId_Job_RequeueCount"></span><span id="propid_job_requeuecount"></span><span id="PROPID_JOB_REQUEUECOUNT"></span>**PropId\_Job\_RequeueCount**
</dt> <dd>

Identifies the [**RequeueCount**](ischedulerjob-requeuecount.md) job property.

</dd> <dt>

<span id="PropId_Job_RuntimeSeconds"></span><span id="propid_job_runtimeseconds"></span><span id="PROPID_JOB_RUNTIMESECONDS"></span>**PropId\_Job\_RuntimeSeconds**
</dt> <dd>

Identifies the [**Runtime**](ischedulerjob-runtime.md) job property.

</dd> <dt>

<span id="PropId_Job_RunUntilCanceled"></span><span id="propid_job_rununtilcanceled"></span><span id="PROPID_JOB_RUNUNTILCANCELED"></span>**PropId\_Job\_RunUntilCanceled**
</dt> <dd>

Identifies the [**RunUntilCanceled**](ischedulerjob-rununtilcanceled.md) job property.

</dd> <dt>

<span id="PropId_Job_StartTime"></span><span id="propid_job_starttime"></span><span id="PROPID_JOB_STARTTIME"></span>**PropId\_Job\_StartTime**
</dt> <dd>

Identifies the [**StartTime**](ischedulerjob-starttime.md) job property.

</dd> <dt>

<span id="PropId_Job_State"></span><span id="propid_job_state"></span><span id="PROPID_JOB_STATE"></span>**PropId\_Job\_State**
</dt> <dd>

Identifies the [**State**](ischedulerjob-state.md) job property. Note that when used to sort the jobs, the sort order is based on the enumerated value.

</dd> <dt>

<span id="PropId_Job_SubmitTime"></span><span id="propid_job_submittime"></span><span id="PROPID_JOB_SUBMITTIME"></span>**PropId\_Job\_SubmitTime**
</dt> <dd>

Identifies the [**SubmitTime**](ischedulerjob-submittime.md) job property.

</dd> <dt>

<span id="PropId_Job_UnitType"></span><span id="propid_job_unittype"></span><span id="PROPID_JOB_UNITTYPE"></span>**PropId\_Job\_UnitType**
</dt> <dd>

Identifies the [**UnitType**](ischedulerjob-unittype.md) job property.

</dd> <dt>

<span id="PropId_Job_UserName"></span><span id="propid_job_username"></span><span id="PROPID_JOB_USERNAME"></span>**PropId\_Job\_UserName**
</dt> <dd>

Identifies the [**UserName**](ischedulerjob-username.md) job property.

</dd> <dt>

<span id="PropId_Node_CpuSpeed"></span><span id="propid_node_cpuspeed"></span><span id="PROPID_NODE_CPUSPEED"></span>**PropId\_Node\_CpuSpeed**
</dt> <dd>

Identifies the [**CpuSpeed**](ischedulernode-cpuspeed.md) node property.

</dd> <dt>

<span id="PropId_Node_Guid"></span><span id="propid_node_guid"></span><span id="PROPID_NODE_GUID"></span>**PropId\_Node\_Guid**
</dt> <dd>

Identifies the [**Guid**](ischedulernode-guid.md) node property.

</dd> <dt>

<span id="PropId_Node_JobType"></span><span id="propid_node_jobtype"></span><span id="PROPID_NODE_JOBTYPE"></span>**PropId\_Node\_JobType**
</dt> <dd>

Identifies the [**JobType**](ischedulernode-jobtype.md) node property.

</dd> <dt>

<span id="PropId_Node_MemorySize"></span><span id="propid_node_memorysize"></span><span id="PROPID_NODE_MEMORYSIZE"></span>**PropId\_Node\_MemorySize**
</dt> <dd>

Identifies the [**MemorySize**](ischedulernode-memorysize.md) node property.

</dd> <dt>

<span id="PropId_Node_Name"></span><span id="propid_node_name"></span><span id="PROPID_NODE_NAME"></span>**PropId\_Node\_Name**
</dt> <dd>

Identifies the [**Name**](ischedulernode-name.md) node property.

</dd> <dt>

<span id="PropId_Node_NumCores"></span><span id="propid_node_numcores"></span><span id="PROPID_NODE_NUMCORES"></span>**PropId\_Node\_NumCores**
</dt> <dd>

Identifies the [**NumberOfCores**](ischedulernode-numberofcores.md) node property.

</dd> <dt>

<span id="PropId_Node_NumSockets"></span><span id="propid_node_numsockets"></span><span id="PROPID_NODE_NUMSOCKETS"></span>**PropId\_Node\_NumSockets**
</dt> <dd>

Identifies the [**NumberOfSockets**](ischedulernode-numberofsockets.md) node property.

</dd> <dt>

<span id="PropId_Node_OfflineTime"></span><span id="propid_node_offlinetime"></span><span id="PROPID_NODE_OFFLINETIME"></span>**PropId\_Node\_OfflineTime**
</dt> <dd>

Identifies the [**Offline**](ischedulernode-offlinetime.md) node property.

</dd> <dt>

<span id="PropId_Node_OnlineTime"></span><span id="propid_node_onlinetime"></span><span id="PROPID_NODE_ONLINETIME"></span>**PropId\_Node\_OnlineTime**
</dt> <dd>

Identifies the [**OnlineTime**](ischedulernode-onlinetime.md) node property.

</dd> <dt>

<span id="PropId_Node_Reachable"></span><span id="propid_node_reachable"></span><span id="PROPID_NODE_REACHABLE"></span>**PropId\_Node\_Reachable**
</dt> <dd>

Identifies the [**Reachable**](ischedulernode-reachable.md) node property.

</dd> <dt>

<span id="PropId_Node_State"></span><span id="propid_node_state"></span><span id="PROPID_NODE_STATE"></span>**PropId\_Node\_State**
</dt> <dd>

Identifies the [**State**](ischedulernode-state.md) node property. Note that when used to sort the tasks, the sort order is based on the enumerated value.

</dd> <dt>

<span id="PropId_Task_ChangeTime"></span><span id="propid_task_changetime"></span><span id="PROPID_TASK_CHANGETIME"></span>**PropId\_Task\_ChangeTime**
</dt> <dd>

Identifies the [**ChangeTime**](ischedulertask-changetime.md) task property.

</dd> <dt>

<span id="PropId_Task_CreateTime"></span><span id="propid_task_createtime"></span><span id="PROPID_TASK_CREATETIME"></span>**PropId\_Task\_CreateTime**
</dt> <dd>

Identifies the [**CreateTime**](ischedulertask-createtime.md) task property.

</dd> <dt>

<span id="PropId_Task_EndTime"></span><span id="propid_task_endtime"></span><span id="PROPID_TASK_ENDTIME"></span>**PropId\_Task\_EndTime**
</dt> <dd>

Identifies the [**EndTime**](ischedulertask-endtime.md) task property.

</dd> <dt>

<span id="PropId_Task_ExitCode"></span><span id="propid_task_exitcode"></span><span id="PROPID_TASK_EXITCODE"></span>**PropId\_Task\_ExitCode**
</dt> <dd>

Identifies the [**ExitCode**](ischedulertask-exitcode.md) task property.

</dd> <dt>

<span id="PropId_Task_IsExclusive"></span><span id="propid_task_isexclusive"></span><span id="PROPID_TASK_ISEXCLUSIVE"></span>**PropId\_Task\_IsExclusive**
</dt> <dd>

Identifies the [**IsExclusive**](ischedulertask-isexclusive.md) task property.

</dd> <dt>

<span id="PropId_Task_IsParametric"></span><span id="propid_task_isparametric"></span><span id="PROPID_TASK_ISPARAMETRIC"></span>**PropId\_Task\_IsParametric**
</dt> <dd>

Identifies the [**IsParametric**](ischedulertask-isparametric.md) task property.

</dd> <dt>

<span id="PropId_Task_IsRerunnable"></span><span id="propid_task_isrerunnable"></span><span id="PROPID_TASK_ISRERUNNABLE"></span>**PropId\_Task\_IsRerunnable**
</dt> <dd>

Identifies the [**IsRerunnable**](ischedulertask-isrerunnable.md) task property.

</dd> <dt>

<span id="PropId_Task_MaxCores"></span><span id="propid_task_maxcores"></span><span id="PROPID_TASK_MAXCORES"></span>**PropId\_Task\_MaxCores**
</dt> <dd>

Identifies the [**MaximumNumberOfCores**](ischedulertask-maximumnumberofcores.md) task property.

</dd> <dt>

<span id="PropId_Task_MaxNodes"></span><span id="propid_task_maxnodes"></span><span id="PROPID_TASK_MAXNODES"></span>**PropId\_Task\_MaxNodes**
</dt> <dd>

Identifies the [**MaximumNumberOfNodes**](ischedulertask-maximumnumberofnodes.md) task property.

</dd> <dt>

<span id="PropId_Task_MaxSockets"></span><span id="propid_task_maxsockets"></span><span id="PROPID_TASK_MAXSOCKETS"></span>**PropId\_Task\_MaxSockets**
</dt> <dd>

Identifies the [**MaximumNumberOfSockets**](ischedulertask-maximumnumberofsockets.md) task property.

</dd> <dt>

<span id="PropId_Task_MinCores"></span><span id="propid_task_mincores"></span><span id="PROPID_TASK_MINCORES"></span>**PropId\_Task\_MinCores**
</dt> <dd>

Identifies the [**MinimumNumberOfCores**](ischedulertask-minimumnumberofcores.md) task property.

</dd> <dt>

<span id="PropId_Task_MinNodes"></span><span id="propid_task_minnodes"></span><span id="PROPID_TASK_MINNODES"></span>**PropId\_Task\_MinNodes**
</dt> <dd>

Identifies the [**MinimumNumberOfNodes**](ischedulertask-minimumnumberofnodes.md) task property.

</dd> <dt>

<span id="PropId_Task_MinSockets"></span><span id="propid_task_minsockets"></span><span id="PROPID_TASK_MINSOCKETS"></span>**PropId\_Task\_MinSockets**
</dt> <dd>

Identifies the [**MinimumNumberOfSockets**](ischedulertask-minimumnumberofsockets.md) task property.

</dd> <dt>

<span id="PropId_Task_Name"></span><span id="propid_task_name"></span><span id="PROPID_TASK_NAME"></span>**PropId\_Task\_Name**
</dt> <dd>

Identifies the [**Name**](ischedulertask-name.md) task property.

</dd> <dt>

<span id="PropId_Task_ParentJobId"></span><span id="propid_task_parentjobid"></span><span id="PROPID_TASK_PARENTJOBID"></span>**PropId\_Task\_ParentJobId**
</dt> <dd>

Identifies the [**ParentJobId**](ischedulertask-parentjobid.md) task property.

</dd> <dt>

<span id="PropId_Task_PreviousState"></span><span id="propid_task_previousstate"></span><span id="PROPID_TASK_PREVIOUSSTATE"></span>**PropId\_Task\_PreviousState**
</dt> <dd>

Identifies the [**PreviousState**](ischedulertask-previousstate.md) task property.

</dd> <dt>

<span id="PropId_Task_RequeueCount"></span><span id="propid_task_requeuecount"></span><span id="PROPID_TASK_REQUEUECOUNT"></span>**PropId\_Task\_RequeueCount**
</dt> <dd>

Identifies the [**RequeueCount**](ischedulertask-requeuecount.md) task property.

</dd> <dt>

<span id="PropId_Task_RuntimeSeconds"></span><span id="propid_task_runtimeseconds"></span><span id="PROPID_TASK_RUNTIMESECONDS"></span>**PropId\_Task\_RuntimeSeconds**
</dt> <dd>

Identifies the [**Runtime**](ischedulertask-runtime.md) task property.

</dd> <dt>

<span id="PropId_Task_StartTime"></span><span id="propid_task_starttime"></span><span id="PROPID_TASK_STARTTIME"></span>**PropId\_Task\_StartTime**
</dt> <dd>

Identifies the [**StartTime**](ischedulertask-starttime.md) task property.

</dd> <dt>

<span id="PropId_Task_State"></span><span id="propid_task_state"></span><span id="PROPID_TASK_STATE"></span>**PropId\_Task\_State**
</dt> <dd>

Identifies the [**State**](ischedulertask-state.md) task property.

</dd> <dt>

<span id="PropId_Task_SubmitTime"></span><span id="propid_task_submittime"></span><span id="PROPID_TASK_SUBMITTIME"></span>**PropId\_Task\_SubmitTime**
</dt> <dd>

Identifies the [**SubmitTime**](ischedulertask-submittime.md) task property.

</dd> <dt>

<span id="PropId_Task_Type"></span><span id="propid_task_type"></span><span id="PROPID_TASK_TYPE"></span>**PropId\_Task\_Type**
</dt> <dd>

Identifies the [**Type**](ischedulertask-type.md) task property. This value is supported only for HPC Pack 2008 R2.

</dd> </dl>

## Requirements



|                         |                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.Properties.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IFilterCollection::Add**](ifiltercollection-add.md)
</dt> <dt>

[**ISortCollection::Add**](isortcollection-add.md)
</dt> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerNode**](ischedulernode.md)
</dt> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




