---
Description: 'Retrieves the number of items in the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '97a98373-b9bc-4544-8041-f3b383ab6e6d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IStringCollection::Count property'
---

# IStringCollection::Count property

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

[**IStringCollection**](istringcollection.md)
</dt> </dl>

 

 




