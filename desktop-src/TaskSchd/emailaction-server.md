---
title: EmailAction.Server property
description: For scripting, gets or sets the name of the SMTP server that you use to send email from.
ms.assetid: a6e03144-ae3e-4c4c-aad8-884be5ab324f
keywords:
- Server property Task Scheduler
- Server property Task Scheduler , EmailAction object
- EmailAction object Task Scheduler , Server property
topic_type:
- apiref
api_name:
- EmailAction.Server
api_location:
- taskschd.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EmailAction.Server property

\[This object is no longer supported. Please use IExecAction with the powershell [**Send-MailMessage**](796227F5-C9FF-402D-8A04-CDE9E0C180EE) cmdlet as a workaround.\]

For scripting, gets or sets the name of the SMTP server that you use to send email from.

This property is read/write.

## Syntax


```VB
EmailAction.Server As String
```



## Property value

The name of the server that you use to send email from.

## Remarks

Make sure the SMTP server that sends the email is setup correctly. E-mail is sent using NTLM authentication for Windows SMTP servers, which means that the security credentials used for running the task must also have privileges on the SMTP server to send email message. If the SMTP server is a non-Windows based server, then the email will be sent if the server allows anonymous access. For information about setting up the SMTP server, see [SMTP Server Setup](http://go.microsoft.com/fwlink/p/?linkid=69001), and for information about managing SMTP server settings, see [SMTP Administration](http://go.microsoft.com/fwlink/p/?linkid=69002).

## Requirements



|                                     |                                                                                         |
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

 

 





