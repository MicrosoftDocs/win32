---
description: Explains the registry entries for Winlogon events.
ms.assetid: dbebe23f-84ff-4a3e-8b8c-fa3bda10fa57
title: Registry Entries (Authentication)
ms.topic: article
ms.date: 05/31/2018
---

# Registry Entries (Authentication)

In order for your package to receive event notifications from [*Winlogon*](../secgloss/w-gly.md), you must provide the name of the package, the names of the event handler functions in the package, the DLL responsible for implementing the package, and information about whether the DLL supports asynchronous events and impersonation.

You should create the notification package registry key as a subkey of

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**Windows NT**\\**CurrentVersion**\\**Winlogon**\\**Notify**

The name of the key is usually the same as the name of the DLL; however, this is not mandatory. The name chosen for your package must not conflict with the names of other installed notification packages.

In the **Notify** registry key, create the following registry values if there is a relevant event handler function in your package.



| Value name \[data type\]                         | Description                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Asynchronous**\[**REG\_DWORD**\]<br/>    | Indicates whether the package can handle events asynchronously. If this value is set to 1, Winlogon calls the package functions in a separate thread. Otherwise, it does not.<br/>                                                                                                                                                                                                                                 |
| **DllName**\[**REG\_EXPAND\_SZ**\]<br/>    | Name of the DLL that implements the notification package, for example: "Notify.dll".<br/>                                                                                                                                                                                                                                                                                                                          |
| **Impersonate**\[**REG\_DWORD**\]<br/>     | Indicates whether Winlogon should impersonate the security [*context*](../secgloss/c-gly.md) of the logged-on user when it calls the notification package functions. If this value is set to 1, Winlogon uses impersonation. Otherwise, it does not.<br/>                                                                                                                    |
| **Lock**\[**REG\_SZ**\]<br/>               | Name of the function which handles desktop lock events, for example: "WLEventLock".<br/>                                                                                                                                                                                                                                                                                                                           |
| **Logoff**\[**REG\_SZ**\]<br/>             | Name of the function which handles logoff events, for example: "WLEventLogoff".<br/>                                                                                                                                                                                                                                                                                                                               |
| **Logon**\[**REG\_SZ**\]<br/>              | Name of the function which handles logon events, for example: "WLEventLogon".<br/>                                                                                                                                                                                                                                                                                                                                 |
| **Shutdown**\[**REG\_SZ**\]<br/>           | Name of the function which handles shutdown events, for example: "WLEventShutdown".<br/>                                                                                                                                                                                                                                                                                                                           |
| **SmartCardLogonNotify**\[**DWORD**\]<br/> | Indicates whether Winlogon should generate a notification for logon events from smart cards. If this value is set to 1, Winlogon allows smart card notifications. Otherwise, it does not.<br/>                                                                                                                                                                                                                     |
| **StartScreenSaver**\[**REG\_SZ**\]<br/>   | Name of the function that handles screen saver start events, for example: "WLEventStartScreenSaver".<br/>                                                                                                                                                                                                                                                                                                          |
| **StartShell**\[**REG\_SZ**\]<br/>         | Name of the function that handles shell start events, for example: "WLEventStartShell".<br/> A shell start event occurs after the user has logged on but before the desktop appears. It differs from the logon event in that the user's security [*context*](../secgloss/c-gly.md) has been established, and resources such as network connections are available.<br/> |
| **Startup**\[**REG\_SZ**\]<br/>            | Name of the function that handles system startup events, for example: "WLEventStartup".<br/>                                                                                                                                                                                                                                                                                                                       |
| **StopScreenSaver**\[**REG\_SZ**\]<br/>    | Name of the function that handles screen saver stop events, for example: "WLEventStopScreenSaver".<br/>                                                                                                                                                                                                                                                                                                            |
| **Unlock**\[**REG\_SZ**\]<br/>             | Name of the function that handles desktop unlock events, for example: "WLEventUnlock".<br/>                                                                                                                                                                                                                                                                                                                        |



 

 

 
