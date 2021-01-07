---
description: A service program contains executable code for one or more services.
ms.assetid: 697db543-6149-46ac-add3-c8c6ca3aadbe
title: Service Programs
ms.topic: article
ms.date: 05/31/2018
---

# Service Programs

A *service program* contains executable code for one or more services. A service program created with the type SERVICE\_WIN32\_OWN\_PROCESS contains the code for only one service. A service program created with the type SERVICE\_WIN32\_SHARE\_PROCESS contains code for more than one service, enabling them to share code. An example of a service program that does this is the generic service host process, Svchost.exe, which hosts internal Windows services. Note that Svchost.exe is reserved for use by the operating system and should not be used by non-Windows services. Instead, developers should implement their own service hosting programs.

A service program can be configured to execute in the context of a user account from either the built-in (local), primary, or trusted domain. It can also be configured to run in a special [service user account](service-user-accounts.md).

The following topics describe the interface requirements of the [service control manager](service-control-manager.md) (SCM) that a service program must include:

-   [Service Entry Point](service-entry-point.md)
-   [Service ServiceMain Function](service-servicemain-function.md)
-   [Service Control Handler Function](service-control-handler-function.md)

These topics do not apply to driver services. For interface requirements of driver services, see the Windows Driver Kit (WDK).

A service runs as a background process that can affect system performance, responsiveness, energy efficiency, and security. For service optimization guidelines, see [Developing Efficient Background Processes for Windows](/windows-hardware/drivers/kernel/implementing-power-management). The following topics describe additional programming considerations:

-   [Service State Transitions](service-status-transitions.md)
-   [Receiving Events in a Service](receiving-events-in-a-service.md)
-   [Multithreaded Services](multithreaded-services.md)
-   [Services and the Registry](services-and-the-registry.md)
-   [Services and Redirected Drives](services-and-redirected-drives.md)
-   [Service Trigger Events](service-trigger-events.md)

Note that if the service program functions as an RPC server, it should use dynamic endpoints and mutual authentication.

 

 
