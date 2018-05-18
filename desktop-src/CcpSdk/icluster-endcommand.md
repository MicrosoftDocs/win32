---
Description: 'Cancels the specified command on all nodes on which the command is running.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '70a5a0bf-1c24-4940-8c9e-41f49ea27219'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::EndCommand method'
---

# ICluster::EndCommand method

Cancels the specified command on all nodes on which the command is running.

## Syntax


```C++
HRESULT EndCommand(
  [in] long Id
);
```



## Parameters

<dl> <dt>

*Id* \[in\]
</dt> <dd>

The command identifier. Specify the identifier that you used to [execute](icluster-executecommand.md) the command.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::ExecuteCommand**](icluster-executecommand.md)
</dt> <dt>

[**ICluster::ExecuteCommandWithPaging**](icluster-executecommandwithpaging.md)
</dt> </dl>

 

 




