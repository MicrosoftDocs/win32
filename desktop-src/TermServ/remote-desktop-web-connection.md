---
title: Remote Desktop Web Connection
description: Remote Desktop Web Connection is a web application consisting of an ActiveX control and a sample connection page.
ms.assetid: f9d252b0-205a-47df-9eca-d5744c09e079
ms.tgt_platform: multiple
keywords:
- Remote Desktop Web Connection Remote Desktop Services
- Remote Desktop Protocol (RDP) Remote Desktop Services , Remote Desktop Web Connection overview
ms.topic: article
ms.date: 05/31/2018
---

# Remote Desktop Web Connection

Remote Desktop Web Connection is a web application consisting of an ActiveX control and a sample connection page. When you deploy Remote Desktop Web Connection on a web server, you can provide client connectivity to Remote Desktop Session Host (RD Session Host) servers and other computers using Internet Explorer and TCP/IP.

## In this section

<dl> <dt>

[Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md)
</dt> <dd>

Lists the requirements for a Remote Desktop Web Connection.

</dd> <dt>

[Scriptable virtual channels](scriptable-virtual-channels.md)
</dt> <dd>

Describes changes to the programming model for implementing virtual channel applications that are provided by the Terminal Services Advanced Client (TSAC).

</dd> </dl>

The reference material for Remote Desktop Web Connection is included in the [Remote Desktop Web Connection Reference](remote-desktop-web-connection-reference.md) section.

For more information, see these topics:

-   [Implementing Scriptable Virtual Channels Using Remote Desktop Web Connection](implementing-scriptable-virtual-channels-using-remote-desktop-web-connection.md)
-   [Embedding the Remote Desktop ActiveX Control in a Webpage](embedding-the-remote-desktop-activex-control-in-a-web-page.md)
-   [Downloading and Using the Remote Desktop ActiveX Control](/previous-versions//aa380808(v=vs.85))
-   [Using the Remote Desktop ActiveX Control with Virtual Channels](using-the-remote-desktop-activex-control-with-virtual-channels.md)
-   [Providing for RDP Client Security](providing-for-rdp-client-security.md)
-   [Disabling Remote Desktop Services Features](disabling-terminal-services-features.md)

## Installing Remote Desktop Web Connection

The following steps install the Remote Desktop ActiveX control and sample webpage to the %systemroot%\\Web\\Tsweb directory. They share the webpage in the Tsweb directory on your server, for example, at https://*MyServer*/tsweb. The control (Msrdp.ocx) and the Remote Desktop Web Connection code are located in Msrdp.cab.

**To install Remote Desktop Web Connection**

1.  In the Add/Remove Programs item in Control Panel, under Add/Remove Windows Components, install Microsoft Internet Information Services (IIS).
2.  Install the World Wide Web Service subcomponent of IIS.
3.  Install the Remote Desktop Web Connection subcomponent of World Wide Web Service.

For a description of the webpage that is included with the installation of Remote Desktop Web Connection, see [Sample Webpage Included with the Remote Desktop ActiveX Control](sample-web-page-included-with-the-remote-desktop-activex-control.md).

 

 