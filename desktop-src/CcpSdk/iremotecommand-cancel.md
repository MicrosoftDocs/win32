---
Description: 'Cancels the command.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f656c992-be39-44ce-8a32-f75387943c08'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IRemoteCommand::Cancel method'
---

# IRemoteCommand::Cancel method

Cancels the command.

## Syntax


```C++
HRESULT Cancel();
```



## Parameters

This method has no parameters.

## Remarks

You can cancel the command at any time before the command finishes. The TTLCompletedJobs cluster parameter (for details, see the Remarks section of [**IScheduler::SetClusterParameter**](ischeduler-setclusterparameter.md)) determines when the command is removed from the scheduler after it has been canceled.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IRemoteCommand**](iremotecommand.md)
</dt> </dl>

 

 




