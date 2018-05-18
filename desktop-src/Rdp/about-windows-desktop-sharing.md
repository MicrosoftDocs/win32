---
title: About Windows Desktop Sharing
description: There are two participants in Windows Desktop Sharing the sharer and the viewer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ef271727-4185-41e4-9e24-c96f4b390f27'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["Windows Desktop Sharing RDP , about"]
---

# About Windows Desktop Sharing

There are two participants in Windows Desktop Sharing: the sharer and the viewer. The *sharer* is the system whose screen is being shared out, while the *viewer* is the system that can view the sharer's screen.

For information on connecting from Windows to a Wireless Display (WiDi), please see [Project to a wireless display with Miracast](http://windows.microsoft.com/windows-8/project-wireless-screen-miracast).

## The Object Model

The only objects that can be co-created are the [**RDPSession**](rdpsession.md) object for creating a sharer instance, and the **RDPViewer** object for creating a viewer instance. All other objects are created and accessed through the methods of these objects.

An application groups the shareable windows within a process. Each application object contains a list of window objects. If an application object is shared, all its windows are shared.

An application filter manages the shared desktop area at the window and process level. Applications can use the enumerators to display lists of objects in the session that can be shared.

Attendee objects are created as a result of clients connecting to the session and being authenticated. After an attendee object is created it is automatically added to the attendees list.

Invitations enable a person or group of persons to connect to a session. When an attendee connects to a session, the client sends a ticket and a password. These two pieces of information are used to authenticate an attendee.

> [!Note]  
> Beginning with Windows 8 and Windows Server 2012, Windows Desktop Sharing uses the [Desktop Duplication API](https://msdn.microsoft.com/library/windows/desktop/hh404487). To ensure that your application will work correctly at all dots per inch (dpi) settings, your application must be DPI-aware. The recommended method for doing this is to configure the application manifest to mark your application as per-monitor DPI-aware as described in [Writing DPI-Aware Desktop and Win32 Applications](https://msdn.microsoft.com/library/windows/desktop/dn469266). This will set the application level when the application is launched.

 

## Security Concerns

If an application in a shared desktop or a shared application elevates, the viewer will not see the UAC prompt. This is by design.

A viewer cannot take control of a shared application running as an administrator. This is also by design.

## Related topics

<dl> <dt>

[Windows Desktop Sharing Reference](windows-desktop-sharing-reference.md)
</dt> </dl>

 

 




