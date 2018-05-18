---
Description: 'Defines the methods used to schedule and manage the jobs and tasks in a compute cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a225343f-49a9-4838-9b15-d37775220dde'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: IScheduler interface
---

# IScheduler interface

Defines the methods used to schedule and manage the jobs and tasks in a compute cluster.

To create an instance of this interface, call the [**CoCreateInstance**](_com_cocreateinstance) function. Use CLSID\_Scheduler as the class identifier and IID\_IScheduler as the interface identifier. For an example, see [Connecting to a Cluster](connecting-to-a-cluster.md).

## Members

The **IScheduler** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IScheduler** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IScheduler** interface has these methods.



| Method                                                                          | Description                                                                                                                                                                                                                                 |
|:--------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddJob**](ischeduler-addjob.md)                                             | Adds the specified job to the cluster.<br/>                                                                                                                                                                                           |
| [**CancelJob**](ischeduler-canceljob.md)                                       | Cancels the specified job.<br/>                                                                                                                                                                                                       |
| [**CancelJob\_2**](ischeduler-canceljob-2.md)                                  | Cancels the specified job and provides a message to the user that explains why you canceled the job, and optionally forces the job to stop immediately.<br/> This method is supported only for Windows HPC Server 2008 R2.<br/> |
| [**CloneJob**](ischeduler-clonejob.md)                                         | Clones the specified job.<br/>                                                                                                                                                                                                        |
| [**Close**](ischeduler-close.md)                                               | Closes the connection between the application and the HPC Job Scheduler Service.<br/> This method is supported only for Windows HPC Server 2008 R2.<br/>                                                                        |
| [**ConfigureJob**](ischeduler-configurejob.md)                                 | Moves the job to the configuration state.<br/>                                                                                                                                                                                        |
| [**Connect**](ischeduler-connect.md)                                           | Connects to the specified cluster.<br/>                                                                                                                                                                                               |
| [**CreateCommand**](ischeduler-createcommand.md)                               | Creates a command to execute and writes the output to the cluster's spooler.<br/>                                                                                                                                                     |
| [**CreateCommandInfo**](ischeduler-createcommandinfo.md)                       | Creates a CommandInfo object that defines the command properties.<br/>                                                                                                                                                                |
| [**CreateFilterCollection**](ischeduler-createfiltercollection.md)             | Creates an empty collection to which you add filter properties.<br/>                                                                                                                                                                  |
| [**CreateIntCollection**](ischeduler-createintcollection.md)                   | Creates an empty collection to which you add integer values.<br/>                                                                                                                                                                     |
| [**CreateJob**](ischeduler-createjob.md)                                       | Creates a job that uses the default job template.<br/>                                                                                                                                                                                |
| [**CreateNameValueCollection**](ischeduler-createnamevaluecollection.md)       | Creates an empty collection to which you can add name/value pairs.<br/>                                                                                                                                                               |
| [**CreateParametricTaskId**](ischeduler-createparametrictaskid.md)             | Creates a task identifier that identifies a parametric task.<br/>                                                                                                                                                                     |
| [**CreatePool**](ischeduler-createpool.md)                                     | Creates a pool on a cluster based on the supplied name with a desired weight. An exception is thrown if a pool with the same name exists.<br/>                                                                                        |
| [**CreateSortCollection**](ischeduler-createsortcollection.md)                 | Creates an empty collection to which you add sort properties.<br/>                                                                                                                                                                    |
| [**CreateStringCollection**](ischeduler-createstringcollection.md)             | Creates an empty collection to which you add string values.<br/>                                                                                                                                                                      |
| [**CreateTaskId**](ischeduler-createtaskid.md)                                 | Creates a task identifier that identifies a task.<br/>                                                                                                                                                                                |
| [**DeleteCachedCredentials**](ischeduler-deletecachedcredentials.md)           | Deletes the credentials that were cached for the specified user.<br/>                                                                                                                                                                 |
| [**DeleteEmailCredentials**](ischeduler-deleteemailcredentials.md)             | Removes the email credentials for running jobs.<br/>                                                                                                                                                                                  |
| [**DeletePool**](ischeduler-deletepool.md)                                     | Deletes a pool on a cluster based on the supplied name. An exception is thrown if the pool doesn’t exist.<br/>                                                                                                                        |
| [**EnrollCertificate**](ischeduler-enrollcertificate.md)                       | Enrolls the user in a certificate based on the supplied template.<br/>                                                                                                                                                                |
| [**GetActiveHeadNode**](ischeduler-getactiveheadnode.md)                       | Retrieves the name of the active head node.<br/>                                                                                                                                                                                      |
| [**GetCertificateFromStore**](ischeduler-getcertificatefromstore.md)           | Retrieves a certificate matching the thumbprint from the local store encoded as a stream of bytes.<br/>                                                                                                                               |
| [**GetCounters**](ischeduler-getcounters.md)                                   | Retrieves counter information for the cluster.<br/>                                                                                                                                                                                   |
| [**GetJobIdList**](ischeduler-getjobidlist.md)                                 | Retrieves a list of job identifiers based on the specified filter.<br/>                                                                                                                                                               |
| [**GetJobList**](ischeduler-getjobidlist.md)                                   | Retrieves a list of job objects based on the specified filter.<br/>                                                                                                                                                                   |
| [**GetJobTemplateList**](ischeduler-getjobtemplatelist.md)                     | Retrieves a list of job template names defined in the cluster.<br/>                                                                                                                                                                   |
| [**GetNodeGroupList**](ischeduler-getnodegrouplist.md)                         | Retrieves a list of node group names defined in the cluster.<br/>                                                                                                                                                                     |
| [**GetNodeIdList**](ischeduler-getnodeidlist.md)                               | Retrieves a list of identifiers for the nodes in the cluster based on the specified filter.<br/>                                                                                                                                      |
| [**GetNodeList**](ischeduler-getnodelist.md)                                   | Retrieves a list of nodes in the cluster based on the specified filter.<br/>                                                                                                                                                          |
| [**GetNodesInNodeGroup**](ischeduler-getnodesinnodegroup.md)                   | Retrieves the list of nodes in the specified node group.<br/>                                                                                                                                                                         |
| [**GetPoolList**](ischeduler-getpoollist.md)                                   | Gets a list of all pools on the cluster.<br/>                                                                                                                                                                                         |
| [**GetServerVersion**](ischeduler-getserverversion.md)                         | Retrieves the file version of the HPC server assembly.<br/>                                                                                                                                                                           |
| [**GetUserPrivilege**](ischeduler-getuserprivilege.md)                         | Retrieves the privilege level of the user.<br/>                                                                                                                                                                                       |
| [**OpenJob**](ischeduler-openjob.md)                                           | Retrieves the specified job from the scheduler.<br/>                                                                                                                                                                                  |
| [**OpenNode**](ischeduler-opennode.md)                                         | Retrieves a node object using the specified node identifier.<br/>                                                                                                                                                                     |
| [**OpenNodeByName**](ischeduler-opennode-2.md)                                 | Retrieves a node object using the specified node name.<br/>                                                                                                                                                                           |
| [**OpenPool**](ischeduler-openpool.md)                                         | Opens a pool based on the name of the pool on the cluster.<br/>                                                                                                                                                                       |
| [**SetCachedCredentials**](ischeduler-setcachedcredentials.md)                 | Sets the credentials for the specified user in the credential cache, so that the job scheduler can use the credentials for submitting jobs.<br/>                                                                                      |
| [**SetCertificateCredentials**](ischeduler-setcertificatecredentials.md)       | Uploads a certificate in the client’s certificate store to the scheduler for running jobs as this user.<br/>                                                                                                                          |
| [**SetCertificateCredentialsPfx**](ischeduler-setcertificatecredentialspfx.md) | Uploads a certificate encoded with a password to the scheduler to use for running jobs as this user.<br/>                                                                                                                             |
| [**SetClusterParameter**](ischeduler-setclusterparameter.md)                   | Sets a configuration parameter for the cluster.<br/>                                                                                                                                                                                  |
| [**SetEmailCredentials**](ischeduler-setemailcredentials.md)                   | Sets the email credentials by using the specified username and password.<br/>                                                                                                                                                         |
| [**SetEnvironmentVariable**](ischeduler-setenvironmentvariable.md)             | Sets a cluster-wide environment variable.<br/>                                                                                                                                                                                        |
| [**SetInterfaceMode**](ischeduler-setinterfacemode.md)                         | Specifies whether the calling application is a console or Windows application.<br/>                                                                                                                                                   |
| [**SubmitJob**](ischeduler-submitjob.md)                                       | Adds the job to the scheduling queue using the job object to identify the job.<br/>                                                                                                                                                   |
| [**SubmitJobById**](ischeduler-submitjob-2.md)                                 | Adds the job to the scheduling queue using the job identifier to identify the job.<br/>                                                                                                                                               |



 

### Properties

The **IScheduler** interface has these properties.



| Property                                                                   | Access type          | Description                                                  |
|:---------------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------|
| [**ClusterParameters**](ischeduler-clusterparameters.md)<br/>       | Read-only<br/> | Retrieves the cluster's configuration parameters.<br/> |
| [**EnvironmentVariables**](ischeduler-environmentvariables.md)<br/> | Read-only<br/> | Retrieves the cluster-wide environment variables.<br/> |



 

## Remarks

After creating an instance of this interface, call the [**Connect**](ischeduler-connect.md) method to connect to a cluster. You can then create and schedule jobs, run commands, and retrieve information about nodes in the cluster.

To create the Scheduler object in a script, use Microsoft.Hpc.Scheduler.Scheduler as the program identifier when calling the **CreateObject** method.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerNode**](ischedulernode.md)
</dt> <dt>

[**ISchedulerCounters**](ischedulercounters.md)
</dt> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




