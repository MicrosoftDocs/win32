---
title: Desktops
description: A desktop has a logical display surface and contains user interface objects such as windows, menus, and hooks; it can be used to create and manage windows.
ms.assetid: 'c56cd63b-c260-40d0-9a62-1dee1eb18679'
keywords:
- desktop objects
ms.topic: article
ms.date: 05/31/2018
---

# Desktops

A *desktop* has a logical display surface and contains user interface objects such as windows, menus, and hooks; it can be used to create and manage windows. Each desktop object is a securable object. When a desktop is created, it is associated with the current [window station](window-stations.md) of the calling process and assigned to the calling thread.

Window messages can be sent only between processes that are on the same desktop. In addition, the hook procedure of a process running on a particular desktop can only receive messages intended for windows created in the same desktop.

The desktops associated with the interactive window station, Winsta0, can be made to display a user interface and receive user input, but only one of these desktops at a time is active. This active desktop, also known as the *input desktop*, is the one that is currently visible to the user and that receives user input. Applications can use the [**OpenInputDesktop**](/windows/win32/api/winuser/nf-winuser-openinputdesktop) function to get a handle to the input desktop. Applications that have the required access can use the [**SwitchDesktop**](/windows/win32/api/winuser/nf-winuser-switchdesktop) function to specify a different input desktop.

By default, there are three desktops in the interactive window station: Default, ScreenSaver, and Winlogon.

The Default desktop is created when Winlogon starts the initial process as the logged-on user. At that point, the Default desktop becomes active, and it is used to interact with the user.

Whenever a secure screen saver activates, the system automatically switches to the ScreenSaver desktop, which protects the processes on the default desktop from unauthorized users. Unsecured screen savers run on Winsta0\\Default.

The Winlogon desktop is active while a user logs on. The system switches to the default desktop when the shell indicates that it is ready to display something, or after thirty seconds, whichever comes first. During the user's session, the system switches to the Winlogon desktop when the user presses the CTRL+ALT+DEL key sequence, or when the User Account Control (UAC) dialog box is open.

**Windows Server 2003 and Windows XP/2000:** The UAC dialog box is not supported.

The Winlogon desktop's security descriptor allows access to a very restricted set of accounts, including the [LocalSystem account](/windows/desktop/Services/localsystem-account). Applications generally do not carry any of these accounts' SIDs in their tokens and therefore cannot access the Winlogon desktop or switch to a different desktop while the Winlogon desktop is active.

For more information, see the following topics:

-   [Window Station and Desktop Creation](window-station-and-desktop-creation.md)
-   [Thread Connection to a Desktop](thread-connection-to-a-desktop.md)
-   [Desktop Security and Access Rights](desktop-security-and-access-rights.md)

 

 