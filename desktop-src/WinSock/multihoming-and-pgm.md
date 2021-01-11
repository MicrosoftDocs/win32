---
description: Special consideration must be given to multihomed PGM senders or receivers. This page describes the considerations, and provides guidelines for best programming practices.
ms.assetid: 10fb56dd-3c96-4944-9b53-aee76c269528
title: Multihoming and PGM
ms.topic: article
ms.date: 05/31/2018
---

# Multihoming and PGM

Special consideration must be given to multihomed PGM senders or receivers. This page describes the considerations, and provides guidelines for best programming practices.

## Multihomed PGM Sender

When an application fails to specify an interface upon calling the [**connect**](/windows/desktop/api/Winsock2/nf-winsock2-connect) function, the first available interface is used. If no interface is available, **connect** fails.

When an application specifies an interface using the [RM\_SET\_SEND\_IF](socket-options.md) socket option, a [**bind**](/windows/desktop/api/winsock/nf-winsock-bind) attempt is made implicitly to that interface using TCP/IP, and fails if TCP/IP fails the bind request. If the interface is set using RM\_SET\_SEND\_IF multiple times, only the last interface set successfully is applicable.

Windows Sockets maintains which interface is set, and if that interface disappears, the session is disconnected.

## Multihomed PGM Receiver

When an application fails to specify an interface upon calling the [**listen**](/windows/desktop/api/Winsock2/nf-winsock2-listen) function, the default interface is used. If no interface is available, [**bind**](/windows/desktop/api/winsock/nf-winsock-bind) fails.

When an application specifies one or more interfaces on which to listen, using [RM\_ADD\_RECEIVE\_IF](socket-options.md), Windows Sockets attempts to bind to the requested interface or interfaces using TCP/IP. Any error from TCP/IP causes this request to fail. Unlike the PGM sender case, adding a receive interface multiple times result in the listens being posted on all the successfully added interfaces. Use the RM\_DEL\_RECEIVE\_IF socket option to stop listening on an interface.

Windows Sockets does not maintain state about multiple specified listening interfaces, and instead relies on TCP/IP to do so. Once a session is in progress, however, Windows Sockets track the incoming interface for that session, and if that interface disappears, Windows Sockets disconnects the session.

 

 



