---
Description: 'Represents a collection of name/value pairs.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '29621136-ef85-4177-889d-d1d7c7b00724'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: INameValueCollection interface
---

# INameValueCollection interface

Represents a collection of name/value pairs.

The following properties return this interface:

-   [**ICommandInfo::EnvironmentVariables**](icommandinfo-environmentvariables.md)
-   [**IScheduler::EnvironmentVariables**](ischeduler-environmentvariables.md)
-   [**IScheduler::ClusterParameters**](ischeduler-clusterparameters.md)
-   [**ISchedulerJob::GetCustomProperties**](ischedulerjob-getcustomproperties.md)
-   [**ISchedulerTask::GetCustomProperties**](ischedulertask-getcustomproperties.md)
-   [**ISchedulerTask::EnvironmentVariables**](ischedulertask-environmentvariables.md)

To create this interface, call the [**IScheduler::CreateNameValueCollection**](ischeduler-createnamevaluecollection.md) method.

## Members

The **INameValueCollection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **INameValueCollection** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **INameValueCollection** interface has these methods.



| Method                                                       | Description                                                                                          |
|:-------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------|
| [**AddNameValue**](inamevaluecollection-addnamevalue.md)    | Adds a name/value pair to the collection.<br/>                                                 |
| [**GetEnumerator**](inamevaluecollection2-getenumerator.md) | Retrieves an enumerator that you use to enumerate the name/value pairs in the collection.<br/> |



 

### Properties

The **INameValueCollection** interface has these properties.



| Property                                                | Access type          | Description                                                 |
|:--------------------------------------------------------|:---------------------|:------------------------------------------------------------|
| [**Count**](inamevaluecollection2-count.md)<br/> | Read-only<br/> | Retrieves the number of items in the collection.<br/> |



 

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> <dt>

[**INameValue**](inamevaluecollection2.md)
</dt> </dl>

 

 




