---
title: Remote Desktop Protocol
description: The Microsoft Remote Desktop Protocol (RDP) provides remote display and input capabilities over network connections for Windows-based applications running on a server.
ms.assetid: 442c3c7f-d04b-4dcd-945d-f6e0168c59d5
ms.tgt_platform: multiple
keywords:
- Remote Desktop Protocol (RDP) Remote Desktop Services
- RDP (see Remote Desktop Protocol)
ms.topic: article
ms.date: 05/31/2018
---

# Remote Desktop Protocol

The Microsoft Remote Desktop Protocol (RDP) provides remote display and input capabilities over network connections for Windows-based applications running on a server. RDP is designed to support different types of network topologies and multiple LAN protocols.

> [!Note]  
> This topic is for software developers. If you are looking for user information for Remote Desktop, see [Windows Support](https://windows.microsoft.com/windows/support#1TC=windows-8). If you are looking for IT professional information for Remote Desktop, see [Remote Desktop Services on TechNet](/windows/deployment/deploy-whats-new).

 

## Basic Architecture

RDP is based on, and an extension of, the ITU T.120 family of protocols. RDP is a multiple-channel capable protocol that allows for separate virtual channels for carrying device communication and presentation data from the server, as well as encrypted client mouse and keyboard data. RDP provides an extensible base and supports up to 64,000 separate channels for data transmission and provisions for multipoint transmission.

On the server, RDP uses its own video driver to render display output by constructing the rendering information into network packets by using RDP protocol and sending them over the network to the client. On the client, RDP receives rendering data and interprets the packets into corresponding Microsoft Windows graphics device interface (GDI) API calls. For the input path, client mouse and keyboard events are redirected from the client to the server. On the server, RDP uses its own keyboard and mouse driver to receive these keyboard and mouse events.

In a Remote Desktop session, all environment variables—for example, variables determining color depth and wallpaper enabling and disabling—are determined by the RCP-Tcp connection settings. This applies to all functions and methods that set environment variables in the [Remote Desktop Web Connection Reference](remote-desktop-web-connection-reference.md) and the [Remote Desktop Services WMI Provider interface](terminal-services-wmi-provider-reference.md).

## Features

Microsoft RDP includes the following features and capabilities:

<dl> <dt>

<span id="Encryption"></span><span id="encryption"></span><span id="ENCRYPTION"></span>Encryption
</dt> <dd>

RDP uses RSA Security's RC4 cipher, a stream cipher designed to efficiently encrypt small amounts of data. RC4 is designed for secure communications over networks. Administrators can choose to encrypt data by using a 56- or 128-bit key.

</dd> <dt>

<span id="Bandwidth_reduction_features"></span><span id="bandwidth_reduction_features"></span><span id="BANDWIDTH_REDUCTION_FEATURES"></span>Bandwidth reduction features
</dt> <dd>

RDP supports various mechanisms to reduce the amount of data transmitted over a network connection. Mechanisms include data compression, persistent caching of bitmaps, and caching of glyphs and fragments in RAM. The persistent bitmap cache can provide a substantial improvement in performance over low-bandwidth connections, especially when running applications that make extensive use of large bitmaps.

</dd> <dt>

<span id="Roaming_disconnect"></span><span id="roaming_disconnect"></span><span id="ROAMING_DISCONNECT"></span>Roaming disconnect
</dt> <dd>

A user can manually disconnect from a remote desktop session without logging off. The user is automatically reconnected to their disconnected session when he or she logs back onto the system, either from the same device or a different device. When a user's session is unexpectedly terminated by a network or client failure, the user is disconnected but not logged off.

</dd> <dt>

<span id="Clipboard_mapping"></span><span id="clipboard_mapping"></span><span id="CLIPBOARD_MAPPING"></span>Clipboard mapping
</dt> <dd>

Users can delete, copy, and paste text and graphics between applications running on the local computer and those running in a remote desktop session, and between sessions.

</dd> <dt>

<span id="Print_redirection"></span><span id="print_redirection"></span><span id="PRINT_REDIRECTION"></span>Print redirection
</dt> <dd>

Applications running within a remote desktop session can print to a printer attached to the client device.

</dd> <dt>

<span id="Virtual_channels"></span><span id="virtual_channels"></span><span id="VIRTUAL_CHANNELS"></span>Virtual channels
</dt> <dd>

By using RDP virtual channel architecture, existing applications can be augmented and new applications can be developed to add features that require communications between the client device and an application running in a remote desktop session.

</dd> <dt>

<span id="Remote_control"></span><span id="remote_control"></span><span id="REMOTE_CONTROL"></span>Remote control
</dt> <dd>

Computer support staff can view and control a remote desktop session. Sharing input and display graphics between two remote desktop sessions gives a support person the ability to diagnose and resolve problems remotely.

</dd> <dt>

<span id="Network_load_balancing"></span><span id="network_load_balancing"></span><span id="NETWORK_LOAD_BALANCING"></span>Network load balancing
</dt> <dd>

RDP takes advantage of network load balancing (NLB), where available.

</dd> </dl>

In addition, RDP contains the following features:

-   Support for 24-bit color.
-   Improved performance over low-speed dial-up connections through reduced bandwidth.
-   Smart Card authentication through Remote Desktop Services.
-   Keyboard hooking. The ability to direct special Windows key combinations, in full-screen mode, to the local computer or to a remote computer.
-   Sound, drive, port, and network printer redirection. Sounds that occur on the remote computer can be heard on the client computer running the RDC client, and local client drives will be visible to the remote desktop session.

 

 