---
Description: 'Defines a task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b323b39a-a9c3-420c-9a38-e3d3761a0482'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ISchedulerTask interface
---

# ISchedulerTask interface

Defines a task.

To create a task, call the [**ISchedulerJob::CreateTask**](ischedulerjob-createtask.md) method.

## Members

The **ISchedulerTask** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ISchedulerTask** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ISchedulerTask** interface has these methods.



| Method                                                                  | Description                                                                                                                                                             |
|:------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Commit**](ischedulertask-commit.md)                                 | Commits the local task changes to the server.<br/>                                                                                                                |
| [**GetCounters**](ischedulertask-getcounters.md)                       | Retrieves the counter data for the task.<br/>                                                                                                                     |
| [**GetCustomProperties**](ischedulertask-getcustomproperties.md)       | Retrieves the application-defined properties that were added to the task.<br/>                                                                                    |
| [**Refresh**](ischedulertask-refresh.md)                               | Refreshes this copy of the task with the contents from the server.<br/>                                                                                           |
| [**ServiceConclude**](ischedulertask-serviceconclude.md)               | Directs the HPC Job Scheduler Service to stop starting subtasks for a service task.<br/> This method is supported only for Windows HPC Server 2008 R2.<br/> |
| [**SetCustomProperty**](ischedulertask-setcustomproperty.md)           | Sets an application-defined property on the task.<br/>                                                                                                            |
| [**SetEnvironmentVariable**](ischedulertask-setenvironmentvariable.md) | Sets a task-specific environment variable.<br/>                                                                                                                   |



 

### Properties

The **ISchedulerTask** interface has these properties.



| Property                                                                           | Access type           | Description                                                                                                                                                                                                                     |
|:-----------------------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AllocatedCoreIds**](ischedulertask-allocatedcoreids.md)<br/>             | Read-only<br/>  | Retrieves the identifiers of the processor cores that have been allocated to run the task or that have run the task.<br/> This property is supported only for Windows HPC Server 2008 R2.<br/>                      |
| [**AllocatedNodes**](ischedulertask-allocatednodes.md)<br/>                 | Read-only<br/>  | Retrieves the names of the nodes that have been allocated to run the task or have run the task.<br/>                                                                                                                      |
| [**ChangeTime**](ischedulertask-changetime.md)<br/>                         | Read-only<br/>  | Retrieves the last time that the user or server changed a property of the task.<br/>                                                                                                                                      |
| [**CommandLine**](ischedulertask-commandline.md)<br/>                       | Read/write<br/> | Retrieves or sets the command line for the task.<br/>                                                                                                                                                                     |
| [**CreateTime**](ischedulertask-createtime.md)<br/>                         | Read-only<br/>  | Retrieves the date and time when the task was created.<br/>                                                                                                                                                               |
| [**DependsOn**](ischedulertask-dependson.md)<br/>                           | Read/write<br/> | Retrieves or sets the dependent tasks.<br/>                                                                                                                                                                               |
| [**EndTime**](ischedulertask-endtime.md)<br/>                               | Read-only<br/>  | Retrieves the date and time that the task ended.<br/>                                                                                                                                                                     |
| [**EndValue**](ischedulertask-endvalue.md)<br/>                             | Read/write<br/> | Retrieves or sets the ending value for a parametric task.<br/>                                                                                                                                                            |
| [**EnvironmentVariables**](ischedulertask-environmentvariables.md)<br/>     | Read-only<br/>  | Retrieves the environment variables that were set for the task.<br/>                                                                                                                                                      |
| [**ErrorMessage**](ischedulertask-errormessage.md)<br/>                     | Read-only<br/>  | Retrieves the task error message.<br/>                                                                                                                                                                                    |
| [**ExitCode**](ischedulertask-exitcode.md)<br/>                             | Read-only<br/>  | Retrieves the exit code for the task.<br/>                                                                                                                                                                                |
| [**FailJobOnFailure**](ischedulertask-failjobonfailure.md)<br/>             | Read/write<br/> | Determines whether the task is critical for the job. If a task is critical for the job, the job and its tasks stop running and the job is immediately marked as failed if the task fails.<br/>                            |
| [**FailJobOnFailureCount**](ischedulertask-failjobonfailurecount.md)<br/>   | Read/write<br/> | Retrieves or sets the number of subtasks of a critical parametric sweep or service task that must fail before the job and its tasks and subtask should stop running and the task and job should be marked as failed.<br/> |
| [**HasRuntime**](ischedulertask-hasruntime.md)<br/>                         | Read/write<br/> | Determines whether the [**Runtime**](ischedulertask-runtime.md) task property is set.<br/>                                                                                                                               |
| [**IncrementValue**](ischedulertask-incrementvalue.md)<br/>                 | Read/write<br/> | Retrieves or sets the number by which to increment the instance value for a parametric task.<br/>                                                                                                                         |
| [**IsExclusive**](ischedulertask-isexclusive.md)<br/>                       | Read/write<br/> | Determines whether other tasks from the job can run on the node at the same time as this task.<br/>                                                                                                                       |
| [**IsParametric**](ischedulertask-isparametric.md)<br/>                     | Read/write<br/> | Determines whether the task is a parametric task.<br/>                                                                                                                                                                    |
| [**IsRerunnable**](ischedulertask-isrerunnable.md)<br/>                     | Read/write<br/> | Determines whether the task can rerun after a failure.<br/>                                                                                                                                                               |
| [**IsServiceConcluded**](ischedulertask-isserviceconcluded.md)<br/>         | Read-only<br/>  | Gets whether the HPC Job Scheduler Service has concluded starting subtasks for a service task.<br/> This property is supported only for Windows HPC Server 2008 R2.<br/>                                            |
| [**MaximumNumberOfCores**](ischedulertask-maximumnumberofcores.md)<br/>     | Read/write<br/> | Retrieves or sets the maximum number of cores that the task requires to run.<br/>                                                                                                                                         |
| [**MaximumNumberOfNodes**](ischedulertask-maximumnumberofnodes.md)<br/>     | Read/write<br/> | Retrieves or sets the maximum number of nodes that the task requires to run.<br/>                                                                                                                                         |
| [**MaximumNumberOfSockets**](ischedulertask-maximumnumberofsockets.md)<br/> | Read/write<br/> | Retrieves or sets the maximum number of sockets that the task requires to run.<br/>                                                                                                                                       |
| [**MinimumNumberOfCores**](ischedulertask-minimumnumberofcores.md)<br/>     | Read/write<br/> | Retrieves or sets the minimum number of cores that the task requires to run.<br/>                                                                                                                                         |
| [**MinimumNumberOfNodes**](ischedulertask-minimumnumberofnodes.md)<br/>     | Read/write<br/> | Retrieves or sets the minimum number of nodes that the task requires to run.<br/>                                                                                                                                         |
| [**MinimumNumberOfSockets**](ischedulertask-minimumnumberofsockets.md)<br/> | Read/write<br/> | Retrieves or sets the minimum number of sockets that the task requires to run.<br/>                                                                                                                                       |
| [**Name**](ischedulertask-name.md)<br/>                                     | Read/write<br/> | Retrieves or sets the display name of the task.<br/>                                                                                                                                                                      |
| [**Output**](ischedulertask-output.md)<br/>                                 | Read-only<br/>  | Retrieves the output from the command.<br/>                                                                                                                                                                               |
| [**ParentJobId**](ischedulertask-parentjobid.md)<br/>                       | Read-only<br/>  | Retrieves the identifier of the parent job.<br/>                                                                                                                                                                          |
| [**PreviousState**](ischedulertask-previousstate.md)<br/>                   | Read-only<br/>  | Retrieves the previous state of the task.<br/>                                                                                                                                                                            |
| [**RequeueCount**](ischedulertask-requeuecount.md)<br/>                     | Read-only<br/>  | Retrieves the number of times that the task has been queued. <br/>                                                                                                                                                        |
| [**RequiredNodes**](ischedulertask-requirednodes.md)<br/>                   | Read/write<br/> | Retrieves or sets the list of required nodes for the task.<br/>                                                                                                                                                           |
| [**Runtime**](ischedulertask-runtime.md)<br/>                               | Read/write<br/> | Retrieves or sets the run-time limit for the task.<br/>                                                                                                                                                                   |
| [**StartTime**](ischedulertask-starttime.md)<br/>                           | Read-only<br/>  | Retrieves the date and time that the job started running.<br/>                                                                                                                                                            |
| [**StartValue**](ischedulertask-startvalue.md)<br/>                         | Read/write<br/> | Retrieves or sets the starting instance value for a parametric task.<br/>                                                                                                                                                 |
| [**State**](ischedulertask-state.md)<br/>                                   | Read-only<br/>  | Retrieves the state of the task.<br/>                                                                                                                                                                                     |
| [**StdErrFilePath**](ischedulertask-stderrfilepath.md)<br/>                 | Read/write<br/> | Retrieves or sets the path to which the server redirects standard error.<br/>                                                                                                                                             |
| [**StdInFilePath**](ischedulertask-stdinfilepath.md)<br/>                   | Read/write<br/> | Retrieves or sets the path from which the server redirects standard input.<br/>                                                                                                                                           |
| [**StdOutFilePath**](ischedulertask-stdoutfilepath.md)<br/>                 | Read/write<br/> | Retrieves or sets the path to which the server redirects standard output.<br/>                                                                                                                                            |
| [**SubmitTime**](ischedulertask-submittime.md)<br/>                         | Read-only<br/>  | Retrieves the time that the task was submitted.<br/>                                                                                                                                                                      |
| [**TaskId**](ischedulertask-taskid.md)<br/>                                 | Read-only<br/>  | Retrieves the identifiers that uniquely identify the task.<br/>                                                                                                                                                           |
| [**Type**](ischedulertask-type.md)<br/>                                     | Read/write<br/> | Gets or sets a task type that defines how to run the command for the task.<br/> This property is supported only for Windows HPC Server 2008 R2.<br/>                                                                |
| [**UserBlob**](ischedulertask-userblob.md)<br/>                             | Read/write<br/> | Retrieves or sets the user data associated with the task.<br/>                                                                                                                                                            |
| [**ValidExitCodes**](ischedulertask-validexitcodes.md)<br/>                 | Read/write<br/> | Retrieves or sets the exit codes to be used for checking whether tasks in the job successfully exit.<br/>                                                                                                                 |
| [**WorkDirectory**](ischedulertask-workdirectory.md)<br/>                   | Read/write<br/> | Retrieves or sets the startup directory for the task.<br/>                                                                                                                                                                |



 

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack  2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                          |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerNode**](ischedulernode.md)
</dt> <dt>

[**ISchedulerTaskCounters**](ischedulertaskcounters.md)
</dt> </dl>

 

 




