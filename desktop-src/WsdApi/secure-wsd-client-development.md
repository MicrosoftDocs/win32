---
Description: This document is intended for developers that are implementing secure clients that interoperate with secure WSD devices and secure Windows-based device hosts.
ms.assetid: baf0cd85-e309-4377-9414-a48de270d0e0
title: Secure WSD Client Development
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Secure WSD Client Development

This document is intended for developers that are implementing secure clients that interoperate with secure WSD devices and secure Windows-based device hosts. A *secure client* is a hardware component that connects other devices, device hosts, and/or hosted services on the network using a secure channel. A secure channel provides client and server authentication capabilities. Data transmitted over a secure channel is encrypted.

The secure client requirements described in this document are not relevant to Windows-based WSD client application developers. Windows-based clients use WSDAPI, which serves as an abstraction layer. For more information about configuring Windows-based secure clients, see [Configuring WSDAPI Applications to Use a Secure Channel](configuring-wsdapi-applications-to-use-a-secure-channel.md)

The key words "must", "must not", and "should" are to be interpreted as described in [RFC 2119](Http://go.microsoft.com/fwlink/p/?linkid=84410).

## General Requirements

A secure WSD client must implement or support the following requirements.

-   A secure client must support SSL v3.0 or TLS with server certificates.
-   A secure client must be configured to trust the issuer of the server certificate for the secure device. A secure client must be able to build a certificate chain from the server certificate to a trusted root certificate.

A secure WSD client should implement or support the following requirements.

-   A secure client should implement the Devices Profile for Web Services (DPWS). Some features of the DPWS are not supported by Windows Vista, and it is not required to implement those features. Windows Vista does not support security policy assertions, as defined in the WS-Policy specification. Also, Windows Vista does not implement signatures on [WS-Discovery](Http://go.microsoft.com/fwlink/p/?linkid=84391) messages.
-   A secure client should have the correct time so that it can check for expiration of server certificates.
-   A secure client should reject a server certificate unless the current time is between the ValidFrom and ValidTo times specified in the server certificate.
-   A secure client should check for revocation of server certificates. If the certificate specifies a CRL distribution point, then the server hosting the CRL must be online so that the secure client can download the certificate revocation list.
-   A secure client should support SSL v3.0 or TLS with client certificates.
-   A secure client should have an X.509 public key certificate. If the certificate is present, the Enhanced Key Usage section of the certificate must contain the Client Authentication (1.3.6.1.5.5.7.3.2) object identifier (OID).
-   If a device requests a client certificate and the client has multiple certificates, a secure client should search the local machine certificate store and the user certificate store for a valid client certificate matching one of the trusted issuers specified by the device.

## Eventing Requirements

A secure WSD client must implement the following eventing requirements.

-   A secure client must use an https URL as the \[address\] property of its NotifyTo endpoint reference when sending a Subscribe request to a secure hosted service.
-   A secure client must send the Subscribe message containing the Identifier value over an encrypted channel to prevent disclosure of the secret value.

A secure WSD client should implement the following eventing requirements.

-   A secure client should use an Identifier reference parameter in the NotifyTo endpoint reference when sending a subscribe request to a secure hosted service.
-   The Identifier reference parameter should contain a randomly generated urn:uuid URI.
-   The client should use a secure random number generator to prevent an attacker from guessing the Identifier value. Using a random Identifier value makes it difficult for an attacker to spoof event notification messages.
-   A secure client should verify that an incoming event notification contains an Identifier SOAP header that matches the Identifier reference parameter passed in the NotifyTo endpoint reference.
-   A secure client should drop event notifications that do not contain the correct Identifier value.

A secure hosted service must implement the following eventing requirements.

-   A secure hosted service must handle a NotifyTo address containing an https URL.
-   A secure hosted service must handle a NotifyTo endpoint reference containing an Identifier reference parameter.
-   A secure hosted service must copy the Identifier reference parameter from the NotifyTo endpoint reference to the SOAP header when sending an event notification to the NotifyTo endpoint.

## Related topics

<dl> <dt>

[Secure WSD Device Development](secure-wsd-device-development.md)
</dt> <dt>

[WSD Device Development](wsd-device-development.md)
</dt> </dl>

 

 



