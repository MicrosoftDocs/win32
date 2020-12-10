---
title: Principal object
description: Scripting object that provides the security credentials for a principal.
ms.assetid: '9589f3c2-2709-4e71-8986-2347be049f6b'
keywords:
- Principal object Task Scheduler
- Principal object Task Scheduler , described
topic_type:
- apiref
api_name:
- Principal
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Principal object

Scripting object that provides the security credentials for a principal. These security credentials define the security context for the tasks that are associated with the principal.

## Members

The **Principal** object has these types of members:

-   [Properties](#properties)

### Properties

The **Principal** object has these properties.



| Property                                                | Access type           | Description                                                                                                                                                  |
|:--------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DisplayName**](principal-displayname.md)<br/> | Read/write<br/> | Gets or sets the name of the principal that is displayed in the Task Scheduler UI.<br/>                                                                |
| [**GroupId**](principal-groupid.md)<br/>         | Read/write<br/> | Gets or sets the identifier of the user group that is required to run the tasks that are associated with the principal.<br/>                           |
| [**Id**](principal-id.md)<br/>                   | Read/write<br/> | Gets or sets the identifier of the principal.<br/>                                                                                                     |
| [**LogonType**](principal-logontype.md)<br/>     | Read/write<br/> | Gets or sets the security logon method that is required to run the tasks that are associated with the principal.<br/>                                  |
| [**RunLevel**](principal-runlevel.md)<br/>       | Read/write<br/> | Gets or sets the identifier that is used to specify the privilege level that is required to run the tasks that are associated with the principal.<br/> |
| [**UserId**](principal-userid.md)<br/>           | Read/write<br/> | Gets or sets the user identifier that is required to run the tasks that are associated with the principal.<br/>                                        |



 

## Remarks

When specifying an account, remember to properly use the double backslash in code to specify the domain and user name. For example, use DOMAIN\\\\UserName to specify a value for the [**UserId**](/windows/desktop/api/taskschd/nf-taskschd-iprincipal-get_userid) property.

When reading or writing XML for a task, the security credentials for a principal are specified in the [**Principal**](taskschedulerschema-principal-principaltype-element.md) element of the Task Scheduler schema.

If a task is registered using the at.exe command line tool, and this object is used to retrieve information about the task, then the [**LogonType**](principal-logontype.md) property will return 0, the [**RunLevel**](principal-runlevel.md) property will return 0, and the [**UserId**](principal-userid.md) property will return Nothing.

## Examples

For more information and example code for this scripting object, see [Time Trigger Example (Scripting)](time-trigger-example--scripting-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

 





