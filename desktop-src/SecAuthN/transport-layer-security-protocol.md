---
description: Schannel supports versions 1.0, 1.1, and 1.2 of the Transport Layer Security (TLS) protocol.
ms.assetid: af541a51-fabc-4abd-ae67-268bd984ab92
title: Transport Layer Security Protocol
ms.topic: article
ms.date: 05/31/2018
---

# Transport Layer Security Protocol

Schannel supports versions 1.0, 1.1, and 1.2 of the [*Transport Layer Security (TLS) protocol*](../secgloss/t-gly.md). This protocol is an industry standard designed to protect the privacy of information communicated over the Internet. TLS assumes that a connection-oriented transport, typically TCP, is in use. The TLS protocol allows client/server applications to detect the following security risks:

-   Message tampering
-   Message interception
-   Message forgery

The full specification of the TLS Protocol is available from the IETF website: [https://www.ietf.org/rfc/rfc2246.txt](https://www.ietf.org/rfc/rfc2246.txt).

## Organization of TLS

The following steps are involved in using TLS for client/server communication:

 **To use TLS for client/server communication**

1.  Handshake and cipher suite negotiation
2.  Authentication of parties
3.  Key-related information exchange
4.  Application data exchange

The steps that make up TLS are divided into two protocols that, together, provide connection security:

-   [TLS Handshake Protocol](tls-handshake-protocol.md)— (steps 1 – 3)
-   [TLS Record Protocol](tls-record-protocol.md)— (step 4)

## SSPI with TLS implementations

Because TLS does not have a GSSAPI specification, TLS implementers may not be familiar with the SSPI functions. Applications call the SSPI functions to enumerate available packages, create and work with handles to credentials, create security contexts and ensure message integrity privacy.

To support the SSPI functions used by user mode applications, the functions listed in [Functions Implemented by User-mode SSP/APs](/windows/desktop/SecAuthN/authentication-functions) need to be supported by TLS implementations such as schannel.dll.

For details about the SSPI functions and SSP functions, see [Authentication Functions](authentication-functions.md).

## Related topics

<dl> <dt>

[TLS Cipher Suites](/windows/win32/secauthn/cipher-suites-in-schannel)
</dt> <dt>

[TLS vs. SSL](tls-versus-ssl.md)
</dt> </dl>

 

 