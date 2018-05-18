---
Description: 'Adds an item to the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '889177b1-91b7-4835-b22b-4091599ebe0b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IIntCollection::Add method'
---

# IIntCollection::Add method

Adds an item to the collection.

## Syntax


```C++
HRESULT Add(
  [in] long item
);
```



## Parameters

<dl> <dt>

*item* \[in\]
</dt> <dd>

The integer item to add to the collection.

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

[**IIntCollection::Remove**](iintcollection-remove.md)
</dt> </dl>

 

 




