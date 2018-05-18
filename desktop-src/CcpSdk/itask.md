---
Description: 'Defines a task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3118a416-14d8-4d38-a8c8-e5e7e985aeef'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ITask interface
---

# ITask interface

Defines a task.

To create a task, call the [**ICluster::CreateTask**](icluster-createtask.md) method.

## Members

The **ITask** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ITask** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITask** interface has these methods.



| Method                                                                        | Description                                                                     |
|:------------------------------------------------------------------------------|:--------------------------------------------------------------------------------|
| [**get\_CommandLine**](itask-get-commandline.md)                             | Retrieves the command line for the task.<br/>                             |
| [**get\_CreateTime**](itask-get-createtime.md)                               | Retrieves the task creation time.<br/>                                    |
| [**get\_Depend**](itask-get-depend.md)                                       | Retrieves the dependent tasks.<br/>                                       |
| [**get\_EndTime**](itask-get-endtime.md)                                     | Retrieves the task end time.<br/>                                         |
| [**get\_EnvironmentVariables**](itask-get-environmentvariables.md)           | Retrieves the environment variables for the task.<br/>                    |
| [**get\_ErrorMessage**](itask-get-errormessage.md)                           | Retrieves the task error message.<br/>                                    |
| [**get\_ExitCode**](itask-get-exitcode.md)                                   | Retrieves the exit code for the task.<br/>                                |
| [**get\_ExtendedTaskTerms**](itask-get-extendedtaskterms.md)                 | Retrieves the application-defined extended terms for the task.<br/>       |
| [**get\_Id**](itask-get-id.md)                                               | Retrieves the task identifier.<br/>                                       |
| [**get\_IsExclusive**](itask-get-isexclusive.md)                             | Checks whether the node should be exclusively allocated to the task.<br/> |
| [**get\_IsRerunnable**](itask-get-isrerunnable.md)                           | Checks whether the task can be rerun after a failure.<br/>                |
| [**get\_MaximumNumberOfProcessors**](itask-get-maximumnumberofprocessors.md) | Retrieves the maximum number of processors required by the task.<br/>     |
| [**get\_MinimumNumberOfProcessors**](itask-get-minimumnumberofprocessors.md) | Retrieves the minimum number of processors required by the task.<br/>     |
| [**get\_Name**](itask-get-name.md)                                           | Retrieves the display name of the task.<br/>                              |
| [**get\_ParentJobId**](itask-get-parentjobid.md)                             | Retrieves the identifier of the parent job.<br/>                          |
| [**get\_RequiredNodes**](itask-get-requirednodes.md)                         | Retrieves the list of required nodes for the task.<br/>                   |
| [**get\_Runtime**](itask-get-runtime.md)                                     | Retrieves the run-time limit for the task.<br/>                           |
| [**get\_StartTime**](itask-get-starttime.md)                                 | Retrieves the time that the task started running.<br/>                    |
| [**get\_Status**](itask-get-status.md)                                       | Retrieves the task status.<br/>                                           |
| [**get\_Stderr**](itask-get-stderr.md)                                       | Retrieves the file to which standard error has been redirected.<br/>      |
| [**get\_Stdin**](itask-get-stdin.md)                                         | Retrieves the file from which standard input has been redirected.<br/>    |
| [**get\_Stdout**](itask-get-stdout.md)                                       | Retrieves the file to which standard output has been redirected.<br/>     |
| [**get\_SubmitTime**](itask-get-submittime.md)                               | Retrieves the time that the task was submitted.<br/>                      |
| [**get\_WorkDirectory**](itask-get-workdirectory.md)                         | Retrieves the startup directory for the task.<br/>                        |
| [**put\_CommandLine**](itask-put-commandline.md)                             | Sets the command line for the task.<br/>                                  |
| [**put\_Depend**](itask-put-depend.md)                                       | Sets the dependent tasks.<br/>                                            |
| [**put\_IsExclusive**](itask-put-isexclusive.md)                             | Sets whether the node should be exclusively allocated to the task.<br/>   |
| [**put\_IsRerunnable**](itask-put-isrerunnable.md)                           | Sets whether the task can be rerun after a failure.<br/>                  |
| [**put\_MaximumNumberOfProcessors**](itask-put-maximumnumberofprocessors.md) | Sets the maximum number of processors required by the task.<br/>          |
| [**put\_MinimumNumberOfProcessors**](itask-put-minimumnumberofprocessors.md) | Sets the minimum number of processors required by the task.<br/>          |
| [**put\_Name**](itask-put-name.md)                                           | Sets the display name of the task.<br/>                                   |
| [**put\_RequiredNodes**](itask-put-requirednodes.md)                         | Sets the list of required nodes for the task.<br/>                        |
| [**put\_Runtime**](itask-put-runtime.md)                                     | Sets the run-time limit for the task.<br/>                                |
| [**put\_Stderr**](itask-put-stderr.md)                                       | Redirects standard error to the specified file.<br/>                      |
| [**put\_Stdin**](itask-put-stdin.md)                                         | Redirects standard input to the specified file.<br/>                      |
| [**put\_Stdout**](itask-put-stdout.md)                                       | Redirects standard output to the specified file.<br/>                     |
| [**put\_WorkDirectory**](itask-put-workdirectory.md)                         | Sets the startup directory for the task.<br/>                             |
| [**SetEnvironmentVariable**](itask-setenvironmentvariable.md)                | Sets the task-specific environment variable.<br/>                         |
| [**SetExtendedTaskTerm**](itask-setextendedtaskterm.md)                      | Sets the application-defined extended term for the task.<br/>             |



 

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Header<br/>       | <dl> <dt>Mstask.h</dt> </dl>   |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[Jobs and Tasks](jobs-and-tasks.md)
</dt> <dt>

[CCP Interfaces](interfaces.md)
</dt> </dl>

 

 




