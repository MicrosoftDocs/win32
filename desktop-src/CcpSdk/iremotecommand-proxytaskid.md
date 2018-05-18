---
Description: 'Retrieves the unique task identifier for the proxy task in a remote command job. The proxy task is the task that sends the output and error streams from all of the nodes in a remote command to the client.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ba0ed611-bc8d-4ba6-bed5-47ebc6ee233f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IRemoteCommand::ProxyTaskId property'
---

# IRemoteCommand::ProxyTaskId property

Retrieves the unique task identifier for the proxy task in a remote command job. The proxy task is the task that sends the output and error streams from all of the nodes in a remote command to the client.

This property is read-only.

## Syntax


```C++
HRESULT get_ProxyTaskId(
  [out] long *pRetVal
);
```



## Property value

The unique task identifier for the proxy task in a remote command job.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

Each remote command job has a proxy task in addition to a task for each node in the remote command.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 with Service Pack 1 Client Utilities<br/>       |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IRemoteCommand**](iremotecommand.md)
</dt> </dl>

 

 




