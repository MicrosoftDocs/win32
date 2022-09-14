---
description: Lists Winlogon notification events.
ms.assetid: 48b0f389-5b3c-4b13-ad23-a8bc6bcd1850
title: Winlogon Notification Events
ms.topic: article
ms.date: 05/31/2018
---

# Winlogon Notification Events

[*Winlogon*](../secgloss/w-gly.md) can inform your notification package of the following events.



| Event                               | Description                                                                                                                                                                                                                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Lock**<br/>                 | This event occurs when the user locks the workstation.<br/>                                                                                                                                                                                                                                                   |
| **Logoff**<br/>               | This event occurs when a user logs off from the system. The **Logoff** event is performed synchronously, even if the notification package's registry settings indicate that it can handle events asynchronously.<br/>                                                                                         |
| **Logon**<br/>                | This event occurs when a user logs on the system.<br/> Note that the **Logon** event occurs before the user's network connections are restored. If your event handler requires access to the user's network connections, it should handle the **StartShell** event instead of the **Logon** event.<br/> |
| **Shutdown**<br/>             | This event occurs just before the system shuts down.<br/>                                                                                                                                                                                                                                                     |
| **SmartCardLogonNotify**<br/> | This event occurs when a user logs on to the system with a smart card.<br/>                                                                                                                                                                                                                                   |
| **StartScreenSaver**<br/>     | This event occurs when the screen saver has started. Typically, this happens after a user has been inactive for a set period of time.<br/> Functions handling this event should not display a user interface. **StartScreenSaver** event notification is intended for informational purposes only.<br/> |
| **StartShell**<br/>           | This event occurs after the user has logged onto the system, network connections have been established, and the user-specified shell program (usually Windows Explorer) has been started.<br/>                                                                                                                |
| **Startup**<br/>              | This event occurs when the system is started or restarted.<br/>                                                                                                                                                                                                                                               |
| **StopScreenSaver**<br/>      | This event occurs when the screen saver has stopped. Typically this happens when there is keyboard or mouse activity.<br/> Functions handling this event should not display a user interface. **StopScreenSaver** event notification is intended for informational purposes only.<br/>                  |
| **Unlock**<br/>               | This event occurs when the user unlocks the workstation or when a system administrator overrides the lock and logs the user off.<br/>                                                                                                                                                                         |



 

 

 
