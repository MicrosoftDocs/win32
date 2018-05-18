---
Description: 'A service control program starts and controls services.'
ms.assetid: 'e7ba295f-2937-44ad-89e8-40200c5e58b6'
title: Service Control Programs
---

# Service Control Programs

A service control program starts and controls services. It performs the following actions:

-   Starts a service or driver service, if the start type is SERVICE\_DEMAND\_START.
-   Sends control requests to a running service.
-   Queries the current status of a running service.

These actions require an open handle to the service object. To obtain the handle, the service control program must:

1.  Use the [**OpenSCManager**](openscmanager.md) function to obtain a handle to the SCM database on a specified machine.
2.  Use the [**OpenService**](openservice.md) or [**CreateService**](createservice.md) function to obtain a handle to the service object.

For more information, see the following topics:

-   [Service Startup](service-startup.md)
-   [Service Control Requests](service-control-requests.md)
-   [Controlling a Service Using SC](controlling-a-service-using-sc.md)

 

 



