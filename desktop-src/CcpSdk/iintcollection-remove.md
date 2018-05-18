---
Description: 'Removes the first occurrence of the specified item from the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8014ef34-57e5-44b7-9c39-218526ac821b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IIntCollection::Remove method'
---

# IIntCollection::Remove method

Removes the first occurrence of the specified item from the collection.

## Syntax


```C++
HRESULT Remove(
  [in]  long         item,
  [out] VARIANT_BOOL *pIsRemoved
);
```



## Parameters

<dl> <dt>

*item* \[in\]
</dt> <dd>

The integer item to remove from the collection.

</dd> <dt>

*pIsRemoved* \[out\]
</dt> <dd>

Is VARIANT\_TRUE if the item is found and removed from the collection; otherwise, VARIANT\_FALSE.

</dd> </dl>

## Return value

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

[**IIntCollection::Add**](iintcollection-add.md)
</dt> <dt>

[**IIntCollection::Clear**](iintcollection-clear.md)
</dt> </dl>

 

 




