---
Description: 'Beginning with Microsoft&\#160;HPC&\#160;Pack&\#160;2008&\#160;R2 with Service Pack 2 (SP2), Microsoft HPC Pack provides access to the HPC Job Scheduler Service by using an HTTP web service that is based on the representational state transfer (REST) model.&\#160;HPC&\#160;Pack, including HPC Pack 2012, HPC Pack 2012 R2, and HPC Pack 2016, provide additional operations that provide information about nodes and node groups, and that allow you to create and manage SOA sessions, SOA requests, and SOA responses.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'DDBF2623-DFD7-4C93-A873-BBC2C2AEA13A'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: HPC Web Service API Reference
---

# HPC Web Service API Reference

Beginning with Microsoft HPC Pack 2008 R2 with Service Pack 2 (SP2), Microsoft HPC Pack provides access to the HPC Job Scheduler Service by using an HTTP web service that is based on the representational state transfer (REST) model.

Later versions of Microsoft HPC Pack, including HPC Pack 2012, HPC Pack 2012 R2, and HPC Pack 2016, provide additional operations that provide information about nodes and node groups, and that allow you to create and manage SOA sessions, SOA requests, and SOA responses.

The HPC REST API defines a number of operations that you can perform, including the information that is expected in the HTTP requests that you send to the HPC REST web service and that is provided in the HTTP responses that you receive in return as part of each operation.

> [!Note]
>
> The HPC REST API does not define the manner in which you create and send these HTTP requests and process the HTTP responses. The approach you can use to work with the HTTP requests and responses varies depending on the programming language that you use, and can also vary depending on the libraries or other tools that you choose to install to work with HTTP requests and responses in your programming language of choice. Additional information about working with the HTTP requests and responses is beyond the scope of this documentation. For an example of how to work with HTTP requests and responses for operations in the HPC REST API, see [Creating and Submitting Jobs by Using the REST API in Microsoft HPC Pack](http://social.technet.microsoft.com/wiki/contents/articles/7737.creating-and-submitting-jobs-by-using-the-rest-api-in-windows-hpc-server-2008-r2.aspx).

 

For certain operations (starting the Microsoft HPC Pack 2008 R2 with Service Pack 3 (SP3)), the api-version URI parameter or request header is required to use functionality that is available as of a certain version of Microsoft HPC Pack. The following table lists the values of the api-version parameter that correspond to versions of HPC Pack.



| Version of HPC Pack                            | Value of api-version      |
|------------------------------------------------|---------------------------|
| HPC Pack 2012, HPC Pack 2012 R2, HPC Pack 2016 | 2012-11-01.4.0            |
| HPC Pack 2008 R2 with SP4                      | 2012-03-31.3.4            |
| HPC Pack 2008 R2 with SP3                      | 2011-11-01<br/>     |
| HPC Pack 2008 R2 with SP2                      | Not available.<br/> |



 

The following table shows the operations that are available in the REST API both when the REST web service is hosted in an on-premises cluster, and when the REST web service is hosted in Azure.



| Operation                                                                          | Description                                                                                                                                                  |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add Task**](schedulerwebservice--addtask.md)                                   | Adds a task to a job.<br/>                                                                                                                             |
| [**Cancel Job**](cancel-job.md)                                                   | Cancels the specified job.<br/>                                                                                                                        |
| [**Cancel Subtask**](schedulerwebservice--cancelsubtask.md)                       | Cancels the specified subtask.<br/>                                                                                                                    |
| [**Cancel Task**](schedulerwebservice--canceltask.md)                             | Cancels the specified task.<br/>                                                                                                                       |
| [**Create Job**](schedulerwebservice--createjob.md)                               | Creates a new job on the HPC cluster, for which the specified properties have the specified values.<br/>                                               |
| [**Create Job From XML**](schedulerwebservice--createjobfromxml.md)               | Creates a new job on the HPC cluster by using the information in the specified job XML.<br/>                                                           |
| [**Get Active Head Node**](get-active-head-node.md)                               | Gets the name of the active head node of the HPC cluster. Supported beginning with Microsoft HPC Pack 2008 R2 with SP4.<br/>                           |
| [**Get Clusters**](get-clusters.md)                                               | Gets the name of the cluster that hosts the instance of the REST web service. Supported beginning with Microsoft HPC Pack 2008 R2 with SP3.<br/>       |
| [**Get Job**](schedulerwebservice--getjob.md)                                     | Gets information about the specified job.<br/>                                                                                                         |
| [**Get Job Custom Properties**](schedulerwebservice--getcustomproperties.md)      | Gets the values of the specified custom properties for the job, or the values of all of the properties if none are specified.<br/>                     |
| [**Get Job Environment Variables**](schedulerwebservice--getenvvariables.md)      | Gets the values of the specified environment variables for the job, or the values of all of the environment variables if none are specified.<br/>      |
| [**Get Job List**](schedulerwebservice--getjoblist.md)                            | Gets the values of the specified properties for all jobs for the HPC cluster, or optionally for jobs filtered by job owner or job state.<br/>          |
| [**Get Job Templates**](get-job-templates.md)                                     | Gets a list of the names of the job templates that are available on the HPC cluster.<br/>                                                              |
| [**Get Node**](get-node.md)                                                       | Gets the values of all of the properties for the specified node. Supported beginning with Microsoft HPC Pack 2008 R2 with SP3.<br/>                    |
| [**Get Node Group List**](get-node-group-list.md)                                 | Gets the names and descriptions for all of the node groups for the HPC cluster. Supported beginning with Microsoft HPC Pack 2008 R2 with SP3.<br/>     |
| [**Get Node Group Members**](get-node-group.md)                                   | Gets the list of the nodes that belong to the specified node group. Supported beginning with Microsoft HPC Pack 2008 R2 with SP3.<br/>                 |
| [**Get Node List**](get-node-list.md)                                             | Gets the values of the specified properties for all of the nodes in an HPC cluster. Supported beginning with Microsoft HPC Pack 2008 R2 with SP3.<br/> |
| [**Get Subtask**](schedulerwebservice--getsubtask.md)                             | Gets the values of the specified properties for the specified subtask, or the values of all of the properties if no properties are specified.<br/>     |
| [**Get Task**](schedulerwebservice--gettask.md)                                   | Gets the values of the specified properties for the specified task, or the values of all of the properties if no properties are specified.<br/>        |
| [**Get Task Custom Properties**](get-task-custom-properties.md)                   | Gets the values of the specified custom properties for the task, or the values of all of the properties if none are specified.<br/>                    |
| [**Get Task Environment Variables**](schedulerwebservice--gettaskenvvariables.md) | Gets the values of the specified environment variables for the task, or the values of all of the environment variables if none are specified.<br/>     |
| [**Get Task List**](schedulerwebservice--gettasklist.md)                          | Gets the values of the properties for all of the tasks in the specified job.<br/>                                                                      |
| [**Get Version**](get-version.md)                                                 | Gets the version of Microsoft HPC Pack that is installed on the HPC cluster that hosts the web service.<br/>                                           |
| [**Requeue Job**](schedulerwebservice--requeuejob.md)                             | Resubmits the specified job to the queue.<br/>                                                                                                         |
| [**Requeue Subtask**](schedulerwebservice--requeuesubtask.md)                     | Moves a failed, canceled, or queued subtask to the configuring state so that the subtask can be queued again when the job is resubmitted.<br/>         |
| [**Requeue Task**](schedulerwebservice--requeuetask.md)                           | Moves a failed, canceled, or queued task to the configuring state so that the task can be queued again when the job is resubmitted.<br/>               |
| [**Set Job Custom Properties**](schedulerwebservice--setcustomproperties.md)      | Sets the values of custom properties for a job.<br/>                                                                                                   |
| [**Set Job Environment Variables**](schedulerwebservice--setenvvariables.md)      | Sets the value of one or more environment variables for a job.<br/>                                                                                    |
| [**Set Job Properties**](schedulerwebservice--setjobproperties.md)                | Sets the values for the properties of the specified job.<br/>                                                                                          |
| [**Set Subtask Properties**](set-subtask-properties.md)                           | Sets the values of properties for the task that contains that specified subtask.<br/>                                                                  |
| [**Set Task Custom Properties**](set-task-custom-properties.md)                   | Sets the values of custom properties for a task.<br/>                                                                                                  |
| [**Set Task Environment Variables**](schedulerwebservice--settaskenvvariables.md) | Sets the value of one or more environment variables for a task.<br/>                                                                                   |
| [**Set Task Properties**](schedulerwebservice--settaskproperties.md)              | Sets the values of properties for a task in a job.<br/>                                                                                                |
| [**Submit Job**](schedulerwebservice--submitjob.md)                               | Submits a job to the HPC Job Scheduler Service so that the HPC Job Scheduler Service can add the job to the queue of jobs to run.<br/>                 |



 

The following table shows the operations that are available only when the REST web service is hosted in Windows Azure. All of the operations are supported starting with Microsoft HPC Pack 2008 R2 with SP3.



| Operation                                                            | Description                                                                                                                              |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [**Attach to Session**](attach-to-session.md)                       | Connects to an existing SOA session.<br/>                                                                                          |
| [**Close Session**](close-session.md)                               | Closes a SOA session, which ends the job for the session and deletes the response messages.<br/>                                   |
| [**Create Session**](create-session.md)                             | Creates a new service-oriented architecture (SOA) session with the specified configuration information.<br/>                       |
| [**Delete Requests**](remove-a-batch-of-requests.md)                | Deletes a batch of SOA requests that you previously sent.<br/>                                                                     |
| [**Get Responses**](get-all-repsonses-to-a-batch-of-requests.md)    | Gets the responses that the service-oriented architecture (SOA) service returned for the SOA requests in the specified batch.<br/> |
| [**Get Request Status**](get-the-status-of-a-batch-of-requests.md)  | Gets the status of a batch of SOA requests.<br/>                                                                                   |
| [**Indicate the End of Requests**](indicate-the-end-of-requests.md) | Indicates that you are finish sending SOA requests and that the broker should commit all requests.<br/>                            |
| [**Send Requests**](send-a-batch-of-requests.md)                    | Sends a batch of SOA requests to the SOA service that you specified when you created the session.<br/>                             |



 

 

 




