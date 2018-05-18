---
Description: 'Defines a generic collection of objects that the scheduler returns.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a9426262-fd1d-408d-9279-1beae4e8bf2e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ISchedulerCollection interface
---

# ISchedulerCollection interface

Defines a generic collection of objects that the scheduler returns.

To get this interface, call one of the following methods:

-   [**IScheduler::GetJobList**](ischeduler-getjoblist.md)
-   [**IScheduler::GetNodeList**](ischeduler-getnodelist.md)
-   [**ISchedulerJob::GetTaskIdList**](ischedulerjob-gettaskidlist.md)
-   [**ISchedulerJob::GetTaskList**](ischedulerjob-gettasklist.md)
-   [**ISchedulerNode::GetCores**](ischedulernode-getcores.md)

## Members

The **ISchedulerCollection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ISchedulerCollection** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ISchedulerCollection** interface has these methods.



| Method                                                      | Description                                                                               |
|:------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| [**Add**](ischedulercollection-add.md)                     | Adds an item to the collection.<br/>                                                |
| [**Clear**](ischedulercollection-clear.md)                 | Removes all items from the collection.<br/>                                         |
| [**Contains**](ischedulercollection-contains.md)           | Determines whether the collection contains the specified item.<br/>                 |
| [**GetEnumerator**](ischedulercollection-getenumerator.md) | Retrieves an enumerator that you use to enumerate the items in the collection.<br/> |
| [**Remove**](ischedulercollection-remove.md)               | Removes an item from the collection.<br/>                                           |



 

### Properties

The **ISchedulerCollection** interface has these properties.



| Property                                               | Access type          | Description                                                            |
|:-------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------|
| [**Count**](ischedulercollection-count.md)<br/> | Read-only<br/> | Retrieves a count of the number of items in the collection.<br/> |
| [**Item**](ischedulercollection-item.md)<br/>   | Read-only<br/> | Retrieves the specified item from the collection.<br/>           |



 

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> <dt>

[**IFilterCollection**](ifiltercollection.md)
</dt> <dt>

[**IIntCollection**](iintcollection.md)
</dt> <dt>

[**INameValueCollection**](inamevaluecollection2.md)
</dt> <dt>

[**ISortCollection**](isortcollection.md)
</dt> <dt>

[**IStringCollection**](istringcollection.md)
</dt> </dl>

 

 




