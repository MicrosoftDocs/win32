---
Description: 'Retrieves the size of the process working set.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '0c9b576b-6712-40c8-9d59-849671765538'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IResourceUsage::get\_WorkingSet method'
---

# IResourceUsage::get\_WorkingSet method

Retrieves the size of the process working set.

## Syntax


```C++
HRESULT get_WorkingSet(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The size of the process working set, in bytes.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IResourceUsage**](iresourceusage.md)
</dt> </dl>

 

 




