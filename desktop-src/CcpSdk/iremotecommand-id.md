---
Description: 'Retrieves the identifier that uniquely identifies the command in the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c0be8c7e-eb40-4529-a33b-004c4df93ecb'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IRemoteCommand::Id property'
---

# IRemoteCommand::Id property

Retrieves the identifier that uniquely identifies the command in the cluster.

This property is read-only.

## Syntax


```C++
HRESULT get_Id(
  [out] long *pId
);
```



## Property value

The identifier that uniquely identifies the command.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IRemoteCommand**](iremotecommand.md)
</dt> <dt>

[**IScheduler::OpenJob**](ischeduler-openjob.md)
</dt> </dl>

 

 




