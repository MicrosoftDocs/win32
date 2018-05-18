---
Description: 'Determines whether the collection contains the specified item.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '49541ee4-39f8-43e4-823a-ba1d34de6e8d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IStringCollection::Contains method'
---

# IStringCollection::Contains method

Determines whether the collection contains the specified item.

## Syntax


```C++
HRESULT Contains(
  [in]  BSTR         item,
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

[**IStringCollection**](istringcollection.md)
</dt> </dl>

 

 




