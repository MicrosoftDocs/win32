---
title: Remote Desktop Services permissions
description: You can use the permissions provided for Remote Desktop Services to control how users and groups access the server.
ms.assetid: 448a7f9b-bf12-48eb-a3e7-4512ec288d95
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Remote Desktop Services permissions

You can use the permissions provided for Remote Desktop Services to control how users and groups access the server. For a description of the default permission types and more detailed information about Remote Desktop Services permissions in general, see the documentation that accompanies the Remote Desktop Services Configuration administrative tool. For information about configuring these permissions for Windows Server 2008, see [Configure Permissions for Remote Desktop Services Connections](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc753032(v=ws.11)).

Following is a list of the permissions that you can set and the tasks the permissions allow.



| Value                        | Meaning                                                                                                                                                               |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Query Information<br/> | Query sessions and servers for information.<br/>                                                                                                                |
| Set Information<br/>   | Configure connection properties.<br/>                                                                                                                           |
| Remote Control<br/>    | View or actively control another user's session.<br/>                                                                                                           |
| Logon<br/>             | Log on to a session on the server.<br/>                                                                                                                         |
| Logoff<br/>            | Log off a user from a session. Be aware that logging off a user without warning can result in loss of data at the client.<br/>                                  |
| Message<br/>           | Send a message to another user's sessions.<br/>                                                                                                                 |
| Connect<br/>           | Connect to another session.<br/>                                                                                                                                |
| Disconnect<br/>        | Disconnect a session.<br/>                                                                                                                                      |
| Virtual Channels<br/>  | Use virtual channels. Be aware that turning off virtual channels disables some Remote Desktop Services features such as clipboard and printer redirection.<br/> |
| Reset<br/>             | End a session. Be aware that ending a session without warning can result in loss of data at the client.<br/>                                                    |



 

The Logon permission is required for a user to log on to a new Remote Desktop Services session. All other Remote Desktop Services permissions apply to controlling another user's Remote Desktop Services session.

Remote Desktop Services permissions can be granted, or set, for individual users or groups. Users can also inherit permissions as a result of being a group member. The denial of a permission, however, overrides an inherited permission. For example, members of the Remote Desktop Users (RDU) group are granted the Query permission by default. If an Administrator sets the Query permission to "Deny" for that user, the user will not be able to query another user's session. After a user logs on to a session, the user is granted all other Remote Desktop Services permissions for his or her session.

## Related topics

<dl> <dt>

[Remote Desktop Services management applications](terminal-services-management-applications.md)
</dt> <dt>

[**Win32\_TSAccount**](win32-tsaccount.md)
</dt> </dl>

 

