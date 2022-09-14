---
description: Like the client, the server also acquires a credentials handle to be ready to respond to an incoming authentication request from the client.
ms.assetid: 2a0aeadf-e099-4264-8522-e498f437bf75
title: Server Context Initialization
ms.topic: article
ms.date: 05/31/2018
---

# Server Context Initialization

Like the client, the server also acquires a [*credentials*](../secgloss/c-gly.md) handle to be ready to respond to an incoming authentication request from the client. Server credentials are used to authenticate the server to the client in [*security protocols*](../secgloss/s-gly.md) that support server authentication or mutual authentication. The server obtains a handle to its credentials defined by the service account used to start the server. It does so by calling [**AcquireCredentialsHandle**](/windows/win32/api/sspi/nf-sspi-acquirecredentialshandlea).

The server can acquire its credentials handle and then go into a listen state, or it can wait in a listen state until a connection request arrives and then acquire an inbound credentials handle. For more information on credentials functions, see [Credential Management](authentication-functions.md).

When the server receives a connection request message from a client, it creates a local [*security context*](../secgloss/s-gly.md) for the client using [**AcceptSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-acceptsecuritycontext). The server uses this local security context to carry out future requests by the same client. For more information on context functions, see [Context Management](authentication-functions.md).

The server checks the return status and output buffer descriptor to ensure there are no errors so far, and can reject the connection request if there are errors. If there is information in the output buffer returned by [**AcceptSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-acceptsecuritycontext), it bundles that buffer into a response message to the client.

Any output buffer from [**AcceptSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-acceptsecuritycontext) must be sent back to the client. In addition, if the return status requires the protocol to continue (SEC\_I\_CONTINUE\_NEEDED or SEC\_I\_COMPLETE\_AND\_CONTINUE), another message exchange with the client is required.

For additional legs, the server waits for the client to respond with another message. This wait can be timed out so as to avoid a denial of service attack where a client purposely never responds, causing a server thread and soon, all server threads, to stop responding.

 

 
