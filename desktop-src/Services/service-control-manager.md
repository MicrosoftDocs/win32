---
description: The service control manager (SCM) is started at system boot. It is a remote procedure call (RPC) server, so that service configuration and service control programs can manipulate services on remote machines.
ms.assetid: 56ad011d-17c4-4410-b598-6ef47fb3638f
title: Service Control Manager
ms.topic: article
ms.date: 05/31/2018
---

# Service Control Manager

The service control manager (SCM) is started at system boot. It is a remote procedure call (RPC) server, so that service configuration and service control programs can manipulate services on remote machines.

The service functions provide an interface for the following tasks performed by the SCM:

-   Maintaining the database of installed services.
-   Starting services and driver services either upon system startup or upon demand.
-   Enumerating installed services and driver services.
-   Maintaining status information for running services and driver services.
-   Transmitting control requests to running services.
-   Locking and unlocking the service database.

The following sections describe the SCM in more detail:

-   [Database of Installed Services](database-of-installed-services.md)
-   [Automatically Starting Services](automatically-starting-services.md)
-   [Starting Services on Demand](starting-services-on-demand.md)
-   [Service Record List](service-record-list.md)
-   [SCM Handles](scm-handles.md)

 

 



