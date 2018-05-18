---
Description: 'Retrieves the name from the name/value pair.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd32e76c0-8607-40dc-9411-c79b71f9bee3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'INameValue::Name property'
---

# INameValue::Name property

Retrieves the name from the name/value pair.

This property is read-only.

## Syntax


```C++
HRESULT get_Name(
  [out] BSTR *pName
);
```



## Property value

The name.

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

[**INameValue.Value**](inamevalue2-value.md)
</dt> </dl>

 

 




