---
description: A transport protocol must be properly installed on the system and registered with Windows Sockets to be accessible to an application.
ms.assetid: 45b20f66-4e12-44df-b64b-c96cd5b24cd4
title: Simultaneous Access to Multiple Transport Protocols
ms.topic: article
ms.date: 05/31/2018
---

# Simultaneous Access to Multiple Transport Protocols

A transport protocol must be properly installed on the system and registered with Windows Sockets to be accessible to an application. The Ws2\_32.dll library exports a set of functions to facilitate the registration process. This includes creating a new registration and removing an existing one.

When new registrations are created, the caller (that is, the stack vendor's installation script) supplies one or more filled in [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structures containing a complete set of information about the protocol. For more information, see [Windows Sockets 2 SPI](about-the-winsock-spi.md). Any transport stack installed in this manner is referred to as a Windows Sockets service provider.

On Windows XP with Service Pack 2 (SP2), Windows Server 2003 with Service Pack 1 (SP1), and Windows Vista and later. the Winsock catalog that contains a list of installed transport and namespace providers can be displayed in a command prompt with the following command:

**netsh winsock show catalog**

The Microsoft Windows Software Development Kit (SDK) includes *Sporder.exe*, which enables the user to view and modify the order in which service providers are enumerated. Using *Sporder.exe*, a user can manually establish a particular TCP/IP protocol stack as the default TCP/IP provider if more than one such stack is present.

The *Sporder.exe* application uses exported functions from *Sporder.dll* to reorder the service providers. As a result, installation applications can use the interface provided by *Sporder.dll* to programmatically reorder service providers.

-   [Layered Protocols and Protocol Chains](layered-protocols-and-protocol-chains-2.md)
-   [Using Multiple Protocols](using-multiple-protocols-2.md)
-   [Multiple Provider Restrictions on Select](multiple-provider-restrictions-on-select-2.md)

 

 
