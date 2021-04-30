---
description: In some circumstances, a server application needs to present a clients identity to resources it accesses on the clients behalf, usually to cause access checks or authentication to be performed against the clients identity.
ms.assetid: fd75eb54-eefe-411f-a7aa-0bc8628f8778
title: Client Impersonation and Delegation
ms.topic: article
ms.date: 05/31/2018
---

# Client Impersonation and Delegation

In some circumstances, a server application needs to present a client's identity to resources it accesses on the client's behalf, usually to cause access checks or authentication to be performed against the client's identity. To a certain extent, the server can act under the client's identity—an action referred to as impersonating the client.

*Impersonation* is the ability of a thread to execute in a security context different from that of the process owning the thread. The server thread uses an access token representing the client's credentials, and with this, it can access resources that the client can access.

Using impersonation ensures that the server can do precisely what the client can do. Access to resources may be either restricted or expanded, depending on what the client has permission to do.

You might choose to have a server impersonate a client when connecting to a database so that the database can authenticate and authorize the client for itself. Or, if your application accesses files that are protected with a security descriptor and to enable the client to obtain authorized access to information in these files, the application can impersonate the client before accessing the files.

## How to Implement Impersonation

Impersonation requires participation by both client and server (and, in some cases, system administrators). The client must indicate its willingness to let the server use its identity, and the server must explicitly assume the client's identity programmatically. For details, see the topics [Client-Side Requirements for Impersonation](client-side-requirements-for-impersonation.md) and [Server-Side Requirements for Impersonation](server-side-requirements-for-impersonation.md).

## Administrative Requirements for Delegate-Level Impersonation

To effectively use the most powerful form of impersonation, *delegation*, which is the impersonation of clients over the network, the client and server user accounts must be properly configured in the Active Directory Service to support it (in addition to the client granting authority to do delegate-level impersonation), as follows:

-   The server identity must be marked as "Trusted for delegation" in the Active Directory Service.
-   The client identity must not be marked as "Account is sensitive and cannot be delegated" in the Active Directory Service.

These configuration features give the domain administrator a high degree of control over delegation, which is desirable, given how much trust (and hence security risk) is involved. For more detail about delegation, see [Delegation and Impersonation](/windows/desktop/com/delegation-and-impersonation).

## Cloaking

Along with the authority a client grants a server through the impersonation level, the server's cloaking capability largely determines how impersonation will behave. Cloaking affects what identity is actually presented by the server when it makes calls on the client's behalf—its own or the client's. For details, see [Cloaking](cloaking.md).

## Performance Implications

Impersonation can significantly affect performance and scaling. It is generally more expensive to impersonate a client on a call than to make the call directly. Following are some of the issues to consider:

-   The computational overhead of passing around identity in complicated patterns, particularly if dynamic cloaking is enabled.
-   The general complexity of enforcing redundant security checking in numerous places, instead of just centrally in the middle tier.
-   Resources such as database connections, when opened impersonating a client, cannot be reused across multiple clients—a very large roadblock to scaling well.

Sometimes the only effective solution to a problem is to use impersonation, but this decision should be carefully weighed. For a further discussion of these issues, see [Multi-Tier Application Security](multi-tier-application-security.md).

## Queued Components

[Queued components](com--queued-components.md) do not support impersonation. When a client makes a call to a queued object, the call is actually made to the recorder, which packages it as part of a message to the server. The listener then reads the message from the queue and passes it to the player, which invokes the actual server component and makes the same method call. As such, when the server receives the call, the original client token is unavailable via impersonation. Role-based security still applies, however, and programmatic security using the [**ISecurityCallContext**](/windows/desktop/api/ComSvcs/nn-comsvcs-isecuritycallcontext) interface will work. For details, see [Queued Components Security](queued-components-security.md).

## Related topics

<dl> <dt>

[Client Authentication](client-authentication.md)
</dt> <dt>

[Library Application Security](library-application-security.md)
</dt> <dt>

[Multi-Tier Application Security](multi-tier-application-security.md)
</dt> <dt>

[Programmatic Component Security](programmatic-component-security.md)
</dt> <dt>

[Role-Based Security Administration](role-based-security-administration.md)
</dt> <dt>

[Using the Software Restriction Policy in COM+](using-the-software-restriction-policy-in-com-.md)
</dt> </dl>

 

 
