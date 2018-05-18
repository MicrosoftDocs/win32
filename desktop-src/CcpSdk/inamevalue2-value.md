---
Description: 'Retrieves the value from the name/value pair.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b8e3ef24-a044-459c-a46e-74d067f423ac'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'INameValue::Value property'
---

# INameValue::Value property

Retrieves the value from the name/value pair.

This property is read-only.

## Syntax


```C++
HRESULT get_Value(
  [out] BSTR *pValue
);
```



## Property value

The value.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**INameValue**](inamevalue2.md)
</dt> <dt>

[**INameValue.Name**](inamevalue2-name.md)
</dt> </dl>

 

 




