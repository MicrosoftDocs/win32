---
Description: 'Retrieves the command line to execute.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c567421e-f158-40d9-ae1d-5ecf791eccdc'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IRemoteCommand::CommandLine property'
---

# IRemoteCommand::CommandLine property

Retrieves the command line to execute.

This property is read-only.

## Syntax


```C++
HRESULT get_CommandLine(
  [out] BSTR *pCommandLine
);
```



## Property value

The command line to execute.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The command is specified when you call the [**IScheduler::CreateCommand**](ischeduler-createcommand.md) method to create the [**RemoteCommand**](iremotecommand.md) object.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IRemoteCommand**](iremotecommand.md)
</dt> </dl>

 

 




