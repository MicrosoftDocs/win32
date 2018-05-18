---
Description: 'Sets the maximum time that the application will wait for a response from the cluster when making synchronous calls.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a216b6af-e662-4b0c-9dc6-cfffa071d8e0'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::put\_Timeout method'
---

# ICluster::put\_Timeout method

Sets the maximum time that the application will wait for a response from the cluster when making synchronous calls.

## Syntax


```C++
HRESULT put_Timeout(
  [in] long timeout
);
```



## Parameters

<dl> <dt>

*timeout* \[in\]
</dt> <dd>

The time to wait, in milliseconds. To wait indefinitely (the default), set this value to 0.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

Synchronous calls to the cluster wait indefinitely. This can be an issue if the cluster is under heavy load and your application cannot appear to stop responding. This method limits the time to wait before method calls return. When the time-out expires, the method fails and sets [**get\_ErrorMessage**](icluster-get-errormessage.md).

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::get\_Timeout**](icluster-get-timeout.md)
</dt> </dl>

 

 




