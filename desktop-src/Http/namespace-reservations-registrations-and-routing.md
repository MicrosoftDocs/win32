---
title: Namespace Reservations, Registrations, and Routing
description: Reservation and registration are the operations by which the HTTP Server API gives access to the URL namespace on a machine.
ms.assetid: dc66960b-36cd-4c09-be0a-3aec9a8a25d8
ms.topic: article
ms.date: 05/31/2018
---

# Namespace Reservations, Registrations, and Routing

Reservation and registration are the operations by which the HTTP Server API gives access to the URL namespace on a machine. Applications can register for a portion of the URL namespace in order to service requests from HTTP clients. The application registers a namespace with the HTTP Server API using the [**HttpAddUrl**](/windows/desktop/api/Http/nf-http-httpaddurl) function. The HTTP Server API adds the URLs to the request queue for the application and routes requests to the applications depending on the URLs in their queues. Before the application can register to receive requests for a URL namespace, however, the system administrator must make a reservation for that URL on behalf of the user running the application. By default, the namespace is closed, that is, only the administrator can register UrlPrefixes until the administrator enters a reservation.

A reservation persistently allocates a portion of the URL namespace to individual users allowing them to reserve or "own" that part of namespace. Reservations give the user the right to register to service requests for the namespace. The HTTP Server API ensures that users do not register URLs from portions of the namespace that they do not own. In order to ensure namespace security, ACLs (Access Control List) are applied to the portion of the namespace reserved for each user.

Reserved namespaces are identified by URL prefix strings, formatted in the same fashion as URL prefixes used for registrations. This means that all the various host specifier categories are also available for reservations.

Namespace reservations are persisted across reboots, and changes take effect dynamically so there is no need to stop and restart the machine.

The following concepts are further clarified as they apply to the process of registering and reserving namespaces.

-   REGISTRATION. Registration is the operation by which an application indicates interest in receiving requests for a specified UrlPrefix. The API for URL registration is [**HttpAddUrl**](/windows/desktop/api/Http/nf-http-httpaddurl). Registration typically occurs during application startup and must be performed each time the application starts.
-   ROUTING. Routing is performed by the HTTP Server API to determine the application to dispatch the request to, based on the best matching [UrlPrefix](urlprefix-strings.md) that is registered and/or reserved. The routing operation makes use of both registration and reservation information.
-   RESERVATION. Reservation allocates a portion of the URL namespace to one or more users. This operation gives users the right to register for the specified namespace. A user for whom a namespace is reserved is said to "own" that part of URL namespace. Namespace reservations are typically performed during the installation of the application and are an infrequent operation. Reservations persist across reboots of the machine and require administrator privileges on the machine or ownership with delegation privileges to create or delete.
-   DELEGATION. Delegation privileges allow a user who owns a namespace to hand off ownership of a subtree to another user by a subsequent reservation. Delegation privileges are granted to a user by the system administrator when the reservation is made. One or more than one user can be assigned delegation privileges to a namespace.

 

 




