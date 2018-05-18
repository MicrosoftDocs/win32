---
Description: 'Executes the command.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5acc9e44-9055-4be8-ae5b-0386e6da9a52'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IRemoteCommand::Start method'
---

# IRemoteCommand::Start method

Executes the command.

## Syntax


```C++
HRESULT Start();
```



## Parameters

This method has no parameters.

## Remarks

The credentials used to run the command are requested from the user. If your application is a Windows application, you must call the [**IScheduler::SetInterfaceMode**](ischeduler-setinterfacemode.md) method to specify the parent window for the credentials dialog box.

After starting the command, your application must continue to run until the job that run the command finishes. If your application exits too soon, the HPC Job Scheduler Service may not create and start the task that runs the command.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IRemoteCommand**](iremotecommand.md)
</dt> <dt>

[**IRemoteCommand::StartWithCredentials**](iremotecommand-startwithcredentials.md)
</dt> </dl>

 

 




