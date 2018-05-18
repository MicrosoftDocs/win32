---
Description: 'Sets the display name of the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ee059c13-2bd9-4a5d-b63f-d31a8631d1dc'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::put\_Name method'
---

# IJob::put\_Name method

Sets the display name of the job.

## Syntax


```C++
HRESULT put_Name(
  [in] BSTR Val
);
```



## Parameters

<dl> <dt>

*Val* \[in\]
</dt> <dd>

The display name. The name is limited to 80 Unicode characters.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The default job name has the form *username*:*timestamp*.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJob**](ijob.md)
</dt> <dt>

[**IJob::get\_Name**](ijob-get-name.md)
</dt> </dl>

 

 




