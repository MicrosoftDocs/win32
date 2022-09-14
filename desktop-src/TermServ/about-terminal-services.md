---
title: About Remote Desktop Services
description: Remote Desktop Services (formerly known as Terminal Services) provides functionality similar to a terminal-based, centralized host, or mainframe, environment in which multiple terminals connect to a host computer.
ms.assetid: 5b5b0f97-f973-4f52-a965-c9c2390e6c8d
ms.tgt_platform: multiple
keywords:
- Remote Desktop Services Remote Desktop Services , about
ms.topic: article
ms.date: 05/31/2018
---

# About Remote Desktop Services

Remote Desktop Services (formerly known as Terminal Services) provides functionality similar to a terminal-based, centralized host, or mainframe, environment in which multiple terminals connect to a host computer. Each terminal provides a conduit for input and output between a user and the host computer. A user can log on at a terminal, and then run applications on the host computer, accessing files, databases, network resources, and so on. Each terminal session is independent, with the host operating system managing conflicts between multiple users contending for shared resources.

The primary difference between Remote Desktop Services and the traditional mainframe environment is that the dumb terminals in a mainframe environment only provide character-based input and output. A Remote Desktop Connection (RDC) client or emulator provides a complete graphical user interface including a Windows operating system desktop and support for a variety of input devices, such as a keyboard and mouse.

In the Remote Desktop Services environment, an application runs entirely on the Remote Desktop Session Host (RD Session Host) server (formerly known as a terminal server). The RDC client performs no local processing of application software. The server transmits the graphical user interface to the client. The client transmits the user's input back to the server.

For more information, see the following topics.

## In this section

<dl> <dt>

[Modify Device Redirection Default](modify-device-redirection-default-.md)
</dt> <dd>

Because Remote Desktop Gateway servers attempt to enforce secure device redirection policies before passing the client connection through to a Remote Desktop Session Host server, you may need to disable this default in some cases.

</dd> <dt>

[Remote Desktop Protocol](remote-desktop-protocol.md)
</dt> <dd>

The Microsoft Remote Desktop Protocol (RDP) provides remote display and input capabilities over network connections for Windows-based applications running on a server.

</dd> <dt>

[Remote Desktop Services API](terminal-services-api.md)
</dt> <dd>

The Remote Desktop Services API is primarily useful to client/server applications and applications for Remote Desktop Services administration.

</dd> <dt>

[Remote Desktop Services management applications](terminal-services-management-applications.md)
</dt> <dd>

Describes the management applications that Remote Desktop Services supports.

</dd> <dt>

[Remote Desktop Services programming guidelines](terminal-services-programming-guidelines.md)
</dt> <dd>

Topics that provide guidelines for developing applications in a Remote Desktop Services environment.

</dd> <dt>

[Remote Desktop Sessions](terminal-services-sessions.md)
</dt> <dd>

Because each logon to a Remote Desktop Connection (RDC) client receives a separate session ID, the user-experience is similar to being logged on to multiple computers at the same time; for example, an office computer and a home computer.

</dd> <dt>

[Remote Desktop Web Connection](remote-desktop-web-connection.md)
</dt> <dd>

Describes how to install a Remote Desktop Web Connection.

</dd> <dt>

[Resources on a Remote Desktop Session Host Server](resources-on-a-terminal-server.md)
</dt> <dd>

Multiple users can log on simultaneously to a single RD Session Host server, sharing the hardware and software resources of the server.

</dd> <dt>

[What's New in Remote Desktop Services](what-s-new-in-terminal-services.md)
</dt> <dd>

Topics that describe the changes in each release of the Remote Desktop Services API.

</dd> </dl>

## Related topics

<dl> <dt>

[Connect to another computer using Remote Desktop Connection](https://windows.microsoft.com/windows/connect-using-remote-desktop-connection#connect-using-remote-desktop-connection=windows-7)
</dt> </dl>

 

 




