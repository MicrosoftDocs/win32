---
description: Programmers and system administrators use service configuration programs to modify or query the database of installed services.
ms.assetid: 8ab97a4b-a4c2-4123-b5f5-27029bc3eb15
title: Service Configuration Programs
ms.topic: article
ms.date: 05/31/2018
---

# Service Configuration Programs

Programmers and system administrators use service configuration programs to modify or query the database of installed services. The database can also be accessed by using the registry functions. However, you should only use the SCM configuration functions, which ensure that the service is properly installed and configured.

The SCM configuration functions require either a handle to an SCManager object or a handle to a service object. To obtain these handles, the service configuration program must:

1.  Use the [**OpenSCManager**](/windows/desktop/api/Winsvc/nf-winsvc-openscmanagera) function to obtain a handle to the SCM database on a specified machine.
2.  Use the [**OpenService**](/windows/desktop/api/Winsvc/nf-winsvc-openservicea) or [**CreateService**](/windows/desktop/api/Winsvc/nf-winsvc-createservicea) function to obtain a handle to the service object.

For more information, see the following topics:

-   [Service Installation, Removal, and Enumeration](service-installation-removal-and-enumeration.md)
-   [Service Configuration](service-configuration.md)
-   [Configuring a Service Using SC](configuring-a-service-using-sc.md)

 

 



