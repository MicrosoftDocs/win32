---
Description: 'Retrieves a description of the error that occurred when a method of the ICluster interface failed.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'befc6fab-067b-4cf4-ab64-f06d1d3cc1e6'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::get\_ErrorMessage method'
---

# ICluster::get\_ErrorMessage method

Retrieves a description of the error that occurred when a method of the [**ICluster**](icluster.md) interface failed.

## Syntax


```C++
HRESULT get_ErrorMessage(
  [out] BSTR *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The message that describes the method failure.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The method always returns the last error that was set.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**IJob::get\_ErrorMessage**](ijob-get-errormessage.md)
</dt> <dt>

[**ITask::get\_ErrorMessage**](itask-get-errormessage.md)
</dt> </dl>

 

 




