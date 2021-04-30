---
description: To reduce domain controller traffic and improve performance, the client-side of Microsoft Digest caches information received after successful authentication with a server.
ms.assetid: cd928266-889a-494c-a94b-4ea7b1dcc241
title: Maintaining the Security Context Between Connections
ms.topic: article
ms.date: 05/31/2018
---

# Maintaining the Security Context Between Connections

To reduce domain controller traffic and improve performance, the client-side of Microsoft Digest caches information received after successful authentication with a server. Client applications need only cache the handle to the [*security context*](../secgloss/s-gly.md) that has been established. The following table describes information cached by the security package.



| Information                                                       | Description                                                                                                                                         |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Server name                                                       | The server that has successfully created a security context for the user.                                                                           |
| Realm/Domain                                                      | The domain name used in the successful authentication.                                                                                              |
| [*Nonce*](../secgloss/n-gly.md) | A server nonce that is associated with the successful authentication.                                                                               |
| Nonce count                                                       | The number of times the client has included the nonce in requests to the server. This is used for replay-detection.                                 |
| Opaque value                                                      | The value returned for the opaque directive after a successful authentication. This value contains a reference to the security context of the user. |



 

When a client sends a message to a server, the server must determine whether the client has an existing security context. To do this, the server passes each client request to the [**AcceptSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-acceptsecuritycontext) function. This function extracts the value of the opaque directive from the request, if present, and uses it to look up the client's security context. If the security context is found, the handle of the context is returned to the server. For related information, see [Authenticating Subsequent Requests](authenticating-subsequent-requests-using-microsoft-digest.md).

As a means of detecting spoofing and replay attacks, the client calls the [**MakeSignature**](/windows/desktop/api/Sspi/nf-sspi-makesignature) function which uses a security context to sign a message. When messages are protected using the **MakeSignature** function, the server uses the [**VerifySignature**](/windows/desktop/api/Sspi/nf-sspi-verifysignature) function with the cached context to verify the message's origin and [*integrity*](../secgloss/i-gly.md). For more information, see [Protecting Messages](protecting-messages-using-microsoft-digest.md).

 

 
