---
Description: 'To reduce domain controller traffic and improve performance, the client-side of Microsoft Digest caches information received after successful authentication with a server.'
ms.assetid: 'cd928266-889a-494c-a94b-4ea7b1dcc241'
title: Maintaining the Security Context Between Connections
---

# Maintaining the Security Context Between Connections

To reduce domain controller traffic and improve performance, the client-side of Microsoft Digest caches information received after successful authentication with a server. Client applications need only cache the handle to the [*security context*](security.s_gly#-security-security-context-gly) that has been established. The following table describes information cached by the security package.



| Information                                                       | Description                                                                                                                                         |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Server name                                                       | The server that has successfully created a security context for the user.                                                                           |
| Realm/Domain                                                      | The domain name used in the successful authentication.                                                                                              |
| [*Nonce*](security.n_gly#-security-nonce-gly) | A server nonce that is associated with the successful authentication.                                                                               |
| Nonce count                                                       | The number of times the client has included the nonce in requests to the server. This is used for replay-detection.                                 |
| Opaque value                                                      | The value returned for the opaque directive after a successful authentication. This value contains a reference to the security context of the user. |



 

When a client sends a message to a server, the server must determine whether the client has an existing security context. To do this, the server passes each client request to the [**AcceptSecurityContext (General)**](acceptsecuritycontext--general-.md) function. This function extracts the value of the opaque directive from the request, if present, and uses it to look up the client's security context. If the security context is found, the handle of the context is returned to the server. For related information, see [Authenticating Subsequent Requests](authenticating-subsequent-requests-using-microsoft-digest.md).

As a means of detecting spoofing and replay attacks, the client calls the [**MakeSignature**](makesignature.md) function which uses a security context to sign a message. When messages are protected using the **MakeSignature** function, the server uses the [**VerifySignature**](verifysignature.md) function with the cached context to verify the message's origin and [*integrity*](security.i_gly#-security-integrity-gly). For more information, see [Protecting Messages](protecting-messages-using-microsoft-digest.md).

 

 



