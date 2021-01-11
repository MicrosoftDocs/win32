---
description: In a client/server application protocol, a server binds to a communication port such as a socket or an RPC interface.
ms.assetid: 176d4ca5-83dd-42ef-b116-227d4badc0dd
title: Establishing a Secure Connection with Authentication
ms.topic: article
ms.date: 05/31/2018
---

# Establishing a Secure Connection with Authentication

In a client/server [*application protocol*](/windows/desktop/SecGloss/a-gly), a server binds to a communication port such as a socket or an RPC interface. The server then waits for a client to connect and request service. The role of security at connection setup is two-fold in the case of mutual authentication:

-   Client authentication by the server.
-   Server authentication by the client.

The client and server components of a transport application use a [*security package*](/windows/desktop/SecGloss/s-gly) to establish a secure connection for transmitting messages. The first step in establishing a secure connection is to create a [*security context*](/windows/desktop/SecGloss/s-gly); that is, an opaque data structure that contains the security data relevant to a connection, such as a [*session key*](/windows/desktop/SecGloss/s-gly) and the duration of the session.

A security context is essentially a message from the security package associated with the client to the security package associated with the server. Consequently, creating a security context typically requires both client and server to make calls to their respective security packages. For more information on context functions, see [Context Management](authentication-functions.md).

The protocol used to establish a secure, authenticated connection involves the exchange of one or more "security tokens" between the client and the server. These tokens are sent as opaque messages by the two sides along with any other [*application protocol*](/windows/desktop/SecGloss/a-gly)-specific information. As an opaque message, the token is received from a security package function by the client, which cannot interpret or change it, and forwarded as a message to the server. The token is also opaque to the server, which can neither interpret nor change the token. The server forwards the opaque token to its security package for interpretation. The package then informs the server of the client authentication or failure to authenticate.

The client receives the server's token in a message, retrieves the token from the received message, and uses that token in a call to its security package. The client then calls the security package again indicating whether a secure connection has been established or whether further exchanges are needed before a secure connection is ready. Theoretically, there is no limit to the number of exchanges of security tokens needed. In practice, only a limited number of exchanges is required. NTLM authentication is based on the challenge/response scheme, and uses three legs to authenticate a client to the server. The [*Kerberos*](/windows/desktop/SecGloss/k-gly) version 5.0 protocol can require additional message exchanges.

## Related topics

<dl> <dt>

[Client Context Initialization](client-context-initialization.md)
</dt> <dt>

[Server Context Initialization](server-context-initialization.md)
</dt> </dl>

 

 
