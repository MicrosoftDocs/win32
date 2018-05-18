---
Description: 'Retrieves the number of items in the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'cb372ed2-721d-4dda-bbf9-92ba5a71dcc2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISortCollection::Count property'
---

# ISortCollection::Count property

Retrieves the number of items in the collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Count(
  [out] long *pCount
);
```



## Property value

The number of items.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISortCollection**](isortcollection.md)
</dt> </dl>

 

 




