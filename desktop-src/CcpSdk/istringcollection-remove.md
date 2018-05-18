---
Description: 'Removes the first occurrence of the specified item from the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '84331795-1305-4d7b-817d-d98095a691df'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IStringCollection::Remove method'
---

# IStringCollection::Remove method

Removes the first occurrence of the specified item from the collection.

## Syntax


```C++
VARIANT_BOOL Remove(
  [in]  BSTR         item,
  [out] VARIANT_BOOL *pIsRemoved
);
```



## Parameters

<dl> <dt>

*item* \[in\]
</dt> <dd>

The string item to remove from the collection.

</dd> <dt>

*pIsRemoved* \[out\]
</dt> <dd>

Is VARIANT\_TRUE if the item is found and removed from the collection; otherwise, VARIANT\_FALSE.

</dd> </dl>

## Return value

Is VARIANT\_TRUE if the item is found and removed from the collection; otherwise, VARIANT\_FALSE.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IStringCollection**](istringcollection.md)
</dt> <dt>

[**IStringCollection::Add**](istringcollection-add.md)
</dt> <dt>

[**IStringCollection::Clear**](istringcollection-clear.md)
</dt> </dl>

 

 




