---
Description: 'Retrieves the number of items in the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'cca4e925-f495-451f-9955-357c1b98cd80'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'INameValueCollection::Count property'
---

# INameValueCollection::Count property

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

[**INameValueCollection**](inamevaluecollection2.md)
</dt> <dt>

[**INameValueCollection::GetEnumerator**](inamevaluecollection2-getenumerator.md)
</dt> </dl>

 

 




