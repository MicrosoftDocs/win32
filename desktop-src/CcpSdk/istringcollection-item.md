---
Description: 'Retrieves the specified item from the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1bb61adc-63a0-49b5-95fe-5f3941bd8385'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IStringCollection::Item property'
---

# IStringCollection::Item property

Retrieves the specified item from the collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Item(
  [in]  long index,
  [out] BSTR *pItem
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

[**IStringCollection**](istringcollection.md)
</dt> <dt>

[**IStringCollection::GetEnumerator**](istringcollection-getenumerator.md)
</dt> </dl>

 

 




