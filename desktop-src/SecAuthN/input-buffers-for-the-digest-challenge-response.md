---
description: HTTP authentication using Microsoft Digest requires three input buffers to generate a challenge response. The following table summarizes these buffers.
ms.assetid: 0df02be2-f42e-46d0-a206-765adf3d7a72
title: Input Buffers for the Digest Challenge Response
ms.topic: article
ms.date: 05/31/2018
---

# Input Buffers for the Digest Challenge Response

HTTP authentication using Microsoft Digest requires three input buffers to generate a challenge response. The following table summarizes these buffers.



| Buffer number | Contains                                                                                                                                             | Buffer type                                                 |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| 0             | Challenge received from the Server                                                                                                                   | SECBUFFER\_TOKEN                                            |
| 1             | HTTP Method                                                                                                                                          | SECBUFFER\_PARAMS                                           |
| 2             | H(Entity)                                                                                                                                            | SECBUFFER\_PARAMS                                           |
| 3             | The [*service principal name*](../secgloss/s-gly.md) (SPN) of the target server. | **SECBUFFER\_TARGET\_HOST** \| **SECBUFFER\_READONLY**      |
| 4             | Channel bindings token values                                                                                                                        | **SECBUFFER\_CHANNEL\_BINDINGS** \| **SECBUFFER\_READONLY** |



 

Buffer zero contains the Digest challenge received from the server in response to the initial request for an access-protected resource.

Buffer 1 contains the string representation of the method, such as "GET" or "POST". The method is used in the calculation of A2, as described in [RFC 2617](https://www.ietf.org/rfc/rfc2617.txt).

Buffer 2 is the [*MD5*](../secgloss/m-gly.md) hash of the message's entity-body as described in RFC 2617.

Buffer 3 contains the SPN of the target server in UTF-8 formatting when Digest is used with channel bindings.

Buffer 4 contains the channel binding token value when Digest is used with channel bindings.

## Input Buffers for SASL

Supply buffer zero only. For compatibility with other SSPs, you may call [**InitializeSecurityContext (Digest)**](/windows/win32/api/sspi/nf-sspi-initializesecuritycontexta) without a valid server challenge. In this case the *pInput* parameter should be set to **NULL**.

 

 
