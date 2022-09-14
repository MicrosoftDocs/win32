---
title: Mutual Authentication Using Kerberos
description: Mutual authentication is a security feature in which a client process must prove its identity to a service, and the service must prove its identity to the client, before any application traffic is transmitted over the client/service connection.
ms.assetid: 775dd350-5c70-4d97-aa2f-d21e9aecc778
ms.tgt_platform: multiple
keywords:
- Active Directory, using, mutual authentication
- Active Directory, using, security, mutual authentication
- security AD
- security AD , mutual authentication
ms.topic: article
ms.date: 05/31/2018
---

# Mutual Authentication Using Kerberos

Mutual authentication is a security feature in which a client process must prove its identity to a service, and the service must prove its identity to the client, before any application traffic is transmitted over the client/service connection.

Active Directory Domain Services and Windows provide support for service principal names (SPN), which are a key component in the Kerberos mechanism by which a client authenticates a service. An SPN is a unique name that identifies an instance of a service and is associated with the logon account under which the service instance runs. The components of an SPN are such that a client can compose an SPN for a service without the service logon account. This enables the client to request the service to authenticate its account even though the client does not have the account name.

This section includes an overview of:

-   Mutual authentication using Kerberos.
-   Composing a unique SPN.
-   How a service installer registers SPNs on the account object associated with a service instance.
-   How a client application uses a service instance's service connection point (SCP) object in Active Directory Domain Services to retrieve data from which to compose an SPN for the service.
-   How a client application uses a service SPN in conjunction with the Security Support Provider Interface (SSPI) to authenticate the service.
-   A code example for a Windows Sockets client/service application that uses an SCP and SSPI to perform mutual authentication.
-   A code example for an RPC client/service that performs mutual authentication using the RPC name service and RPC authentication.
-   How a Windows Sockets Registration and Resolution (RnR) service uses SPNs to perform mutual authentication.

This section discusses using Active Directory Domain Service for mutual authentication, in particular, the purpose of service connection points and service principal names in mutual authentication. It is not a complete discussion of how to use SSPI for mutual authentication or the authentication and security support available for RPC and Windows Sockets applications.

For more information, see:

-   [Publishing with service connection points](publishing-with-service-connection-points.md)
-   [SSPI](/windows/desktop/SecAuthN/sspi)
-   [Windows Sockets](/windows/desktop/WinSock/windows-sockets-start-page-2)
-   [RPC](/windows/desktop/Rpc/rpc-start-page)

 

 