---
Description: 'Retrieves the privilege level of the user.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4f780f0f-beef-449f-a045-d356355671df'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::GetUserPrivilege method'
---

# IScheduler::GetUserPrivilege method

Retrieves the privilege level of the user.

## Syntax


```C++
HRESULT GetUserPrivilege(
  [out] UserPrivilege *pUserPrivilege
);
```



## Parameters

<dl> <dt>

*pUserPrivilege* \[out\]
</dt> <dd>

An [**UserPrivilege**](userprivilege.md) enumeration value that identifies the privilege level of the user (for example, if the user is running as an administrator or a normal user).

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Examples

For an example, see [Executing Commands](executing-commands.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> </dl>

 

 




