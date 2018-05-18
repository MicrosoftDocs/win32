---
title: Communicating with Non-Windows Devices
description: Windows Sockets provides only a basic application level–naming convention (supported through IAS) to the IrDA-specified protocol suite.
ms.assetid: '94f06d3f-f3c0-4a19-b7a0-417c42e5fd05'
keywords: ["Infrared Data Association IrDA , described, non-Windows devices", "programming IrDA , communicating with non-Windows devices"]
---

# Communicating with Non-Windows Devices

Windows Sockets provides only a basic application level–naming convention (supported through IAS) to the IrDA-specified protocol suite. A non-Windows device that implements the core IrDA protocol and adheres to the simple naming conventions should be able to interoperate easily with Windows.

Devices can implement a Windows Sockets client, server, or both. The terms client and server refer only to the device that initiates the connection; once a connection is established, data can be reliably exchanged in both directions. Since server-side functionality requires slightly more IrDA stack functionality, it is anticipated that Windows will often host the server. Programmers choose the trigger that initiates the IrDA connection; the connection can be driven from a user-initiated action, or can be the result of discovering a device in a [*discovery polling loop*](d-gly.md#-irda-discovery-polling-loop-gly). Applications are not constrained in their implementation of client or server roles, or in connection establishment.

> [!Note]  
> Battery-constrained devices should refrain from continuous polling to drive connection initiation.

 

Either the client or server can close a connection, although this is generally coordinated by application-level protocols. A receiver receives all data sent to Windows Sockets by the peer application before it receives notification of the peer connection closure. If the connection aborts, both sides of the connection receive an error through Windows Sockets. As such, it is always possible to differentiate between graceful and abortive closes.

Well-designed servers can generally support multiple concurrent incoming connections. Simple servers are not required to implement multiple concurrent connection functionality.

 

 




