---
Description: 'Defines methods to manage the nodes, jobs, and tasks in a compute cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '34662f1a-6615-4e0b-a5a6-99c4a9d27c8e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ICluster interface
---

# ICluster interface

Defines methods to manage the nodes, jobs, and tasks in a compute cluster.

To create an instance of this interface, call the [**CoCreateInstance**](_com_cocreateinstance) function. Use CLSID\_Cluster as the class identifier and IID\_ICluster as the interface identifier. For an example, see [Creating the Cluster Object](creating-the-cluster-object.md).

## Members

The **ICluster** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ICluster** also has these types of members:

-   [Methods](#methods)

### Methods

The **ICluster** interface has these methods.



| Method                                                                    | Description                                                                                                                                                                                                             |
|:--------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddJob**](icluster-addjob.md)                                         | Adds the specified job to the cluster.<br/>                                                                                                                                                                       |
| [**AddJobs**](icluster-addjobs.md)                                       | Adds one or more specified jobs to the cluster.<br/>                                                                                                                                                              |
| [**AddTask**](icluster-addtask.md)                                       | Adds the specified task to the specified job.<br/>                                                                                                                                                                |
| [**AddTasks**](icluster-addtasks.md)                                     | Adds one or more specified tasks to the specified job.<br/>                                                                                                                                                       |
| [**ApproveNode**](icluster-approvenode.md)                               | Approves the addition of the specified node to the cluster.<br/>                                                                                                                                                  |
| [**CancelJob**](icluster-canceljob.md)                                   | Cancels the specified job.<br/>                                                                                                                                                                                   |
| [**CancelJobs**](icluster-canceljobs.md)                                 | Cancels one or more specified jobs.<br/>                                                                                                                                                                          |
| [**CancelTask**](icluster-canceltask.md)                                 | Cancels the specified task.<br/>                                                                                                                                                                                  |
| [**CancelTasks**](icluster-canceltasks.md)                               | Cancels one or more specified tasks.<br/>                                                                                                                                                                         |
| [**CheckAnyTask**](icluster-checkanytask.md)                             | Checks which tasks for the job have finished, failed, or been canceled.<br/>                                                                                                                                      |
| [**Connect**](icluster-connect.md)                                       | Connects to the specified cluster.<br/>                                                                                                                                                                           |
| [**CreateClusterEnumerable**](icluster-createclusterenumerable.md)       | Creates an enumerable object.<br/>                                                                                                                                                                                |
| [**CreateJob**](icluster-createjob.md)                                   | Creates a job.<br/>                                                                                                                                                                                               |
| [**CreateJobFromXml**](icluster-createjobfromxml.md)                     | Creates a job using the specified XML document.<br/>                                                                                                                                                              |
| [**CreateJobFromXmlFile**](icluster-createjobfromxmlfile.md)             | Creates a job using the specified XML file.<br/>                                                                                                                                                                  |
| [**CreateTask**](icluster-createtask.md)                                 | Creates a task.<br/>                                                                                                                                                                                              |
| [**CreateTaskFromXml**](icluster-createtaskfromxml.md)                   | Creates a task using the specified XML document.<br/>                                                                                                                                                             |
| [**CreateTaskFromXmlFile**](icluster-createtaskfromxmlfile.md)           | Creates a task using the specified XML file.<br/>                                                                                                                                                                 |
| [**DeleteCachedCredentials**](icluster-deletecachedcredentials.md)       | Deletes the specified user's credentials from the cache.<br/>                                                                                                                                                     |
| [**EndCommand**](icluster-endcommand.md)                                 | Cancels the specified command on all nodes.<br/>                                                                                                                                                                  |
| [**ExecuteCommand**](icluster-executecommand.md)                         | Executes a task on a specified group of nodes in the cluster.<br/>                                                                                                                                                |
| [**ExecuteCommandWithPaging**](icluster-executecommandwithpaging.md)     | Executes a task on a specified group of nodes in the cluster. The output is returned in the requested page size.<br/>                                                                                             |
| [**get\_ClusterCounter**](icluster-get-clustercounter.md)                | Retrieves counter information for the cluster.<br/>                                                                                                                                                               |
| [**get\_ComputeNodes**](icluster-get-computenodes.md)                    | Retrieves the list of compute nodes in the cluster.<br/>                                                                                                                                                          |
| [**get\_EnvironmentVariables**](icluster-get-environmentvariables.md)    | Retrieves the cluster-wide environment variables.<br/>                                                                                                                                                            |
| [**get\_ErrorMessage**](icluster-get-errormessage.md)                    | Retrieves a description of the error that occurred when a method of the **ICluster** interface failed.<br/>                                                                                                       |
| [**get\_IsAsynchronous**](icluster-get-isasynchronous.md)                | Determines whether calls to the server are executed asynchronously.<br/>                                                                                                                                          |
| [**get\_Name**](icluster-get-name.md)                                    | Retrieves the display name of the cluster.<br/>                                                                                                                                                                   |
| [**get\_Parameters**](icluster-get-parameters.md)                        | Retrieves the cluster's configuration parameters.<br/>                                                                                                                                                            |
| [**get\_Timeout**](icluster-get-timeout.md)                              | Retrieves the maximum time that the application will wait for a response from the cluster when making synchronous calls.<br/>                                                                                     |
| [**GetJob**](icluster-getjob.md)                                         | Retrieves a job from the cluster.<br/>                                                                                                                                                                            |
| [**GetJobCounter**](icluster-getjobcounter.md)                           | Retrieves counter information for a specified job.<br/>                                                                                                                                                           |
| [**GetJobResourceUsage**](icluster-getjobresourceusage.md)               | Retrieves the resource usage information for the specified job.<br/>                                                                                                                                              |
| [**GetNewCommandId**](icluster-getnewcommandid.md)                       | Gets a command identifier that is used to execute a command.<br/>                                                                                                                                                 |
| [**GetTask**](icluster-gettask.md)                                       | Retrieves the task from the specified job.<br/>                                                                                                                                                                   |
| [**GetTaskResourceUsage**](icluster-gettaskresourceusage.md)             | Retrieves the resource usage information for the specified task.<br/>                                                                                                                                             |
| [**IsAdmin**](icluster-isadmin.md)                                       | Determines whether the user is a member of the cluster's Administrators group.<br/>                                                                                                                               |
| [**ListAllJobs**](icluster-listalljobs.md)                               | Retrieves all jobs in the cluster.<br/>                                                                                                                                                                           |
| [**ListAllJobsWithPaging**](icluster-listalljobswithpaging.md)           | Retrieves all jobs in the cluster. The jobs are returned in blocks of jobs from a specified snapshot of the cluster.<br/>                                                                                         |
| [**ListJobs**](icluster-listjobs.md)                                     | Retrieves all jobs in the cluster that were submitted by the specified owner and that have the specified status.<br/>                                                                                             |
| [**ListJobsOnNode**](icluster-listjobsonnode.md)                         | Retrieves all jobs that are running on the specified node.<br/>                                                                                                                                                   |
| [**ListJobsWithPaging**](icluster-listjobswithpaging.md)                 | Retrieves all jobs in the cluster that were submitted by the specified owner and that have the specified status. The jobs are returned in blocks of jobs from a specified snapshot of the cluster.<br/>           |
| [**ListTasks**](icluster-listtasks.md)                                   | Retrieves all tasks in the specified job.<br/>                                                                                                                                                                    |
| [**ListTasksOnNode**](icluster-listtasksonnode.md)                       | Retrieves a list of all tasks running on the node.<br/>                                                                                                                                                           |
| [**ListTasksWithPaging**](icluster-listtaskswithpaging.md)               | Retrieves all tasks in the specified job. The tasks are returned in blocks of tasks from a specified snapshot of the job.<br/>                                                                                    |
| [**ModifyJob**](icluster-modifyjob.md)                                   | Modifies the specified job.<br/>                                                                                                                                                                                  |
| [**ModifyJobTerm**](icluster-modifyjobterm.md)                           | Modifies the specified job term.<br/>                                                                                                                                                                             |
| [**PauseNode**](icluster-pausenode.md)                                   | Prevents the scheduler from starting new jobs and tasks on the specified node until the [**ICluster::ResumeNode**](icluster-resumenode.md) method is called; existing jobs and tasks will continue to run. <br/> |
| [**put\_IsAsynchronous**](icluster-put-isasynchronous.md)                | Sets whether calls to the server are executed asynchronously.<br/>                                                                                                                                                |
| [**put\_Timeout**](icluster-put-timeout.md)                              | Sets the maximum time that the application will wait for a response from the cluster when making synchronous calls.<br/>                                                                                          |
| [**QueueJob**](icluster-queuejob.md)                                     | Adds the specified job to the cluster and scheduling queue.<br/>                                                                                                                                                  |
| [**QueueJobs**](icluster-queuejobs.md)                                   | Adds one or more specified jobs to the cluster and scheduling queue.<br/>                                                                                                                                         |
| [**ReadExecutionResult**](icluster-readexecutionresult.md)               | Retrieves the output from a command.<br/>                                                                                                                                                                         |
| [**RequeueJob**](icluster-requeuejob.md)                                 | Queues the specified job again.<br/>                                                                                                                                                                              |
| [**RequeueJobs**](icluster-requeuejobs.md)                               | Queues one or more specified jobs again.<br/>                                                                                                                                                                     |
| [**RequeueTask**](icluster-requeuetask.md)                               | Queues the specified task again.<br/>                                                                                                                                                                             |
| [**RequeueTasks**](icluster-requeuetasks.md)                             | Queues one or more specified tasks again.<br/>                                                                                                                                                                    |
| [**ResumeNode**](icluster-resumenode.md)                                 | Resumes scheduling new jobs and tasks on the specified node. <br/>                                                                                                                                                |
| [**SetCachedCredentials**](icluster-setcachedcredentials.md)             | Sets the credentials for the specified user in the credential cache.<br/>                                                                                                                                         |
| [**SetClusterParameter**](icluster-setclusterparameter.md)               | Sets a configuration parameter for the cluster.<br/>                                                                                                                                                              |
| [**SetEnvironmentVariable**](icluster-setenvironmentvariable.md)         | Sets a cluster-wide environment variable.<br/>                                                                                                                                                                    |
| [**SetJobCredentials**](icluster-setjobcredentials.md)                   | Sets the credentials for the specified job.<br/>                                                                                                                                                                  |
| [**SetJobCredentialsFromCache**](icluster-setjobcredentialsfromcache.md) | Sets the credentials for the specified job using credentials from the credential cache.<br/>                                                                                                                      |
| [**SubmitJob**](icluster-submitjob.md)                                   | Adds the specified job to the scheduling queue.<br/>                                                                                                                                                              |
| [**SubmitJobs**](icluster-submitjobs.md)                                 | Adds one or more specified jobs to the scheduling queue.<br/>                                                                                                                                                     |
| [**WaitForCommand**](icluster-waitforcommand.md)                         | Waits for execution of the command to be completed on at least one node.<br/>                                                                                                                                     |
| [**WaitForCommandWithPaging**](icluster-waitforcommandwithpaging.md)     | Waits for execution of the specified command to be completed on at least one node. The output is returned in the requested page size.<br/>                                                                        |



 

## Remarks

After creating an instance of this interface, call the [**Connect**](icluster-connect.md) method to [connect to the cluster](connecting-to-the-cluster.md). You can then [create and schedule jobs](submitting-a-job-to-the-scheduling-queue.md) and tasks on the cluster.

To create the Cluster object in a script, use Microsoft.ComputeCluster.Cluster as the program identifier when calling the [CreateObject](https://msdn.microsoft.com/library/xzysf6hc.aspx) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[CCP Interfaces](interfaces.md)
</dt> <dt>

[Compute Cluster Architecture](compute-cluster-architecture.md)
</dt> </dl>

 

 




