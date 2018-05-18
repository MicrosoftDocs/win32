---
Description: 'Retrieves the value from the name/value pair.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'cabecf8d-8f79-4e09-8513-28def5a1e187'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'INameValue::get\_Value method'
---

# INameValue::get\_Value method

Retrieves the value from the name/value pair.

## Syntax


```C++
HRESULT get_Value(
  [out] BSTR *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The value.

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

[**INameValue**](inamevalue.md)
</dt> <dt>

[**INameValue::get\_Name**](inamevalue-get-name.md)
</dt> </dl>

 

 




