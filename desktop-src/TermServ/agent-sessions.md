---
title: Agent Sessions
description: Agent sessions is a session type similar to Child sessions, used for performing background tasks.
ms.assetid: b9d06cbd-e0b3-45fe-ab0c-a2f3760b2fdf
ms.tgt_platform: multiple
ms.topic: reference
ms.date: 08/20/2025
---

# Agent Sessions

The agent session can be terminated by logging off directly from it, or it will be terminated when its parent session terminates.

An agent session can only be created from within an existing user's session by using the [Remote Desktop ActiveX control](remote-desktop-activex-control.md) and setting the "ConnectToAgentSession" property with [**IMsRdpExtendedSettings.Property**](imsrdpextendedsettings-property.md) prior to connecting. When the [**IMsTscAx.Connect**](imstscax-connect.md) method is called, the Remote Desktop ActiveX control will automatically log on to the agent session without prompting for credentials, except when the user is logged into the parent session using a smart card.

An agent session cannot be locked. It will have no screen saver and no logon screen. Also, unlike a regular session, if the WinLogon logon text policy is set, the logon text will not be displayed in this session. Also, there will be no effect of Remote Desktop Connection Timeout Group policies on the session if these policies are set.
