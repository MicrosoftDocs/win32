---
description: Enables users to perform common tasks as nonadministrators, called standard users, and as administrators without having to switch users, log off, or use Run As.
ms.assetid: 8a7ba726-c2a6-4b7b-b664-3c6fcfbfb221
title: User Account Control (Authorization)
ms.topic: article
ms.date: 05/31/2018
---

# User Account Control (Authorization)

User Account Control (UAC) enables users to perform common tasks as nonadministrators, called standard users, and as administrators without having to switch users, log off, or use **Run As**. The behavior of UAC for the "Never notify" setting no longer disables UAC. The "Never notify" setting gives you a split token and always automatically elevates the privilege required. This subtlety may cause your app to have compatibility problems. You can still disable UAC by using Group Policies or manually setting the registry key.

**Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:** The "Never notify" setting disables UAC.

For example, if you perform the following steps to change the "Never notify" setting, you get different outcomes when you attempt to create a file in a folder that requires elevated privileges. The Windows 8 behavior is to deny access. The Windows 7 behavior allows you to create the File.txt file.

1.  Click or tap **Start**. In the search box, type "Change User Account Control settings".
2.  Click or tap **Change User Account Control settings** to open it.
3.  Move the slider to **Never notify**.
4.  Click or tap **OK**.
5.  Restart your computer.
6.  Click or tap **Start** and then **Run**. In the **Open** box, type "Cmd.exe". Note that the title of the window doesn't contain the string "Administrator".
7.  Type "echo > %windir%\\system32\\File.txt".

UAC was added in Windows Server 2008 and Windows Vista. A standard user account is synonymous with a user account in Windows XP. User accounts that are members of the local Administrators group will run most applications as a standard user.

For information about UAC, see the following topics.



| Topic                                                                                                                                        | Description                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| [Guidelines for User Account Control in UI Development](https://msdn.microsoft.com/library/aa511445(l=en-us,v=MSDN.10).aspx)<br/> | General information about UAC.<br/>                                                                                                     |
| [Developing Applications that Require Administrator Privilege](developing-applications-that-require-administrator-privilege.md)<br/>  | Models for developing applications that perform operations that require administrative privilege, but that run as a standard user.<br/> |
| [Authorization Reference](authorization-reference.md)<br/>                                                                            | Detailed information about authorization functions, interfaces, structures, and other programming elements.<br/>                        |



 

 

 




