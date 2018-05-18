---
Description: 'Retrieves the name from the name/value pair.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '11ff3c4d-2c83-412a-ae0f-f107e047454f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'INameValue::get\_Name method'
---

# INameValue::get\_Name method

Retrieves the name from the name/value pair.

## Syntax


```C++
HRESULT get_Name(
  [out] BSTR *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The name.

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

[**INameValue::get\_Value**](inamevalue-get-value.md)
</dt> </dl>

 

 




