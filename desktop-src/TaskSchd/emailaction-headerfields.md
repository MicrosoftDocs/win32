---
title: EmailAction.HeaderFields property
description: For scripting, gets or sets the header information in the email you want to send.
ms.assetid: 492c1e7c-805a-4c58-82d3-45c82420c694
keywords:
- HeaderFields property Task Scheduler
- HeaderFields property Task Scheduler , EmailAction object
- EmailAction object Task Scheduler , HeaderFields property
topic_type:
- apiref
api_name:
- EmailAction.HeaderFields
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# EmailAction.HeaderFields property

\[This object is no longer supported. Please use IExecAction with the powershell [**Send-MailMessage**](/powershell/module/microsoft.powershell.utility/send-mailmessage) cmdlet as a workaround.\]

For scripting, gets or sets the header information in the email you want to send.

This property is read/write.

## Syntax


```VB
EmailAction.HeaderFields As TaskNamedValueCollection
```



## Property value

The header information in the email you want to send.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows 7<br/>                                                                    |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                       |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**EmailAction**](emailaction.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

