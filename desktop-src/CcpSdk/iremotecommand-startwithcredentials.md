---
Description: 'Executes the command using the specified credentials.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '68e72a8c-1926-4c2e-af1f-93866a0ec75b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IRemoteCommand::StartWithCredentials method'
---

# IRemoteCommand::StartWithCredentials method

Executes the command using the specified credentials.

## Syntax


```C++
HRESULT StartWithCredentials(
  [in] BSTR username,
  [in] BSTR password
);
```



## Parameters

<dl> <dt>

*username* \[in\]
</dt> <dd>

The name of the RunAs user, in the form *domain*\\*username*. The user name is limited to 80 Unicode characters.

If this parameter is **NULL**, the method uses the owner of the job. If this parameter is an empty string, the service searches the credentials cache for the credentials to use. If the cache contains the credentials for a single user, those credentials are used. However, if multiple credentials exist in the cache, the user is prompted for the credentials.

</dd> <dt>

*password* \[in\]
</dt> <dd>

The password for the RunAs user. The password is limited to 127 Unicode characters.

If this parameter is **NULL** or empty, the method uses the cached password if cached; otherwise, the user is prompted for the password. If your application is a Windows application, you must call the [**IScheduler::SetInterfaceMode**](ischeduler-setinterfacemode.md) method to specify the parent window for the credentials dialog box.

</dd> </dl>

## Remarks

After starting the command, your application must continue to run until the job that run the command finishes. If your application exits too soon, the HPC Job Scheduler Service may not create and start the task that runs the command.

## Examples

For an example, see [Executing Commands](executing-commands.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IRemoteCommand**](iremotecommand.md)
</dt> <dt>

[**IRemoteCommand::Start**](iremotecommand-start.md)
</dt> </dl>

 

 




