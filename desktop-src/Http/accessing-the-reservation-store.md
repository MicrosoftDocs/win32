---
title: Accessing the Reservation Store
description: The HTTP Server API maintains the namespace reservation list for all users on the computer.
ms.assetid: 4b1291fc-cc62-4d4f-9150-18cbb1f6e5c0
keywords:
- Accessing the Reservation Store HTTP
- Reservation Store HTTP , Accessing
ms.topic: article
ms.date: 05/31/2018
---

# Accessing the Reservation Store

The HTTP Server API maintains the namespace reservation list for all users on the computer. A reservation entry consists of a [UrlPrefix](urlprefix-strings.md) and corresponding ACL. Each UrlPrefix in the store has an ACL that lists all the users that are permitted to register to receive requests for the namespace. Users with delegation privileges can delegate subtrees of the namespace that they own to other users or delete existing reservations using the configuration APIs.

To add a reservation to the persistent reservation store, the application calls the [**HttpSetServiceConfiguration**](/windows/desktop/api/Http/nf-http-httpsetserviceconfiguration) function with the configuration ID parameter set to the **HttpServiceConfigUrlAclInfo** value. The HTTP Server API verifies the ownership of the namespace and the user ID before adding a reservation to the store.

The HTTP Server API also supplies functions to query and delete the Service configurations for URL namespaces. The [**HttpQueryServiceConfiguration**](/windows/desktop/api/Http/nf-http-httpqueryserviceconfiguration) function called with the configuration ID parameter set to the **HttpServiceConfigUrlAclInfo** value queries, and the [**HttpDeleteServiceConfiguration**](/windows/desktop/api/Http/nf-http-httpdeleteserviceconfiguration) function deletes on the URL namespace store.

 

 




