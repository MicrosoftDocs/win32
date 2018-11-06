---
title: Security Issues for Service Publication
description: The system restricts the ability to create, modify, or delete connection point objects. Be aware of, and handle, these restrictions when you publish a service.
ms.assetid: 38e20a47-738d-4951-ad74-249039afeb52
ms.tgt_platform: multiple
keywords:
- Security Issues for Service Publication AD
- Active Directory, using, security, service publication security issues
ms.topic: article
ms.date: 05/31/2018
---

# Security Issues for Service Publication

The system restricts the ability to create, modify, or delete connection point objects. Be aware of, and handle, these restrictions when you publish a service.

Clients must be able to trust the data published in a connection point object in the directory. For this reason, permission to create a connection point object is typically restricted to privileged users, such as domain administrators. This prevents unauthorized users from deceiving clients by creating invalid connection points for well-known services.

Services must not run with domain administrator privileges. This means that a service typically cannot create its own connection point. Instead, you provide a service installation or configuration application that creates the connection point. This installer must be run by a user with the necessary privileges.

Although a service cannot typically create its connection point, it must be able to update the connection point properties at run time. The connection point properties contain the binding data used by clients to connect to the service. If the binding data changes, the service must update the connection point; otherwise, clients cannot use the service. This means that the installer must also modify the security descriptor on the connection point object to enable the service to read and write the appropriate properties at run time. For more information and a code example, see [Enabling Service Account to Access SCP Properties](enabling-service-account-to-access-scp-properties.md).

A service running under the LocalSystem account can create a connection point as a child object under its own computer object in the directory. Such a service is an exception to the rule of services not creating their own connection points. A LocalSystem service also has permission to modify the properties of connection point objects under its own computer object. Be aware that a service should run under the LocalSystem account only if absolutely necessary. For more information, see [Guidelines for Selecting a Service Logon Account](guidelines-for-selecting-a-service-logon-account.md).

The application that creates a connection point object, or any object, must have create child permissions for the object class to be created in the container where the object will be created. To remove an object, the process performing the operation must have delete child permissions for the object class to be deleted on the container holding the object, or have delete permissions on the object itself. To update a connection point the process performing the operation must have write-access to the properties to be updated on the object.

 

 




