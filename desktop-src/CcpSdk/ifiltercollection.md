---
Description: 'Defines a collection of filter property objects used to filter the results when retrieving jobs, task, and nodes.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '26f73906-1ec5-4513-bbcb-abe9ac4ec040'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: IFilterCollection interface
---

# IFilterCollection interface

Defines a collection of filter property objects used to filter the results when retrieving jobs, task, and nodes.

To get this interface, call the [**IScheduler::CreateFilterCollection**](ischeduler-createfiltercollection.md) method.

## Members

The **IFilterCollection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IFilterCollection** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IFilterCollection** interface has these methods.



| Method                                                   | Description                                                                               |
|:---------------------------------------------------------|:------------------------------------------------------------------------------------------|
| [**Add**](ifiltercollection-add.md)                     | Adds an item to the collection.<br/>                                                |
| [**Clear**](ifiltercollection-clear.md)                 | Removes all items from the collection.<br/>                                         |
| [**GetEnumerator**](ifiltercollection-getenumerator.md) | Retrieves an enumerator that you use to enumerate the items in the collection.<br/> |



 

### Properties

The **IFilterCollection** interface has these properties.



| Property                                            | Access type          | Description                                                  |
|:----------------------------------------------------|:---------------------|:-------------------------------------------------------------|
| [**Count**](ifiltercollection-count.md)<br/> | Read-only<br/> | Retrieves the number of items in the collection.<br/>  |
| [**Item**](ifiltercollection-item.md)<br/>   | Read-only<br/> | Retrieves the specified item from the collection.<br/> |



 

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> <dt>

[**ISortCollection**](isortcollection.md)
</dt> </dl>

 

 




