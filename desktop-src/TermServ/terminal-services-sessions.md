---
title: Remote Desktop Sessions
description: Because each logon to a Remote Desktop Connection (RDC) client receives a separate session ID, the user-experience is similar to being logged on to multiple computers at the same time; for example, an office computer and a home computer.
ms.assetid: 09a990cd-7590-4d73-b1f5-8736f0b4f17e
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Remote Desktop Sessions

When a user logs on to a Remote Desktop Services–enabled computer, a session is started for the user. Each session is identified by a unique session ID. Because each logon to a Remote Desktop Connection (RDC) client receives a separate session ID, the user-experience is similar to being logged on to multiple computers at the same time; for example, an office computer and a home computer.

Each remote desktop session is associated with an interactive window station. The only supported window station name for an interactive window station is "WinSta0"; therefore each session is associated with its own "WinSta0" window station. There are three standard desktops for each window station: the Winlogon desktop, the screen saver desktop, and the interactive desktop.

The user associated with the interactive window station for a session is known as the *interactive user*. On a Remote Desktop Connection (RDC) client there can be multiple interactive users in addition to the interactive user on the Remote Desktop Services console. To retrieve the identifier of the session currently attached to the console, use the [**WTSGetActiveConsoleSessionId**](/windows/desktop/api/Winbase/nf-winbase-wtsgetactiveconsolesessionid) function.

When a user logs off from a Remote Desktop Connection (RDC) client, the session that the client has on the Remote Desktop Session Host (RD Session Host) server (formerly known as a terminal server) is deleted and the window stations and desktops associated with that session are removed. However, because the Remote Desktop Services console session is never deleted, the window stations associated with the console session are not deleted. This affects how applications behave in a Remote Desktop Services environment when they are configured to run in the security context of the interactive user, also known as the "RunAs Interactive User" object activation mode.

For more information about starting a local server process on a specified session, see [Session-to-Session Activation with a Session Moniker](session-to-session-activation-with-a-session-moniker.md) and [Using a Session Moniker](using-a-session-moniker.md). For more information about security contexts, see [The Client's Security Context](/windows/desktop/SecAuthZ/the-client-security-context).

## Related topics

<dl> <dt>

[Child Sessions](child-sessions.md)
</dt> </dl>

 

 