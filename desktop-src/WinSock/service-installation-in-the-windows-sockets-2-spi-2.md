---
Description: Service installation in the Windows Sockets 2 (Winsock) SPI.
ms.assetid: a303fbcf-9122-422a-9b12-d00a5df0fc0f
title: Service Installation in the Windows Sockets 2 SPI
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Service Installation in the Windows Sockets 2 SPI

-   [**NSPInstallServiceClass**](/windows/win32/Ws2spi/nc-ws2spi-lpnspinstallserviceclass?branch=master)
-   [**NSPRemoveServiceClass**](/windows/win32/Ws2spi/nc-ws2spi-lpnspremoveserviceclass?branch=master)
-   [**NSPSetService**](/windows/win32/Ws2spi/nc-ws2spi-lpnspsetservice?branch=master)

When the required service class does not already exist, a namespace SPI client uses [**NSPInstallServiceClass**](/windows/win32/Ws2spi/nc-ws2spi-lpnspinstallserviceclass?branch=master) to install a new service class by supplying a service class name, a GUID for the service class identifier, and a series of [**WSANSCLASSINFO**](/windows/win32/Winsock2/ns-winsock2-_wsansclassinfow?branch=master) structures. These structures are each specific to a particular namespace, and supply common values such as recommended TCP port numbers or NetWare SAP Identifiers. A service class can be removed by calling [**NSPRemoveServiceClass**](/windows/win32/Ws2spi/nc-ws2spi-lpnspremoveserviceclass?branch=master) and supplying the GUID corresponding to the class identifier.

Once a service class exists, specific instances of a service can be installed or removed via [**NSPSetService**](/windows/win32/Ws2spi/nc-ws2spi-lpnspsetservice?branch=master). This function takes a [**WSAQUERYSET**](/windows/win32/Winsock2/ns-winsock2-_wsaquerysetw?branch=master) structure as an input parameter along with an operation code and operation flags. The operation code indicates whether the service is being installed or removed. The **WSAQUERYSET** structure provides all of the relevant information about the service including service class identifier, service name (for this instance), applicable namespace identifier and protocol information, and a set of transport addresses to which the service listens.

 

 



