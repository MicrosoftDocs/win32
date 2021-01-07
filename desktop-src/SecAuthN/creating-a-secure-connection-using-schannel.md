---
description: How to create a secure connection using Schannel.
ms.assetid: 94eb15c3-225b-4b6f-b29c-41e5d356a847
title: Creating a Secure Connection Using Schannel
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Secure Connection Using Schannel

The Schannel [*security package*](/windows/desktop/SecGloss/s-gly) provides access to four [*security protocols*](/windows/desktop/SecGloss/s-gly):

-   [Transport Layer Security (TLS 1.2)](transport-layer-security-protocol.md)
-   [Transport Layer Security (TLS 1.1)](transport-layer-security-protocol.md)
-   [Transport Layer Security (TLS 1.0)](transport-layer-security-protocol.md)
-   [Secure Sockets Layer (SSL 3.0)](secure-sockets-layer-protocol.md)
-   [Secure Sockets Layer (SSL 2.0)](secure-sockets-layer-protocol.md)

> [!Note]  
> The PCT and SSL 2.0 protocols have been superseded by the TLS protocol and should not be used for new development.

 

**To set up a secure connection between a client and server**

1.  Obtain Schannel credentials ([Obtaining Schannel Credentials](obtaining-schannel-credentials.md)).
2.  Create an Schannel security context ([Creating an Schannel Security Context](creating-an-schannel-security-context.md)).

After a connection is established, you can retrieve information about its attributes. For details, see [Getting Information About Schannel Connections](getting-information-about-schannel-connections.md).

If, after you have established a connection, the security requirements of your application change or the connection is lost, you can renegotiate the connection. For details, see [Renegotiating an Schannel Connection](renegotiating-an-schannel-connection.md).

When you have finished using an Schannel connection, you must perform the necessary cleanup. For details, see [Shutting Down an Schannel Connection](shutting-down-an-schannel-connection.md).

For information about samples shipped with the Platform Software Development Kit (SDK) that demonstrate the Schannel [*security package*](/windows/desktop/SecGloss/s-gly), see the PSDK samples using Schannel.

## Related topics

<dl> <dt>

[Specifying Schannel Ciphers and Cipher Strengths](specifying-schannel-ciphers-and-cipher-strengths.md)
</dt> </dl>

 

 
