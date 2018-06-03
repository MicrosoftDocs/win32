---
title: Limited Windows Support for IrCOMM Programming
description: Windows implements a subset of the IrCOMM protocol to support certain legacy applications, but that support is considered legacy, and is not recommended for new applications.
ms.assetid: 061ff792-06a9-49ea-a6e6-8a4768666c87
keywords:
- IrCOMM IrDA , programming support
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Limited Windows Support for IrCOMM Programming

Windows implements a subset of the IrCOMM protocol to support certain legacy applications, but that support is considered legacy, and is not recommended for new applications. Instead of IrCOMM, Windows Sockets is the recommended programming interface for IrDA on all Windows platforms.

Windows exposes the IrCOMM protocol through Telephony or Windows Sockets APIs. There are several reasons why Windows does not expose IrCOMM virtual serial ports, and why Windows Sockets is the recommended programming interface instead of IrCOMM:

-   IrCOMM runs on top of a reliable protocol layer, but session establishment and release services are not exposed through the serial API. Also, since the underlying IrDA connection can be broken and re-established without the event being communicated to the application through the serial API, IrCOMM is not a reliable protocol in practice. As such, IrCOMM applications must be prepared to add another layer of reliability.
-   Multiple applications cannot share a virtual serial port. This condition is particularly troublesome in many situations. For example, if an IrCOMM-based application opens the single virtual serial port and holds it open until system shutdown, the virtual serial port is unavailable for any other operation. An example is an IrTran-P file transfer application running as a background service; no other IrDA application or driver can run on that system, even though the underlying IrDA protocols provide support to allow multiple applications to be waiting for incoming connections and allow clients to select a target application at connect time through established protocol mechanisms.
-   Windows support for multiple concurrent adapters, or IrDA connections to different devices, cannot be well supported with an API and protocol that assumes a single-device connection, such as IrCOMM does.
-   The complexity and various modes of IrCOMM make real-world interoperability a difficult problem to overcome.

Unfortunately, the fundamental limitation of the IrCOMM protocol, which is that multiple servers cannot concurrently listen for incoming connections, is still exposed in this implementation. If one application is listening for incoming IrCOMM connections, another application trying to do so will get an error from Windows Sockets. This means that all new applications should either avoid IrCOMM or support multiple modes concurrently. Details for using IrCOMM through Windows Sockets can be found in [IrCOMM Server Sample Code](ircomm-server-sample-code.md) and [IrCOMM Client Sample Code](ircomm-client-sample-code.md).

 

 




