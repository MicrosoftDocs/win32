---
title: LogonType (principalType) Element
description: Specifies the security logon method required to run those tasks associated with the principal.
ms.assetid: e36a1755-96f3-45dc-8779-8bd0cfde886c
keywords:
- LogonType element Task Scheduler
topic_type:
- apiref
api_name:
- LogonType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# LogonType (principalType) Element

Specifies the security logon method required to run those tasks associated with the principal.

``` syntax
<xs:element name="LogonType"
    type="logonType"
 />
```

The **LogonType** element is defined by the [**principalType**](taskschedulerschema-principaltype-complextype.md) complex type.

## Parent element



| Element                                                                  | Derived from                                                           | Description                                                    |
|--------------------------------------------------------------------------|------------------------------------------------------------------------|----------------------------------------------------------------|
| [**Principal**](taskschedulerschema-principal-principaltype-element.md) | [**principalType**](taskschedulerschema-principaltype-complextype.md) | Specifies the security credentials for a principal.<br/> |



## Remarks

The **LogonType** element and the [**UserId**](taskschedulerschema-userid-principaltype-element.md) element are used together to define the user required to run those tasks that use this principal.

For scripting development, the logon type for the principal is specified by the [**Principal.LogonType**](principal-logontype.md) property.

For C++ development, the logon type for the principal is specified by the [**IPrincipal::LogonType**](/windows/desktop/api/taskschd/nf-taskschd-iprincipal-get_logontype) property.

This element (defined by the [**logonType**](taskschedulerschema-logontype-simpletype.md) simple type) must have one of the following values.

-   S4U: User must log on using a service for user (S4U) logon. When an S4U logon is used, no password is stored by the system and there is no access to the network or encrypted files.
-   Password: User must log on using a password.
-   InteractiveToken: User must already be logged on. The task will be run only in an existing interactive session.

For a task, that contains a message box action, the message box will be displayed if the task is activated and the task has an interactive logon type. To set the task logon type to be interactive, specify **InteractiveToken** in the **<LogonType>** element of the task principal.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





