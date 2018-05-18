---
Description: 'Adds an item to the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'bccf5c85-4783-4586-b323-906a761f208c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IStringCollection::Add method'
---

# IStringCollection::Add method

Adds an item to the collection.

## Syntax


```C++
HRESULT Add(
  [in] BSTR item
);
```



## Parameters

<dl> <dt>

*item* \[in\]
</dt> <dd>

The string item to add to the collection.

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
</dt> <dt>

[**IStringCollection::Remove**](istringcollection-remove.md)
</dt> </dl>

 

 




