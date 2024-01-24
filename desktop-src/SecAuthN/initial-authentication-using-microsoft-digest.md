---
description: The initial authentication takes place when the server receives a challenge response from a client.
ms.assetid: 8a5cf26b-0b2a-4f19-807b-9ec4d533cdd4
title: Initial Authentication Using Microsoft Digest
ms.topic: article
ms.date: 09/14/2022
---

# Initial Authentication Using Microsoft Digest

> [!NOTE]
> Starting in Windows 11 22H2, Microsoft is deprecating Microsoft Digest, also known as wDigest. We will continue to support Microsoft Digest on supported versions of Windows. Future versions of Windows will include limited capabilities for Microsoft Digest, and eventually Microsoft Digest will no longer be supported on Windows.

The initial authentication takes place when the server receives a challenge response from a client. Authenticating a challenge response typically involves a minimum of two servers:

- The originating server—receives the request from the client and issues a challenge, and then receives the challenge response from the client which must be authenticated.
- The authenticating server—receives authorization information from the originating server, and performs the authentication. This server is typically a domain controller that supports multiple originating servers.

When the originating server receives a request with an Authorization header containing a Digest challenge response, the authentication proceeds as follows:

- The identity of the originating server is checked against the server encoded in the challenge's nonce.
- The time stamp encoded in the nonce is checked. If the nonce has expired and the user name/password information is valid, the originating server ends the authentication by issuing a new Digest challenge with the stale directive set to "true". This indicates that only the nonce was "stale" and the client can respond to the new challenge using the password it used in the previous response. If the client receives a new challenge after sending the challenge response for the stale challenge, the client must generate a new challenge response.
- If replay detection is enforced, the nc directive (nonce count) is checked against the nonce session database maintained by the server.
- The authenticating server is identified and sent the client's authorization information.
- The authenticating server checks the identity of the server encoded in the nonce against the identity of the originating server.
- The authenticating server, which is a domain controller, retrieves the user's password.
- Using the authorization information, password, and originating server identification, the authenticating server computes the value that the client should have supplied in the challenge response's response directive. The authenticating server compares the computed value to the client's response to determine the success or failure of the authentication.

If authentication is successful, the user's [*security context*](../secgloss/s-gly.md) and a Digest [*session key*](../secgloss/s-gly.md) are returned to the originating server. If authentication fails, the originating server must generate an error response. After a successful authentication the originating server returns the requested resource to the client.

The Digest session key returned by the authenticating server is cached by the originating server for use in authenticating future requests. For more information, see [Authenticating Subsequent Requests using Microsoft Digest](authenticating-subsequent-requests-using-microsoft-digest.md).
