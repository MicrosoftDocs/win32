---
Description: 'Sets the required licenses.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8369bdab-11cc-4d49-b62f-f6a2f7900967'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::put\_SoftwareLicense method'
---

# IJob::put\_SoftwareLicense method

Sets the required licenses.

## Syntax


```C++
HRESULT put_SoftwareLicense(
  [in] BSTR Val
);
```



## Parameters

<dl> <dt>

*Val* \[in\]
</dt> <dd>

The required licenses. The format is *string*:*integer*{,*string*:*integer*}, where each string is the name of an application and each integer represents how many licenses for the application are required.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The name of the application must match the license feature name.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJob**](ijob.md)
</dt> <dt>

[**IJob::get\_SoftwareLicense**](ijob-get-softwarelicense.md)
</dt> </dl>

 

 




