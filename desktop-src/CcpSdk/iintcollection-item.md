---
Description: 'Retrieves the specified item from the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f5db3ef8-53b9-4243-bda1-82d1c3a8b947'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IIntCollection::Item property'
---

# IIntCollection::Item property

Retrieves the specified item from the collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Item(
  [in]  long index,
  [out] long *pItem
);
```



## Property value

The specified item from the collection.

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
</dt> <dt>

[**IIntCollection::GetEnumerator**](iintcollection-getenumerator.md)
</dt> </dl>

 

 




