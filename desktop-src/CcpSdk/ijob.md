---
Description: 'Manages the tasks and resources that are associated with a job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c7e6b630-b09e-4f86-aa49-d07c37793b10'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: IJob interface
---

# IJob interface

Manages the tasks and resources that are associated with a job.

To create a job, call the [**ICluster::CreateJob**](icluster-createjob.md) method.

## Members

The **IJob** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IJob** also has these types of members:

-   [Methods](#methods)

### Methods

The **IJob** interface has these methods.



| Method                                                                       | Description                                                                                                                         |
|:-----------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| [**AddTask**](ijob-addtask.md)                                              | Adds the task to the job.<br/>                                                                                                |
| [**Clear**](ijob-clear.md)                                                  | Removes all tasks from the job.<br/>                                                                                          |
| [**get\_AskedNodes**](ijob-get-askednodes.md)                               | Retrieves the list of nodes that are requested for the job.<br/>                                                              |
| [**get\_CreateTime**](ijob-get-createtime.md)                               | Retrieves the job creation time.<br/>                                                                                         |
| [**get\_EndTime**](ijob-get-endtime.md)                                     | Retrieves the job end time.<br/>                                                                                              |
| [**get\_ErrorMessage**](ijob-get-errormessage.md)                           | Retrieves the job error message.<br/>                                                                                         |
| [**get\_ExtendedJobTerms**](ijob-get-extendedjobterms.md)                   | Retrieves the extended job terms.<br/>                                                                                        |
| [**get\_Id**](ijob-get-id.md)                                               | Retrieves the job identifier.<br/>                                                                                            |
| [**get\_IsBackfill**](ijob-get-isbackfill.md)                               | Checks whether the job is running as a backfill job.<br/>                                                                     |
| [**get\_IsExclusive**](ijob-get-isexclusive.md)                             | Checks whether nodes should be exclusively allocated to the job.<br/>                                                         |
| [**get\_MaximumNumberOfProcessors**](ijob-get-maximumnumberofprocessors.md) | Retrieves the maximum number of processors that are required by the job.<br/>                                                 |
| [**get\_MinimumNumberOfProcessors**](ijob-get-minimumnumberofprocessors.md) | Retrieves the minimum number of processors that are required by the job.<br/>                                                 |
| [**get\_Name**](ijob-get-name.md)                                           | Retrieves the display name of the job.<br/>                                                                                   |
| [**get\_Priority**](ijob-get-priority.md)                                   | Retrieves the job priority.<br/>                                                                                              |
| [**get\_Project**](ijob-get-project.md)                                     | Retrieves the project name that is associated with the job.<br/>                                                              |
| [**get\_Runtime**](ijob-get-runtime.md)                                     | Retrieves the run-time limit for the job.<br/>                                                                                |
| [**get\_RunUntilCanceled**](ijob-get-rununtilcanceled.md)                   | Checks whether the resources that are allocated to a job are reserved for the job even when the job has no active tasks.<br/> |
| [**get\_SoftwareLicense**](ijob-get-softwarelicense.md)                     | Retrieves information about the required licenses.<br/>                                                                       |
| [**get\_StartTime**](ijob-get-starttime.md)                                 | Retrieves the time that the job started running.<br/>                                                                         |
| [**get\_Status**](ijob-get-status.md)                                       | Retrieves the current job status.<br/>                                                                                        |
| [**get\_SubmittedBy**](ijob-get-submittedby.md)                             | Retrieves the name of the user who submitted the job.<br/>                                                                    |
| [**get\_SubmitTime**](ijob-get-submittime.md)                               | Retrieves the time that the job was submitted.<br/>                                                                           |
| [**get\_TaskCount**](ijob-get-taskcount.md)                                 | Retrieves the number of tasks that are part of the job.<br/>                                                                  |
| [**get\_User**](ijob-get-user.md)                                           | Retrieves the RunAs user for the job.<br/>                                                                                    |
| [**GetEnumerator**](ijob-getenumerator.md)                                  | Retrieves an enumerator that you use to enumerate the tasks of the job.<br/>                                                  |
| [**GetTask**](ijob-gettask.md)                                              | Retrieves the specified task.<br/>                                                                                            |
| [**put\_AskedNodes**](ijob-put-askednodes.md)                               | Sets the list of nodes that are requested for the job.<br/>                                                                   |
| [**put\_IsExclusive**](ijob-put-isexclusive.md)                             | Sets whether nodes should be exclusively allocated to the job.<br/>                                                           |
| [**put\_MaximumNumberOfProcessors**](ijob-put-maximumnumberofprocessors.md) | Sets the maximum number of processors that are required by the job.<br/>                                                      |
| [**put\_MinimumNumberOfProcessors**](ijob-put-minimumnumberofprocessors.md) | Sets the minimum number of processors that are required by the job.<br/>                                                      |
| [**put\_Name**](ijob-put-name.md)                                           | Sets the display name of the job.<br/>                                                                                        |
| [**put\_Priority**](ijob-put-priority.md)                                   | Sets the job priority.<br/>                                                                                                   |
| [**put\_Project**](ijob-put-project.md)                                     | Sets the project name that is associated with the job.<br/>                                                                   |
| [**put\_Runtime**](ijob-put-runtime.md)                                     | Sets the run-time limit for the job.<br/>                                                                                     |
| [**put\_RunUntilCanceled**](ijob-put-rununtilcanceled.md)                   | Sets whether the resources that are allocated to a job are reserved for the job even when the job has no active tasks.<br/>   |
| [**put\_SoftwareLicense**](ijob-put-softwarelicense.md)                     | Sets the required licenses.<br/>                                                                                              |
| [**put\_User**](ijob-put-user.md)                                           | Sets the RunAs user for the job.<br/>                                                                                         |
| [**SetExtendedJobTerm**](ijob-setextendedjobterm.md)                        | Sets the specified extended job term.<br/>                                                                                    |



 

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[Jobs and Tasks](jobs-and-tasks.md)
</dt> <dt>

[CCP Interfaces](interfaces.md)
</dt> </dl>

 

 




