---
Description: 'Retrieves the specified item from the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ef51c175-62e2-496e-9b6b-155e670395c3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCollection::Item property'
---

# ISchedulerCollection::Item property

Retrieves the specified item from the collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Item(
  [in]  long index,
  [out] VARIANT *pItem
);
```



## Property value

The specified item from the collection. The item is returned as a VARIANT. The type of the variant depends on the contents of the collection (see the method or property that returned the collection for the type).

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Examples

For an example, see Getting a [Getting a List of Nodes in the Cluster](getting-a-list-of-nodes-in-the-cluster.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerCollection**](ischedulercollection.md)
</dt> <dt>

[**ISchedulerCollection.Count**](ischedulercollection-count.md)
</dt> <dt>

[**ISchedulerCollection::GetEnumerator**](ischedulercollection-getenumerator.md)
</dt> </dl>

 

 




