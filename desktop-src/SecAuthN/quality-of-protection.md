---
description: The quality of protection, identified by the qop directive, is first specified by the server in the Digest challenge, and then confirmed by the client in the challenge response.
ms.assetid: bee4236c-69e5-4281-a6b3-be316bac0a11
title: Quality of Protection
ms.topic: article
ms.date: 05/31/2018
---

# Quality of Protection

The quality of protection, identified by the qop directive, is first specified by the server in the Digest challenge, and then confirmed by the client in the challenge response. If the client requires a quality of protection that the server does not support, the client must terminate the authentication.

The possible values for the qop directive are described in the following table.



| Value                   | Description                                                                                                                                  |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| "auth"                  | Authentication only.                                                                                                                         |
| "auth-int"              | Authentication and [*integrity*](../secgloss/i-gly.md) checking using signatures.                  |
| (SASL only) "auth-conf" | Authentication, integrity and confidentiality checking by using signatures and encryption. For more information, see [Ciphers](ciphers.md). |



 

Quality of protection is determined by context requirement flags passed to the Microsoft Digest SSP. The following table lists the flags related to quality of protection, and the resulting value of the qop directive.



| Flag                         | qop value               |
|------------------------------|-------------------------|
| *XXX*\_REQ\_CONFIDENTIALITY  | "auth-conf" (SASL only) |
| *XXX*\_REQ\_REPLAY\_DETECT   | "auth-int"              |
| *XXX*\_REQ\_SEQUENCE\_DETECT | "auth-int"              |
| *XXX*\_REQ\_INTEGRITY        | "auth-int"              |
| (none)                       | "auth"                  |



 

> [!Note]  
> Context requirement flags specified by server applications have a prefix of ASC, and those specified by clients are prefixed with ISC. To determine the flag values used by your application, substitute one of these prefixes for *XXX*.

 

For additional server-related information, see [Generating the Digest Challenge](generating-the-digest-challenge.md).

For additional client-related information, see [Generating the Digest Challenge Response](generating-the-digest-challenge-response.md).

 

 
