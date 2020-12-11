---
title: RunLevel (runLevelType) Element
description: Contains a value that specifies the security context level for running the task.
ms.assetid: dc113ffa-8ac9-4dcd-a106-45295da42f46
keywords:
- RunLevel element Task Scheduler
topic_type:
- apiref
api_name:
- RunLevel
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# RunLevel (runLevelType) Element

Contains a value that specifies the security context level for running the task. You can specify to run a task using least privileges or elevated privileges. A value of 0 specifies to run the task with lowest privileges, and a value of 1 specifies to run the task with elevated privileges.

``` syntax
<xs:element name="RunLevel"
    type="runLevelType"
 />
```

The **RunLevel** element is defined by the [**runLevelType**](taskschedulerschema-runleveltype-simpletype.md) simple type.

## Parent element



| Element                                                                                  | Derived from                                                           | Description                                                                                                                           |
|------------------------------------------------------------------------------------------|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**Principal (principalType)**](taskschedulerschema-principal-principaltype-element.md) | [**principalType**](taskschedulerschema-principaltype-complextype.md) | Specifies the security credentials for a principal. These credentials define the security context that a task runs under. <br/> |



## Remarks

For C++ development, see [**RunLevel Property of IPrincipal**](/windows/desktop/api/taskschd/nf-taskschd-iprincipal-get_runlevel).

For script development, see [**Principal.RunLevel**](principal-runlevel.md).

If a task is registered using the **Builtin\\Administrator** account or the [LocalSystem](/windows/desktop/Services/localsystem-account) or [LocalService](/windows/desktop/Services/localservice-account) accounts, the [**RunLevel**](principal-runlevel.md) property is ignored. The attribute value will also be ignored if [User Account Control](/windows/desktop/SecAuthZ/user-account-control) (UAC) is turned off.

If a task is registered using the **Administrators** group for the security context of the task, then you must also set the [**RunLevel**](principal-runlevel.md) property to "HighestAvailable" to run the task. For more information, see [Security Contexts for Tasks](security-contexts-for-running-tasks.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

