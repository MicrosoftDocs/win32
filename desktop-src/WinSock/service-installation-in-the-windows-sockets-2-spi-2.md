---
Description: 'Service installation in the Windows Sockets 2 (Winsock) SPI.'
ms.assetid: 'a303fbcf-9122-422a-9b12-d00a5df0fc0f'
title: Service Installation in the Windows Sockets 2 SPI
---

# Service Installation in the Windows Sockets 2 SPI

-   [**NSPInstallServiceClass**](nspinstallserviceclass-2.md)
-   [**NSPRemoveServiceClass**](nspremoveserviceclass-2.md)
-   [**NSPSetService**](nspsetservice-2.md)

When the required service class does not already exist, a namespace SPI client uses [**NSPInstallServiceClass**](nspinstallserviceclass-2.md) to install a new service class by supplying a service class name, a GUID for the service class identifier, and a series of [**WSANSCLASSINFO**](wsansclassinfo.md) structures. These structures are each specific to a particular namespace, and supply common values such as recommended TCP port numbers or NetWare SAP Identifiers. A service class can be removed by calling [**NSPRemoveServiceClass**](nspremoveserviceclass-2.md) and supplying the GUID corresponding to the class identifier.

Once a service class exists, specific instances of a service can be installed or removed via [**NSPSetService**](nspsetservice-2.md). This function takes a [**WSAQUERYSET**](wsaqueryset-2.md) structure as an input parameter along with an operation code and operation flags. The operation code indicates whether the service is being installed or removed. The **WSAQUERYSET** structure provides all of the relevant information about the service including service class identifier, service name (for this instance), applicable namespace identifier and protocol information, and a set of transport addresses to which the service listens.

 

 



