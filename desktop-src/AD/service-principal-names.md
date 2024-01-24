---
title: Service principal names
description: A service principal name (SPN) is a unique identifier of a service instance.
ms.assetid: 54b02853-4097-4e37-b7a2-6b5cfd168ece
ms.tgt_platform: multiple
keywords:
- Service Principal Names
- SPN see service principal names
- service principal name AD
- service principal name AD , about
ms.topic: article
ms.date: 02/06/2023
---

# Service principal names

A *service principal name (SPN)* is a unique identifier of a service instance. [Kerberos authentication](mutual-authentication-using-kerberos.md) uses SPNs to associate a service instance with a service sign-in account. Doing so allows a client application to request service authentication for an account even if the client doesn't have the account name.

If you install multiple instances of a service on computers throughout a forest, each instance must have its own SPN. If there are multiple names that clients can use for authentication, a service instance can have multiple SPNs. For example, because an SPN always includes the name of the host computer on which the service instance is running, a service instance might register multiple SPNs, one for each name or alias of its host. For more information about SPN format and composing a unique SPN, see [Name formats for unique SPNs](name-formats-for-unique-spns.md).

Before the Kerberos authentication service can use an SPN to authenticate a service, the SPN must be registered on the account object that the service instance uses to sign in. A given SPN can be registered on only one account. For Win32 services, a service installer specifies the sign-in account when an instance of the service is installed. The installer then composes the SPNs and writes them as a property of the account object in Active Directory Domain Services. If the sign-in account of a service instance changes, the SPNs must be re-registered under the new account. For more information, see [How a service registers its SPNs](how-a-service-registers-its-spns.md).

When a client wants to connect to a service, it locates an instance of the service, composes an SPN for that instance, connects to the service, and presents the SPN for the service to authenticate. For more information, see [How clients compose a service's SPN](how-clients-compose-a-serviceampaposs-spn.md).

## In this section

This section includes the following articles:

- [Name formats for unique SPNs](name-formats-for-unique-spns.md)
- [How a service composes its SPNs](how-a-service-composes-its-spns.md)
- [How a service registers its SPNs](how-a-service-registers-its-spns.md)
- [How clients compose a service's SPN](how-clients-compose-a-serviceampaposs-spn.md)

## See also

- [What is an SPN and why should you care?](/archive/blogs/autz_auth_stuff/what-is-a-spn-and-why-should-you-care)
- [Mutual authentication using Kerberos](mutual-authentication-using-kerberos.md)
