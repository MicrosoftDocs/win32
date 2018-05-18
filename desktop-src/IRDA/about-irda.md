---
title: About IrDA
description: Infrared Data Association (IrDA) overview topic.
ms.assetid: '72709201-6519-4b5e-ba5d-6b9b3e07eb03'
keywords: ["Infrared Data Association IrDA , described", "infrared networking IrDA"]
---

# About IrDA

Infrared Data Association (IrDA) can be described as:

-   A protocol suite designed to provide wireless, line-of-sight connectivity between devices.
-   The semi-transparent red window found on many laptops and some desktop computers.
-   An organization that creates, promotes, and standardizes IrDA technology. For more information about the IrDA organization, see [www.irda.org](Http://go.microsoft.com/fwlink/p/?linkid=84072).

Microsoft supports IrDA on many of its Windows versions: Windows XP, Windows 2000, Windows Me, Windows 98, and Windows CE. IrDA is comprised of numerous core protocols and services; Windows provides more thorough support for certain core protocols and services, based on factors including inherent performance characteristics of certain protocols, serialization of data, and programmability. Such support, and recommended programming practices to make the best use of IrDA in Windows, are explained in the following sections:

-   [The Benefits of IrDA](the-benefits-of-irda.md)
-   [Windows IrDA Architecture](windows-irda-architecture.md)
-   [IrDA Programming with Windows Sockets](irda-programming-with-windows-sockets.md)
-   [IrDA and Windows Sockets Reference](irda-and-windows-sockets-reference.md)

IrDA on Windows provides core services similar to those exposed by Transmission Control Protocol (the TCP part of TCP/IP). Like TCP, applications on different devices can open multiple, reliable IrDA connections to send and receive data. Client IrDA applications connect to a server application by specifying a device address (similar to a TCP host IP address), and further specify their connection using an application address (similar to a TCP port).

Like many networking protocols and services, IrDA connectivity and data transfer are programmed through Windows Sockets function calls. The IrDA reference section explains how to use Windows Sockets functions and structures with IrDA protocols, services, and devices.

For more information about IrDA, see the topics listed in the following table.



| Section                                                                            | Content                                                                                                                                                                                           |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [The Benefits of IrDA](the-benefits-of-irda.md)                                   | Describes IrDA and illustrates the convenience of an IrDA-enabled application.                                                                                                                    |
| [Windows IrDA Architecture](windows-irda-architecture.md)                         | Describes the architecture of IrDA.                                                                                                                                                               |
| [IrDA Core Protocols and Services](irda-core-protocols-and-services.md)           | Explains IrDA core protocols and services, including transmission rates and usage recommendations for the Windows platform. Includes information about the limited support for IrCOMM on Windows. |
| [IrDA Programming with Windows Sockets](irda-programming-with-windows-sockets.md) | Explains how to program IrDA applications using Windows Sockets. Includes many examples to speed up IrDA performance and development time.                                                        |



 

 

 




