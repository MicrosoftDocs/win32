---
Description: 'Retrieves information about the required licenses.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '897b2d67-d138-4c12-addb-61a36b960999'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::get\_SoftwareLicense method'
---

# IJob::get\_SoftwareLicense method

Retrieves information about the required licenses.

## Syntax


```C++
HRESULT get_SoftwareLicense(
  [out] BSTR *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The required licenses. The format is *string*:*integer*{,*string*:*integer*}, where each string is the name of an application and each integer represents how many licenses for the application are required.

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

[**IJob**](ijob.md)
</dt> <dt>

[**IJob::put\_SoftwareLicense**](ijob-put-softwarelicense.md)
</dt> </dl>

 

 




