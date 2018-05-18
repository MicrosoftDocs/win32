---
Description: 'Creates an object that you can use to provide additional property values to a command.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f593b98d-5564-479e-a160-4776ea10510b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::CreateCommandInfo method'
---

# IScheduler::CreateCommandInfo method

Creates an object that you can use to provide additional property values to a command.

## Syntax


```C++
HRESULT CreateCommandInfo(
  [in]  INameValueCollection *envVariables,
  [in]  BSTR                 workDirectory,
  [in]  BSTR                 stdin,
  [out] ICommandInfo         **pCommandInfo
);
```



## Parameters

<dl> <dt>

*envVariables* \[in\]
</dt> <dd>

An [**INameValueCollection**](inamevaluecollection2.md) interface that contains a collection of environment variables used by the command. If the command does not use additional environment variables, set to null.

</dd> <dt>

*workDirectory* \[in\]
</dt> <dd>

The full path to the startup directory for the command. If the command runs in the current directory, set to an empty string.

</dd> <dt>

*stdin* \[in\]
</dt> <dd>

The full path to the standard input file used by the command. If the command does not use an input file, set to an empty string.

</dd> <dt>

*pCommandInfo* \[out\]
</dt> <dd>

An [**ICommandInfo**](icommandinfo.md) interface that defines the property values used by the command.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IRemoteCommand**](iremotecommand.md)
</dt> </dl>

 

 




