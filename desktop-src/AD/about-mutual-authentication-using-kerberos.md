---
title: About Mutual Authentication Using Kerberos
description: In mutual authentication, the client and service must verify their respective identities to each other before performing application functions.
ms.assetid: 5ce923d6-bede-4acb-b297-e93f2f506ea9
ms.tgt_platform: multiple
keywords:
- About Mutual Authentication Using Kerberos AD
ms.topic: article
ms.date: 05/31/2018
---

# About Mutual Authentication Using Kerberos

In mutual authentication, the client and service must verify their respective identities to each other before performing application functions. Neither party can perform operations with the other until identity has been verified; that is, the service must be able to verify the client without querying the client and the client must be able to verify the service without querying the service.

The value of a service that can authenticate a client is well-known. For example, a file service impersonates a client to determine which files the client can access.

The value of a client that can authenticate a service is less understood. Authenticating a service enables the client to trust the data that it gets from the service and to be secure in sending sensitive data to the service. The ability of a client to authenticate a service is particularly important in client/service applications that support delegation of the client's security context; that is, the client authorizes the service to act as its delegate in accessing additional services or network resources.

A service authenticates a client as follows: The client establishes a local security context either by executing in a previously established context, for example, in the session of a logged-in user, or by explicitly presenting credentials to the underlying security provider. The service cannot accept connections from any unauthenticated client.

The Kerberos mechanism by which a client authenticates a service works as follows: When a service is installed, a service installer, running with administrator privileges, registers one or more unique SPNs for each service instance. The names are registered in the Active Directory Domain Controller (DC) on the user or computer account object that the service instance will use to log on. When a client requests a connection to a service, it composes an SPN for a service instance, using known data or data provided by the user. The client then uses the SSPI negotiate package to present the SPN to the Key Distribution Center (KDC) for the client domain account. The KDC searches the forest for a user or computer account on which that SPN is registered. If the SPN is registered on more than one account, the authentication fails. Otherwise, the KDC encrypts a message using the password of the account on which the SPN was registered. The KDC passes this encrypted message to the client, which in turn passes it to the service instance. The service uses the SSPI negotiate package to decrypt the message, which it passes back to the client and on to the client's KDC. The KDC authenticates the service if the decrypted message matches its original message.

-   For more information about composing and registering SPNs, see .[Service Principal Names](service-principal-names.md)
-   For more information and a code example that composes an SPN for a Windows Sockets service that publishes itself with a service connection point, see [Composing the SPNs for a Service with an SCP](composing-the-spns-for-a-service-with-an-scp.md).
-   For more information and a code example that composes an SPN for an RPC service, see [Composing SPNs for an RpcNs Service](composing-spns-for-an-rpcns-service.md).

 

 




