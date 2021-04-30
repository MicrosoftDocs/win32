---
description: The service control manager (SCM) maintains a database of installed services and driver services, and provides a unified and secure means of controlling them.
ms.assetid: a3af8340-d367-417b-9759-7282edf1d694
title: About Services
ms.topic: article
ms.date: 05/31/2018
---

# About Services

The [service control manager](service-control-manager.md) (SCM) maintains a database of installed services and driver services, and provides a unified and secure means of controlling them. The database includes information on how each service or driver service should be started. It also enables system administrators to customize security requirements for each service and thereby control access to the service.

The following types of programs use the functions provided by the SCM.



| Type                          | Description                                                                                                                                                                                                                                                                                                                               |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Service program               | A program that provides executable code for one or more services. Service programs use functions that connect to the SCM and send status information to the SCM.                                                                                                                                                                          |
| Service configuration program | A program that queries or modifies the services database. Service configuration programs use functions that open the database, install or delete services in the database, and query or modify the configuration and security parameters for installed services. Service configuration programs manage both services and driver services. |
| Service control program       | A program that starts and controls services and driver services. Service control programs use functions that send requests to the SCM, which carries out the request.                                                                                                                                                                     |



 

This overview discusses the following topics:

-   [Service Control Manager](service-control-manager.md)
-   [Service Programs](service-programs.md)
-   [Service Configuration Programs](service-configuration-programs.md)
-   [Service Control Programs](service-control-programs.md)
-   [Service User Accounts](service-user-accounts.md)
-   [Interactive Services](interactive-services.md)
-   [Service Security and Access Rights](service-security-and-access-rights.md)
-   [Debugging a Service](debugging-a-service.md)
-   [Service Trigger Events](service-trigger-events.md)

 

 



