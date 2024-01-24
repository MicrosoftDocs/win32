---
description: Windows Sockets 2 (Winsock) enables programmers to create advanced Internet, intranet, and other network-capable applications to transmit application data across the wire, independent of the network protocol being used.
ms.assetid: 1ec8758a-40fd-4c98-b839-c2409ef712d6
title: Windows Sockets 2
ms.topic: article
ms.date: 05/31/2018
---

# Windows Sockets 2

## Purpose

Windows Sockets 2 (Winsock) enables programmers to create advanced Internet, intranet, and other network-capable applications to transmit application data across the wire, independent of the network protocol being used. With Winsock, programmers are provided access to advanced Microsoft® Windows® networking capabilities such as multicast and Quality of Service (QoS).

Winsock follows the Windows Open System Architecture (WOSA) model; it defines a standard service provider interface (SPI) between the application programming interface (API), with its exported functions and the protocol stacks. It uses the sockets paradigm that was first popularized by Berkeley Software Distribution (BSD) UNIX. It was later adapted for Windows in Windows Sockets 1.1, with which Windows Sockets 2 applications are backward compatible. Winsock programming previously centered around TCP/IP. Some programming practices that worked with TCP/IP do not work with every protocol. As a result, the Windows Sockets 2 API adds functions where necessary to handle several protocols.

## Developer audience

Windows Sockets 2 is designed for use by C/C++ programmers. Familiarity with Windows networking is required.

## Run-time requirements

Windows Sockets 2 can be used on all Windows platforms. Where certain implementations or capabilities of Windows Sockets 2 platform restrictions do exist, they are clearly noted in the documentation.

## In this section



| Topic                                                                                             | Description                                                                                                                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [What's New for Windows Sockets](what-s-new-for-windows-sockets-2.md)<br/>                 | Information on new features for Windows Sockets.<br/>                                                                                                                                                                                                                                 |
| [Winsock Network Protocol Support in Windows](network-protocol-support-in-windows.md)<br/> | Information on network protocol support for Windows Sockets on different versions of Windows.<br/>                                                                                                                                                                                    |
| [About Winsock](about-winsock.md)<br/>                                                     | General information on Windows Sockets programming considerations, architecture, and capabilities available to developers.<br/>                                                                                                                                                       |
| [Using Winsock](using-winsock.md)<br/>                                                     | Procedures and programming techniques used with Windows Sockets. This section includes basic Winsock programming techniques, such as [Getting Started With Winsock](getting-started-with-winsock.md), as well as advanced techniques useful for experienced Winsock developers.<br/> |
| [Winsock Reference](winsock-reference.md)<br/>                                             | Documentation of the Windows Sockets API.<br/>                                                                                                                                                                                                                                        |



 

## Related topics

<dl> <dt>

[IP Helper](../iphlp/ip-helper-start-page.md)
</dt> <dt>

[Quality of Service](/previous-versions/windows/desktop/qos/qos-start-page)
</dt> </dl>

 

 
