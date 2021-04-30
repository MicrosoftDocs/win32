---
title: Remote Desktop Services (Remote Desktop Services)
description: Microsoft Remote Desktop Services is remote PC access software that supports remote desktop access. Remote Desktop Services connects multiple clients to a Remote Desktop Session Host (RD Session Host) server.
ms.assetid: 90c40b7a-e324-43fc-a1e6-f29997ed9436
ms.tgt_platform: multiple
keywords:
- Remote Desktop Services Remote Desktop Services
- Remote Desktop Services Remote Desktop Services , home page
- Terminal Services See Remote Desktop Services Remote Desktop Services
ms.topic: article
ms.date: 05/31/2018
---

# Remote Desktop Services (Remote Desktop Services)

## Purpose

Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2, or Windows Server 2008 with Remote Desktop Services (formerly known as Terminal Services) allow a server to host multiple, simultaneous client sessions. Remote Desktop uses Remote Desktop Services technology to allow a single session to run remotely. A user can connect to a Remote Desktop Session Host (RD Session Host) server (formerly known as a terminal server) by using Remote Desktop Connection (RDC) client software. The Remote Desktop Web Connection extends Remote Desktop Services technology to the web.

> [!Note]  
> This topic is for software developers. If you are looking for user information for Remote Desktop connections, See [Remote Desktop Connection: frequently asked questions](https://windows.microsoft.com/windows/remote-desktop-connection-faq#1TC=windows-8).

 

## Where applicable

A Remote Desktop Connection (RDC) client can exist in a variety of forms. Thin-client hardware devices that run an embedded Windows-based operating system can run the RDC client software to connect to an RD Session Host server. Windows-, Macintosh-, or UNIX-based computers can run RDC client software to connect to an RD Session Host server to display Windows-based applications. This combination of RDC clients provides access to Windows-based applications from virtually any operating system.

## Developer audience

Developers who use Remote Desktop Services should be familiar with the C and C++ programming languages and the Windows-based programming environment. Familiarity with client/server architecture is required. The Remote Desktop Web Connection includes scriptable interfaces to create and deploy scriptable virtual channels within Remote Desktop Services web applications.

## Run-time requirements

Applications that use Remote Desktop Services require Windows Server 2012 R2, Windows 8.1, Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, or Windows Vista. To use Remote Desktop Web Connection functionality, the Remote Desktop Services client application requires Internet Explorer and a connection to the World Wide Web. For information about run-time requirements for a particular programming element, see the Requirements section of the reference page for that element.

## In this section

<dl> <dt>

[Remote Desktop ActiveX control](remote-desktop-activex-control.md)
</dt> <dd>

Describes how to use the Remote Desktop ActiveX control.

</dd> <dt>

[Remote Desktop Protocol Provider API](custom-remote-desktop-protocols.md)
</dt> <dd>

You use the Remote Desktop Protocol Provider API to create a protocol to provide communication between the Remote Desktop Services service and multiple clients.

</dd> <dt>

[Remote Desktop Services virtual channels](terminal-services-virtual-channels.md)
</dt> <dd>

*Virtual channels* are software extensions that can be used to add functional enhancements to a Remote Desktop Services application.

</dd> <dt>

[RemoteFX Media Redirection API](remotefx-api.md)
</dt> <dd>

The RemoteFX Media Redirection API is used in a Remote Desktop session to identify areas of the server that are displaying fast changing content, such as video. This content can then be video encoded and sent to the client in encoded format.

</dd> <dt>

[Remote Desktop Connection Broker client API](connection-broker-client-api.md)
</dt> <dd>

Describes how to use the Remote Desktop Connection Broker client API.

</dd> <dt>

[Personal desktop task agent API reference](task-agent-api-reference.md)
</dt> <dd>

The personal desktop task agent API is used to handle scheduled updates to a personal virtual desktop.

</dd> <dt>

[About Remote Desktop Services](about-terminal-services.md)
</dt> <dd>

Remote Desktop Services (formerly known as Terminal Services) provides functionality similar to a terminal-based, centralized host, or mainframe, environment in which multiple terminals connect to a host computer.

</dd> <dt>

[Remote Desktop Management Services Provider](rdms-api-reference.md)
</dt> <dd>

The Remote Desktop Management Services (RDMS) Provider manages virtual desktop infrastructure (VDI) environments.

</dd> <dt>

[Remote Desktop Services reference](terminal-services-reference.md)
</dt> <dd>

Documentation of property methods that you can use to examine and configure Remote Desktop Services user properties. Remote Desktop Services functions, structures, and Remote Desktop Web Connection scriptable interfaces are also documented.

</dd> <dt>

[Remote Desktop Services Shortcut Keys](terminal-services-shortcut-keys.md)
</dt> <dd>

A list of the Remote Desktop Services shortcut keys.

</dd> <dt>

[Remote Desktop Services WMI provider](terminal-services-wmi-provider.md)
</dt> <dd>

The Remote Desktop Services WMI provider provides programmatic access to the information and settings that are exposed by the Remote Desktop Services Configuration/Connections Microsoft Management Console (MMC) snap-in.

</dd> <dt>

[Using Remote Desktop Services](using-terminal-services.md)
</dt> <dd>

How to program in the Remote Desktop Services environment and how to extend Remote Desktop Services (formerly known as Terminal Services) technology to the web by using Remote Desktop Web Connection.

</dd> </dl>

## Related topics

<dl> <dt>

[Terminal Services Is Now Remote Desktop Services](terminal-services-is-now-remote-desktop-services.md)
</dt> </dl>

 

 




