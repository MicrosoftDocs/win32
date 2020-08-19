---
title: Connection Points
description: A connection point object contains data about one or more instances of a service available on the network.
ms.assetid: eb810e6d-c220-4a24-ae12-b12ace237413
ms.tgt_platform: multiple
keywords:
- connection points AD
ms.topic: article
ms.date: 05/31/2018
---

# Connection Points

A connection point object contains data about one or more instances of a service available on the network. The [**connectionPoint**](/windows/desktop/ADSchema/c-connectionpoint) object class is the abstract base class from which objects representing connectable resources in Active Directory Domain Services are derived. The following illustration shows some of the object classes derived from the **connectionPoint** object class.

![object classes derived from the connectionpoint object class](images/connection-points.png)

The following table lists immediate subclasses of the [**connectionPoint**](/windows/desktop/ADSchema/c-connectionpoint) class.



| Object Class                                                    | Description                                                                                                                                                                                                                                                                                                              |
|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**serviceConnectionPoint**](/windows/desktop/ADSchema/c-serviceconnectionpoint) | Service connection point (SCP) objects for publishing data that client applications use to bind to a service. For more information, see [Publishing with Service Connection Points (SCPs)](publishing-with-service-connection-points.md).                                                                               |
| [**rpcEntry**](/windows/desktop/ADSchema/c-rpcentry)                             | An abstract class whose subclasses are used by the RPC Name Service (Ns) accessed through the **RpcNs\*** functions in the Win32 API. For more information, see [Publishing with the RPC Name Service (RpcNs)](publishing-with-the-rpc-name-service-rpcns.md).                                                          |
| [**serviceInstance**](/windows/desktop/ADSchema/c-serviceinstance)               | Connection point object used by the Windows Sockets Registration and Resolution (RnR) name service, accessed through the Windows Sockets **WSA\*** APIs. For more information, see [Publishing with Windows Sockets Registration and Resolution (RnR)](publishing-with-windows-sockets-registration-and-resolution.md). |
| [**printQueue**](/windows/desktop/ADSchema/c-printqueue)                         | Connection point object used to publish network printers. For more information, see [**IADsPrintQueue**](/windows/desktop/api/iads/nn-iads-iadsprintqueue).                                                                                                                                                                                           |
| [**volume**](/windows/desktop/ADSchema/c-volume)                                 | Connection point object used to publish file services.                                                                                                                                                                                                                                                                   |



 

Be aware that COM-based services do not use connection-point objects to advertise themselves. These services are published in the class store. The Windows 2000 class store is a directory-based repository for all COM-based applications, interfaces, and APIs that provide for application publishing and assigning. For more information, see [Publishing COM+ Services](publishing-com-services.md).

 

 