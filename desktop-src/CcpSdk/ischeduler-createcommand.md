---
Description: 'Creates a command to execute.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ea80e951-7c54-452d-b03f-44043a8f1dd3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::CreateCommand method'
---

# IScheduler::CreateCommand method

Creates a command to execute.

## Syntax


```C++
HRESULT CreateCommand(
  [in]  BSTR              commandLine,
  [in]  ICommandInfo      *info,
  [in]  IStringCollection *nodeSelection,
  [out] IRemoteCommand    **command
);
```



## Parameters

<dl> <dt>

*commandLine* \[in\]
</dt> <dd>

The command to execute. The command is limited to 480 Unicode characters.

</dd> <dt>

*info* \[in\]
</dt> <dd>

An [**ICommandInfo**](icommandinfo.md) interface that provides additional property values used by the command. If the command does not use the additional property values, set to **NULL**.

</dd> <dt>

*nodeSelection* \[in\]
</dt> <dd>

An [**IStringCollection**](istringcollection.md) interface that identifies the nodes on which the command will run. To run the command on all nodes, set to **NULL**.

</dd> <dt>

*command* \[out\]
</dt> <dd>

An [**IRemoteCommand**](iremotecommand.md) interface that defines the command to run.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

To capture the output from the command, you must subscribe to the events that the command object raises. For details, see the [**IRemoteCommandEvents**](iremotecommandevents.md) interface.

To run a command, the user must run the calling application as an administrator.

When you create a command, you are creating a special job that runs immediately on the specified nodes. The job contains two tasks: the command to run and a proxy task used by the scheduler to process the output from the command (use the [**ISchedulerTask.Name**](ischedulertask-name.md) property to distinguish the two tasks). You cannot rerun a command. Only users with elevated administrator privileges can run commands.

## Examples

For an example, see [Executing Commands](executing-commands.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Header<br/>       | <dl> <dt>Oledb.h</dt> </dl>                     |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::CreateJob**](ischeduler-createjob.md)
</dt> </dl>

 

 




