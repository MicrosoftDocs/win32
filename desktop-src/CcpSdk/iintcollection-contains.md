---
Description: 'Determines whether the collection contains the specified item.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ac91b8df-6020-451e-b70a-c948b38053ee'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IIntCollection::Contains method'
---

# IIntCollection::Contains method

Determines whether the collection contains the specified item.

## Syntax


```C++
HRESULT Contains(
  [in]  long         item,
  [out] VARIANT_BOOL *pExists
);
```



## Parameters

<dl> <dt>

*item* \[in\]
</dt> <dd>

The item to find.

</dd> <dt>

*pExists* \[out\]
</dt> <dd>

Is VARIANT\_TRUE if the item exists; otherwise, VARIANT\_FALSE.

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
</dt> </dl>

 

 




