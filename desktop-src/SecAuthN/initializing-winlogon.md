---
description: When Winlogon initializes, it registers the CTRL+ALT+DEL secure attention sequence (SAS) with the system, and then creates three desktops within the WinSta0 window station.
ms.assetid: 874aa12b-e213-4857-9600-698c28dfda37
title: Initializing Winlogon
ms.topic: article
ms.date: 05/31/2018
---

# Initializing Winlogon

When [Winlogon](winlogon.md) initializes, it registers the CTRL+ALT+DEL [*secure attention sequence*](../secgloss/s-gly.md) (SAS) with the system, and then creates three desktops within the WinSta0 window station.

Registering CTRL+ALT+DEL makes this initialization the first process, thus ensuring that no other application has hooked that key sequence.

WinSta0 is the name of the window station object that represents the physical screen, keyboard and mouse. Winlogon creates the following desktops in the WinSta0 object.



| Desktop              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Winlogon desktop     | This is the desktop that Winlogon and [*GINA*](../secgloss/g-gly.md) use for interactive identification and authentication, and other secure dialog boxes. Winlogon automatically switches to this desktop when it receives SAS event notification.                                                                                                                                                                                                                                                                                                                                                                          |
| Application desktop  | Each time a user successfully logs on, an application desktop is created for that [*logon session*](../secgloss/l-gly.md). The application desktop is also known as the default or user desktop. This desktop is where all user activity takes place. The application desktop is protected; only the system and the interactive logon session have access to it. Note that only a particular instance of the logged-on user has access to the desktop. If the interactive user activates a process using the service controller, that service application will not have access to the application desktop. |
| Screen saver desktop | This is the current desktop when a screen saver is running. If a user is logged on, both the system and the interactive logon session have access to the desktop. Otherwise, only the system has access to the desktop.                                                                                                                                                                                                                                                                                                                                                                                                                                      |



 

As the owner of these desktops, Winlogon can switch the current, or visible, desktop to any of the three desktops and allow the GINA access to this functionality. In general, GINA developers will not change the current desktop because Winlogon sets the desktop appropriately before communicating with the GINA. The description of each GINA function indicates which desktop is current for that call.



| For information about                                    | See                                                                                                      |
|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| The different states in which Winlogon can run           | [Winlogon States](winlogon-states.md)                                                                   |
| Time out operations                                      | [Supported Dialog Box Service Time-out Operations](supported-dialog-box-service-time-out-operations.md) |
| Sending messages to GINA while a dialog box is displayed | [Sending Messages to the GINA](sending-messages-to-the-gina.md)                                         |
| Support functions                                        | [Winlogon Support Functions](authentication-functions.md)                    |



 

 

 
