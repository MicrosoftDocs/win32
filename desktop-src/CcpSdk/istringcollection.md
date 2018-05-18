---
Description: 'Defines a collection of string values.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e4fae7b4-bd3a-4b0b-b07d-a8cd15aaaf44'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: IStringCollection interface
---

# IStringCollection interface

Defines a collection of string values.

To get this interface, call one of the following properties or method:

-   [**IRemoteCommand::NodeNames**](iremotecommand-nodenames.md)
-   [**IScheduler::GetJobTemplateList**](ischeduler-getjobtemplatelist.md)
-   [**ISchedulerJob::AllocatedNodes**](ischedulerjob-allocatednodes.md)
-   [**ISchedulerJob::NodeGroups**](ischedulerjob-nodegroup.md)
-   [**ISchedulerJob::RequestedNodes**](ischedulerjob-requestednodes.md)
-   [**ISchedulerNode::NodeGroups**](ischedulernode-nodegroups.md)
-   [**ISchedulerTask::AllocatedNodes**](ischedulertask-allocatednodes.md)
-   [**ISchedulerTask::DependsOn**](ischedulertask-dependson.md)
-   [**ISchedulerTask::RequiredNodes**](ischedulertask-requirednodes.md)

To create an empty collection, call the [**IScheduler::CreateStringCollection**](ischeduler-createstringcollection.md) method.

## Members

The **IStringCollection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IStringCollection** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IStringCollection** interface has these methods.



| Method                                                   | Description                                                                               |
|:---------------------------------------------------------|:------------------------------------------------------------------------------------------|
| [**Add**](istringcollection-add.md)                     | Adds an item to the collection.<br/>                                                |
| [**Clear**](istringcollection-clear.md)                 | Removes all items from the collection.<br/>                                         |
| [**Contains**](istringcollection-contains.md)           | Determines whether the collection contains the specified item.<br/>                 |
| [**GetEnumerator**](istringcollection-getenumerator.md) | Retrieves an enumerator that you use to enumerate the items in the collection.<br/> |
| [**Remove**](istringcollection-remove.md)               | Removes an item from the collection.<br/>                                           |



 

### Properties

The **IStringCollection** interface has these properties.



| Property                                            | Access type          | Description                                                  |
|:----------------------------------------------------|:---------------------|:-------------------------------------------------------------|
| [**Count**](istringcollection-count.md)<br/> | Read-only<br/> | Retrieves the number of items in the collection.<br/>  |
| [**Item**](istringcollection-item.md)<br/>   | Read-only<br/> | Retrieves the specified item from the collection.<br/> |



 

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Header<br/>       | <dl> <dt>Wuapi.h</dt> </dl>                     |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IFilterCollection**](ifiltercollection.md)
</dt> <dt>

[**IIntCollection**](iintcollection.md)
</dt> <dt>

[**INameValueCollection**](inamevaluecollection2.md)
</dt> <dt>

[**ISchedulerCollection**](ischedulercollection.md)
</dt> <dt>

[**ISortCollection**](isortcollection.md)
</dt> </dl>

 

 




