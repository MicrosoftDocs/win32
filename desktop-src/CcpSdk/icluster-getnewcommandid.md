---
Description: 'Gets a command identifier that is used to execute a command.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e746bb69-dde6-496f-8d1f-405e6ed0bf1f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::GetNewCommandId method'
---

# ICluster::GetNewCommandId method

Gets a command identifier that is used to execute a command.

## Syntax


```C++
HRESULT GetNewCommandId(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The command identifier.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

The [**ICluster::ExecuteCommand**](icluster-executecommand.md) method requires a command identifier. You use the **GetNewCommandId** method to generate an identifier that uniquely identifies the command that you want to execute.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> </dl>

 

 




