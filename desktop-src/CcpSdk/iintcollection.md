---
Description: 'Defines a collection of integer values, typically identifiers such as job identifiers.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b4233d25-13ab-4981-b882-0ce09e398ead'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: IIntCollection interface
---

# IIntCollection interface

Defines a collection of integer values, typically identifiers such as job identifiers.

To get this interface, call one of the following properties or methods:

-   [**IScheduler::GetJobIdList**](ischeduler-getjobidlist.md)
-   [**IScheduler::GetNodeIdList**](ischeduler-getnodeidlist.md)

To create an empty collection, call the [**IScheduler::CreateIntCollection**](ischeduler-createintcollection.md) method.

## Members

The **IIntCollection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IIntCollection** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IIntCollection** interface has these methods.



| Method                                                | Description                                                                               |
|:------------------------------------------------------|:------------------------------------------------------------------------------------------|
| [**Add**](iintcollection-add.md)                     | Adds an item to the collection.<br/>                                                |
| [**Clear**](iintcollection-clear.md)                 | Removes all items from the collection.<br/>                                         |
| [**Contains**](iintcollection-contains.md)           | Determines whether the collection contains the specified item.<br/>                 |
| [**GetEnumerator**](iintcollection-getenumerator.md) | Retrieves an enumerator that you use to enumerate the items in the collection.<br/> |
| [**Remove**](iintcollection-remove.md)               | Removes an item from the collection.<br/>                                           |



 

### Properties

The **IIntCollection** interface has these properties.



| Property                                         | Access type          | Description                                                  |
|:-------------------------------------------------|:---------------------|:-------------------------------------------------------------|
| [**Count**](iintcollection-count.md)<br/> | Read-only<br/> | Retrieves the number of items in the collection.<br/>  |
| [**Item**](iintcollection-item.md)<br/>   | Read-only<br/> | Retrieves the specified item from the collection.<br/> |



 

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> </dl>

 

 




