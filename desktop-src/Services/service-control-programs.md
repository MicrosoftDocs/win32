---
Description: A service control program starts and controls services.
ms.assetid: e7ba295f-2937-44ad-89e8-40200c5e58b6
title: Service Control Programs
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Service Control Programs

A service control program starts and controls services. It performs the following actions:

-   Starts a service or driver service, if the start type is SERVICE\_DEMAND\_START.
-   Sends control requests to a running service.
-   Queries the current status of a running service.

These actions require an open handle to the service object. To obtain the handle, the service control program must:

1.  Use the [**OpenSCManager**](/windows/win32/Winsvc/nf-winsvc-openscmanagera?branch=master) function to obtain a handle to the SCM database on a specified machine.
2.  Use the [**OpenService**](/windows/win32/Winsvc/nf-winsvc-openservicea?branch=master) or [**CreateService**](/windows/win32/Winsvc/nf-winsvc-createservicea?branch=master) function to obtain a handle to the service object.

For more information, see the following topics:

-   [Service Startup](service-startup.md)
-   [Service Control Requests](service-control-requests.md)
-   [Controlling a Service Using SC](controlling-a-service-using-sc.md)

 

 



