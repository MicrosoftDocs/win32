---
title: Service Publication
description: Services advertise themselves using objects stored in Active Directory Domain Services.
ms.assetid: 69e9256f-40ee-4aed-8213-1bbda0e508af
ms.tgt_platform: multiple
keywords:
- Service Publication AD
- Active Directory, using, service publication
ms.topic: article
ms.date: 05/31/2018
---

# Service Publication

Services advertise themselves using objects stored in Active Directory Domain Services. This is known as *service publication*. Clients query the directory to locate services. This is called *client-service rendezvous*. This section discusses the types of directory objects used for service publication and explains how they are used for client-service rendezvous.

This section discusses the following topics:

-   [An overview of service publication](about-service-publication.md)
-   [Security issues for service publication](security-issues-for-service-publication.md)
-   [Connection point objects](connection-points.md)
-   [Publishing with service connection points (SCPs)](publishing-with-service-connection-points.md)
-   [What information to store in a service connection point](service-connection-point-properties.md)
-   [Where to create a service connection point](where-to-create-a-service-connection-point.md)
-   [How to publish replicable, host-based, and database services using service connection points](service-connection-points-for-replicated-host-based-and-database-services.md)
-   [Creating and maintaining a service connection point](creating-and-maintaining-a-service-connection-point.md)
-   [How a client queries for an SCP and uses it to bind to a service instance](how-clients-find-and-use-a-service-connection-point.md)
-   [Using the RPC name service (RpcNs) APIs to publish an RPC service](publishing-with-the-rpc-name-service-rpcns.md)
-   [Windows Sockets registration and resolution (RnR) to publish a Windows Sockets service](publishing-with-windows-sockets-registration-and-resolution.md)
-   [Publication of COM-based services in the COM+ class store](publishing-com-services.md)

For more information about how services and clients authenticate each other, see [Mutual Authentication Using Kerberos](mutual-authentication-using-kerberos.md). For more information about service security contexts and logon accounts, see [Service Logon Accounts](service-logon-accounts.md).

 

 




