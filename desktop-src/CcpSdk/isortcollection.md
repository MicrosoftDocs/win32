---
Description: 'Defines a collection of sort property objects used to sort the results when retrieving jobs, task, and nodes.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd720f970-582b-4981-b2e4-9ae169cfe330'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ISortCollection interface
---

# ISortCollection interface

Defines a collection of sort property objects used to sort the results when retrieving jobs, task, and nodes.

To get this interface, call the [**IScheduler::CreateSortCollection**](ischeduler-createsortcollection.md) method.

## Members

The **ISortCollection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ISortCollection** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ISortCollection** interface has these methods.



| Method                                                 | Description                                                                               |
|:-------------------------------------------------------|:------------------------------------------------------------------------------------------|
| [**Add**](isortcollection-add.md)                     | Adds an item to the collection.<br/>                                                |
| [**Clear**](ischedulercollection-clear.md)            | Removes all items from the collection.<br/>                                         |
| [**GetEnumerator**](isortcollection-getenumerator.md) | Retrieves an enumerator that you use to enumerate the items in the collection.<br/> |



 

### Properties

The **ISortCollection** interface has these properties.



| Property                                          | Access type          | Description                                                  |
|:--------------------------------------------------|:---------------------|:-------------------------------------------------------------|
| [**Count**](isortcollection-count.md)<br/> | Read-only<br/> | Retrieves the number of items in the collection.<br/>  |
| [**Item**](isortcollection-item.md)<br/>   | Read-only<br/> | Retrieves the specified item from the collection.<br/> |



 

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
</dt> </dl>

 

 




