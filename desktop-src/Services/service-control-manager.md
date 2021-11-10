---
title: Service control manager
description: The service control manager (SCM) is started at system boot. It's a remote procedure call (RPC) server, so that service configuration and service control programs can manipulate services on remote machines.
ms.assetid: 56ad011d-17c4-4410-b598-6ef47fb3638f
ms.topic: article
ms.date: 11/09/2021
---

# Service control manager

The service control manager (SCM) is started at system boot. It's a remote procedure call (RPC) server, so that service configuration and service control programs can manipulate services on remote machines.

The service functions provide an interface for the following tasks performed by the SCM:

-   Maintaining the database of installed services.
-   Starting services and driver services either upon system startup or upon demand.
-   Enumerating installed services and driver services.
-   Maintaining status information for running services and driver services.
-   Transmitting control requests to running services.
-   Locking and unlocking the service database.

The following sections describe the SCM in more detail:

-   [Database of installed services](database-of-installed-services.md)
-   [Automatically starting services](automatically-starting-services.md)
-   [Starting services on demand](starting-services-on-demand.md)
-   [Service record list](service-record-list.md)
-   [SCM handles](scm-handles.md)
