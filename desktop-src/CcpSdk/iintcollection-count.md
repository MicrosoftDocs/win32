---
Description: 'Retrieves the number of items in the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '91e9d380-aae3-4237-8d55-cbf2e47c1acc'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IIntCollection::Count property'
---

# IIntCollection::Count property

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

[**IIntCollection**](iintcollection.md)
</dt> </dl>

 

 




