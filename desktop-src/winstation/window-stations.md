---
title: Window Stations
description: A window station contains a clipboard, an atom table, and one or more desktop objects. Each window station object is a securable object. When a window station is created, it is associated with the calling process and assigned to the current session.
ms.assetid: 617661e2-3b0d-42a9-9769-2ba0957c31a8
keywords:
- window station objects
ms.topic: article
ms.date: 05/31/2018
---

# Window Stations

A *window station* contains a clipboard, an atom table, and one or more [desktop](desktops.md) objects. Each window station object is a securable object. When a window station is created, it is associated with the calling process and assigned to the current session.

The *interactive window station* is the only window station that can display a user interface or receive user input. It is assigned to the logon session of the interactive user, and contains the keyboard, mouse, and display device. It is always named "WinSta0". All other window stations are noninteractive, which means they cannot display a user interface or receive user input.

When a user logs on to a computer using Remote Desktop Services, a session is started for the user. Each session is associated with its own interactive window station named "WinSta0". For more information, see [Remote Desktop Sessions](/windows/desktop/TermServ/terminal-services-sessions).

For more information on window stations, see the following topics:

-   [Window Station and Desktop Creation](window-station-and-desktop-creation.md)
-   [Process Connection to a Window Station](process-connection-to-a-window-station.md)
-   [Window Station Security and Access Rights](window-station-security-and-access-rights.md)

 

 