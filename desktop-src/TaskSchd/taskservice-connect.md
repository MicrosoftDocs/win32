---
title: TaskService.Connect method
description: For scripting, connects to a remote machine and associates all subsequent calls on this interface with a remote session.
ms.assetid: '206087df-307c-4ba9-9e83-915f5287f281'
keywords:
- Connect method Task Scheduler
- Connect method Task Scheduler , TaskService object
- TaskService object Task Scheduler , Connect method
topic_type:
- apiref
api_name:
- TaskService.Connect
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskService.Connect method

For scripting, connects to a remote machine and associates all subsequent calls on this interface with a remote session. If the serverName parameter is empty, then this method will execute on the local computer. If the userId is not specified, then the current token is used.

## Syntax


```VB
TaskService.Connect( _
  [ ByVal serverName ], _
  [ ByVal user ], _
  [ ByVal domain ], _
  [ ByVal password ] _
)
```



## Parameters

<dl> <dt>

*serverName* \[in, optional\]
</dt> <dd>

The name of the computer that you want to connect to. If the serverName parameter is empty, then this method will execute on the local computer.

</dd> <dt>

*user* \[in, optional\]
</dt> <dd>

The user name that is used during the connection to the computer. If the user is not specified, then the current token is used.

</dd> <dt>

*domain* \[in, optional\]
</dt> <dd>

The domain of the user specified in the *user* parameter.

</dd> <dt>

*password* \[in, optional\]
</dt> <dd>

The password that is used to connect to the computer. If the user name and password are not specified, then the current token is used.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The **TaskService.Connect** method should be called before calling any of the other [**TaskService**](taskservice.md) methods.

If the Connect method fails, you can collect the error identifier to find the meaning of the error. The following table lists the error identifiers and their descriptions.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Error Identifier</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0x80070005</td>
<td>Access is denied to connect to the Task Scheduler service.</td>
</tr>
<tr class="even">
<td>0x80041315</td>
<td>The Task Scheduler service is not running.</td>
</tr>
<tr class="odd">
<td>0x8007000e</td>
<td>The application does not have enough memory to complete the operation or the <em>user</em>, <em>password</em>, or <em>domain</em> has at least one null and one non-null value.</td>
</tr>
<tr class="even">
<td>53</td>
<td>This error is returned in the following situations:
<ul>
<li>The computer name specified in the <em>serverName</em> parameter does not exist.</li>
<li>When you are trying to connect to a Windows Server 2003 or Windows XP computer, and the remote computer does not have the File and Printer Sharing firewall exception enabled or the Remote Registry service is not running.</li>
<li>When you are trying to connect to a Windows Vista computer, and the remote computer does not have the Remote Scheduled Tasks Management firewall exception enabled and the File and Printer Sharing firewall exception enabled, or the Remote Registry service is not running.</li>
</ul></td>
</tr>
<tr class="odd">
<td>50</td>
<td>The <em>user</em>, <em>password</em>, or <em>domain</em> parameters cannot be specified when connecting to a remote Windows XP or Windows Server 2003 computer from a Windows Vista computer.</td>
</tr>
</tbody>
</table>



 

If you are to connecting to a remote Windows Vista computer from a Windows Vista, you need to allow the Remote Scheduled Tasks Management firewall exception on the remote computer. To allow this exception click Start, Control Panel, Security, Allow a program through Windows Firewall, and then select the Remote Scheduled Tasks Management check box. Then click the Ok button in the Windows Firewall Settings dialog box.

If you are connecting to a remote Windows XP or Windows Server 2003 computer from a Windows Vista computer, you need to allow the File and Printer Sharing firewall exception on the remote computer. To allow this exception click Start, Control Panel, double-click Windows Firewall, select the Exceptions tab, and then select the File and Printer Sharing firewall exception. Then click the OK button in the Windows Firewall dialog box. The Remote Registry service must also be running on the remote computer.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

 





