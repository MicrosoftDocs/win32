---
title: Child Sessions
description: Beginning with Windows Server 2012 and Windows 8, Remote Desktop supports the concept of a child session, which is a special loopback Remote Desktop session that is tied to a users existing session.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 65B9DB67-4EE8-40B5-B465-CA425792C62B
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Child Sessions

Beginning with Windows Server 2012 and Windows 8, Remote Desktop supports the concept of a *child session*, which is a special loopback Remote Desktop session that is tied to a user's existing session.

Child sessions are not supported on the following operating systems:

<dl> Windows RT  
Windows Server 2012 Server Core installation option  
Microsoft Hyper-V Server 2012  
</dl>

A system can only have one active and connected child session at any given time.

The child session can be terminated by logging off directly from it, or it will be terminated when its parent session terminates.

Before child sessions can be used on a system, you must enable the child session functionality by calling the [**WTSEnableChildSessions**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsenablechildsessions?branch=master) function. You can also determine if child sessions have been enabled by using the [**WTSIsChildSessionsEnabled**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsischildsessionsenabled?branch=master) function.

A child session can only be created from within an existing user's session by using the [Remote Desktop ActiveX control](remote-desktop-activex-control.md) and setting the "ConnectToChildSession" property with [**IMsRdpExtendedSettings.Property**](imsrdpextendedsettings-property.md) prior to connecting. When the [**IMsTscAx.Connect**](imstscax-connect.md) method is called, the Remote Desktop ActiveX control will automatically log on to the child session without prompting for credentials, except when the user is logged into the parent session using a smart card. Unlike a regular Remote Desktop session, a user does not need the Remote Interactive right to log on to the child session because this is a loopback session.

A child session cannot be locked. It will have no screen saver and no logon screen. Also, unlike a regular session, if the WinLogon logon text policy is set, the logon text will not be displayed in this child session. Also, there will be no effect of Remote Desktop Connection Timeout Group policies on the child session if these policies are set.

The following APIs are used in conjunction with child sessions:

-   [**WTSEnableChildSessions**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsenablechildsessions?branch=master)
-   [**WTSIsChildSessionsEnabled**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsischildsessionsenabled?branch=master)
-   [**WTSGetChildSessionId**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsgetchildsessionid?branch=master)
-   "ConnectToChildSession" property in [**IMsRdpExtendedSettings.Property**](imsrdpextendedsettings-property.md)

 

 




