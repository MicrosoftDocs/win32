---
Description: 'Defines the privilege levels of HPC users.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b777b93c-dc89-42d4-9250-e45e79d6a524'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: UserPrivilege enumeration
---

# UserPrivilege enumeration

Defines the privilege levels of HPC users.

## Syntax


```C++
typedef enum  { 
  UserPrivilege_AccessDenied  = 0,
  UserPrivilege_User          = 1,
  UserPrivilege_Admin         = 2
} UserPrivilege;
```



## Constants

<dl> <dt>

<span id="UserPrivilege_AccessDenied"></span><span id="userprivilege_accessdenied"></span><span id="USERPRIVILEGE_ACCESSDENIED"></span>**UserPrivilege\_AccessDenied**
</dt> <dd>

The user does not have permissions to access HPC.

</dd> <dt>

<span id="UserPrivilege_User"></span><span id="userprivilege_user"></span><span id="USERPRIVILEGE_USER"></span>**UserPrivilege\_User**
</dt> <dd>

The user is a member of the Users group.

</dd> <dt>

<span id="UserPrivilege_Admin"></span><span id="userprivilege_admin"></span><span id="USERPRIVILEGE_ADMIN"></span>**UserPrivilege\_Admin**
</dt> <dd>

The user is a member of the Administrators group.

</dd> </dl>

## Requirements



|                         |                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.Properties.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Enumerations](hpc-enumerations.md)
</dt> <dt>

[**IScheduler::GetUserPrivilege**](ischeduler-getuserprivilege.md)
</dt> </dl>

 

 




