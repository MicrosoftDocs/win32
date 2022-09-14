---
title: EmailAction.Attachments property
description: For scripting, gets or sets an array of attachments that is sent with the email message.
ms.assetid: 59bcb8c4-8b8c-4f09-94d6-3a65f1e8c0a8
keywords:
- Attachments property Task Scheduler
- Attachments property Task Scheduler , EmailAction object
- EmailAction object Task Scheduler , Attachments property
topic_type:
- apiref
api_name:
- EmailAction.Attachments
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# EmailAction.Attachments property

\[This object is no longer supported. Please use IExecAction with the powershell [**Send-MailMessage**](/powershell/module/microsoft.powershell.utility/send-mailmessage) cmdlet as a workaround.\]

For scripting, gets or sets an array of attachments that is sent with the email message.

This property is read/write.

## Syntax


```VB
EmailAction.Attachments As String
```



## Property value

An array of attachments that is sent with the email message.

## Remarks

A maximum of eight attachments can be in the array of attachments.

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

 

