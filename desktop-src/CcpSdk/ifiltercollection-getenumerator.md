---
Description: 'Retrieves an enumerator that you use to enumerate the items in the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '6cd2a216-8e64-4db2-92b6-8242bbdb1cee'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IFilterCollection::GetEnumerator method'
---

# IFilterCollection::GetEnumerator method

Retrieves an enumerator that you use to enumerate the items in the collection.

## Syntax


```C++
HRESULT GetEnumerator(
  [out] IEnumVARIANT **pEnum
);
```



## Parameters

<dl> <dt>

*pEnum* \[out\]
</dt> <dd>

An [**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e) interface that you use to enumerate the items in the collection. The items of the enumeration are VARIANTs of type VT\_DISPATCH. Query the **pdispVal** member for the [**IFilterProperty**](ifilterproperty.md) interface.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

Because the filter objects are opaque, do not try to enumerate the objects in the collection.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IFilterCollection**](ifiltercollection.md)
</dt> <dt>

[**IFilterCollection.Item**](ifiltercollection-item.md)
</dt> </dl>

 

 




