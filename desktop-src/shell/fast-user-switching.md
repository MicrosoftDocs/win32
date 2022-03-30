---
description: In older operating systems, a user was required to log off before another user could log on. As of Windows XP, a user does not have to log off to allow another user to log on.
ms.assetid: 72f99d32-184f-4f0b-bec1-6068c6e32f88
title: Fast User Switching
ms.topic: article
ms.date: 05/31/2018
---

# Fast User Switching

When a user logs onto a computer, the system loads their profile. Because each user has a unique user account, this allows multiple users to share a computer. When a user logs on, the desktop settings, files, favorites, and history they see are theirs; they cannot be accessed by other users. When that user logs off, their profile is preserved for the next time that they log on. In older operating systems, a user was required to log off before another user could log on. As of Windows XP, a user does not have to log off to allow another user to log on. Instead, it is possible for multiple users to log on and switch quickly between their open accounts. This feature is referred to as *fast user switching*. Switching to another account does not change the state of the applications that a user is currently running. Suppose, for instance, that one user allows another user to switch to their account while the first user is logged on. When the first user switchs back to their account, their applications are running and their network connections are preserved. Therefore, it appears that both users are simultaneously using the computer.

If your applications comply with the Windows 2000 logo requirements, they should work with fast user switching on Windows XP and later operating systems. However, it is important to keep this scenario in mind when developing an application so that it behaves as users would expect. Use the following guidelines when writing your applications:

- Implement true profile separation. The system provides an underlying infrastructure that supports separation of user data, user settings, and computer settings. For example, use the user's **Documents** folder to store user-created data. To locate a directory for application-specific data, use the [known folder](known-folders.md) system with [**FOLDERID\_RoamingAppData**](knownfolderid.md)) or, for older operating systems, the [**CSIDL**](csidl.md) system with [**CSIDL\_APPDATA**](csidl.md)). Use **FOLDERID\_LocalAppData** or **CSIDL\_LOCAL\_APPDATA** for data that should not be available to the user on other computers, such as temporary files.
- Register for notification of a user switch. Typically, an application does not need to be notified when the switch occurs. However, if your application must be notified of a session change, it can register to receive a [**WM\_WTSSESSION\_CHANGE**](../termserv/wm-wtssession-change.md) message.
- Be aware of other instances of your application. For example, there are times when an application must download an update from the Internet. The update can fail if another user is simultaneously running an instance of the application in another session. Even if the update succeeds, the update can cause other running instances of the application to behave in an unpredictable manner. Therefore it is best to perform a dynamic upgrade only if no other instances of the application are running. Before downloading an application update, it might be appropriate to implement a method that signals all running instances of the application to save data and exit cleanly.

 

 
