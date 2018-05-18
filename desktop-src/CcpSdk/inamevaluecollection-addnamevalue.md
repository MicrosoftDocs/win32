---
Description: 'Adds a name/value pair to the collection.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b00aeafd-18d6-44f7-91bd-2146f06ebfdd'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'INameValueCollection::AddNameValue method'
---

# INameValueCollection::AddNameValue method

Adds a name/value pair to the collection.

## Syntax


```C++
HRESULT AddNameValue(
  [in] BSTR name,
  [in] BSTR value
);
```



## Parameters

<dl> <dt>

*name* \[in\]
</dt> <dd>

The name.

</dd> <dt>

*value* \[in\]
</dt> <dd>

The value.

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

[**INameValueCollection**](inamevaluecollection2.md)
</dt> </dl>

 

 




