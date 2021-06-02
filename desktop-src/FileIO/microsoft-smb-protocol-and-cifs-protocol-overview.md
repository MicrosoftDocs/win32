---
description: Describes the Microsoft implementation of the Server Message Block (SMB) Protocol.
ms.assetid: 641017fa-3721-40aa-b13c-e26c8b61ce5c
title: Microsoft SMB Protocol and CIFS Protocol Overview
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft SMB Protocol and CIFS Protocol Overview

The Server Message Block (SMB) Protocol is a network file sharing protocol, and as implemented in Microsoft Windows is known as Microsoft SMB Protocol. The set of message packets that defines a particular version of the protocol is called a dialect. The Common Internet File System (CIFS) Protocol is a dialect of SMB. Both SMB and CIFS are also available on VMS, several versions of Unix, and other operating systems.

The technical reference to CIFS is available from Microsoft Corporation at [Common Internet File System (CIFS) File Access Protocol](/openspecs/windows_protocols/ms-cifs/d416ff7c-c536-406e-a951-4f04b2fd1d2b).

Although its main purpose is file sharing, additional Microsoft SMB Protocol functionality includes the following:

-   [Dialect negotiation](microsoft-smb-protocol-dialects.md)
-   Determining other Microsoft SMB Protocol servers on the network, or network browsing
-   Printing over a network
-   [File, directory, and share access authentication](microsoft-smb-protocol-authentication.md)
-   File and record locking
-   File and directory change notification
-   Extended file attribute handling
-   Unicode support
-   [Opportunistic locks](opportunistic-locks.md)

In the OSI networking model, Microsoft SMB Protocol is most often used as an Application layer or a Presentation layer protocol, and it relies on lower-level protocols for transport. The transport layer protocol that Microsoft SMB Protocol is most often used with is NetBIOS over TCP/IP ([NBT](/previous-versions//bb870909(v=vs.85))). However, Microsoft SMB Protocol can also be used without a separate transport protocol the Microsoft SMB Protocol/NBT combination is generally used for backward compatibility.

The Microsoft SMB Protocol is a client-server implementation and consists of a set of data packets, each containing a request sent by the client or a response sent by the server. These packets can be broadly classified as follows:

-   Session control packets Establishes and discontinues a connection to shared server resources.
-   File access packets Accesses and manipulates files and directories on the remote server.
-   General message packets Sends data to print queues, mailslots, and named pipes, and provides data about the status of print queues.

Some message packets may be grouped and sent in one transmission to reduce response latency and increase network bandwidth. This is called "batching." The [Microsoft SMB Protocol Packet Exchange Scenario](microsoft-smb-protocol-packet-exchange-scenario.md) section describes an example of a Microsoft SMB Protocol session that uses packet batching.

## In this section



| Topic                                                                                                             | Description                                                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Microsoft SMB Protocol Dialects](microsoft-smb-protocol-dialects.md)<br/>                                 | To establish a connection between a client and a server using Microsoft SMB Protocol, you must first determine the dialect with the highest level of functionality that both the client and server support.<br/>                                                      |
| [Microsoft SMB Protocol Authentication](microsoft-smb-protocol-authentication.md)<br/>                     | The security model used in Microsoft SMB Protocol is identical to the one used by other variants of SMB, and consists of two levels of security user and share. A share is a file, directory, or printer that can be accessed by Microsoft SMB Protocol clients.<br/> |
| [Microsoft SMB Protocol Packet Exchange Scenario](microsoft-smb-protocol-packet-exchange-scenario.md)<br/> | Example of a Microsoft SMB Protocol packet exchange between a client and a server.<br/>                                                                                                                                                                               |



 

 

