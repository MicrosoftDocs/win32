---
Description: This document is intended for developers that are implementing secure devices that interoperate with Windows-based WSD clients and device hosts.
ms.assetid: 96564726-ef48-4b21-9fc3-9c1d4df5074e
title: Secure WSD Device Development
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Secure WSD Device Development

This document is intended for developers that are implementing secure devices that interoperate with Windows-based WSD clients and device hosts. A *secure device* is a hardware component that communicates with other clients, device hosts, and devices on the network using a secure channel. A secure channel provides client and server authentication capabilities. Data transmitted over a secure channel is encrypted.

The key words "must", "must not", and "should" are to be interpreted as described in [RFC 2119](Http://go.microsoft.com/fwlink/p/?linkid=84410).

## Protocols

A secure WSD device must implement or support the following protocols.

-   A secure device must implement the [Devices Profile for Web Services](http://go.microsoft.com/fwlink/p/?linkid=59069) (DPWS).
-   A secure device must support the Transport Layer Security (TLS) 1.0 protocol. For more information, see [RFC 2246](Http://go.microsoft.com/fwlink/p/?linkid=84035).

Windows Vista supports the Secure Sockets Layer (SSL) 3.0 and Transport Layer Security (TLS) 1.0 protocols.

## Device Addressing and Name Resolution

A secure WSD device must meet the following addressing requirements.

-   A secure device must use an https URL as the \[address\] property of its endpoint reference.
-   A secure device must not use a urn:uuid scheme URI as the \[address\] property of its endpoint reference. This supersedes statement R0004 of the DPWS, which states that "A device should use a urn:uuid scheme URI as the \[address\] property of its endpoint reference".

A secure WSD device must meet the following name resolution requirements.

-   A secure device must have a stable https device address.
-   If the address of a secure device contains a device name, then the name must resolve to an IP address using a name resolution protocol supported by Windows Vista.

A secure WSD device should meet the following addressing recommendations.

-   A secure device should use a stable, globally unique identifier that is constant across network interfaces and IPv4/IPv6 addresses as the \[address\] property of its endpoint reference.
-   A secure device should not use a dynamic IP address in the \[address\] property of its endpoint reference. If the address of the secure device changes, it would appear to be a new device. This would make it difficult to manage trust relationships and certificates.
-   A single-homed secure device should use a static IP address, a host name, or a DNS name in the \[address\] property of its endpoint reference.
-   A multi-homed secure device should use a host name or a DNS name in the \[address\] property of its endpoint reference. A multi-homed secure device should not use an IP address in the \[address\] property of its endpoint reference because it is not constant across multiple network interfaces.

Windows Vista does not support security policy assertions, as defined in the WS-Policy specification. Instead, Windows Vista determines if a device supports TLS by checking the URL of the \[address\] property of its endpoint reference. If the URL uses the HTTPS scheme, then it is assumed that the device supports TLS.

## Multicast Discovery and Directed Discovery

WSD devices use two different discovery methods: multicast discovery and directed discovery. Multicast discovery is used to discover devices on the local subnet, and directed discovery is used to discover devices on another subnet.

If the device is installed using PnP-X, then the method used to discover the device must not change after the device is installed. If the device was discovered using multicast discovery, then the device will only be detected by PnP if the device remains on the local subnet. If the device was discovered by directed discovery when it was installed, then it must remain discoverable by directed discovery using the same name provided at the time of installation.

A secure WSD device must meet the following multicast discovery messaging requirements.

-   A device must respond to a received multicast [Probe](probe-message.md) message with a unicast [ProbeMatch](probematches-message.md) message.
-   A device must respond to a received multicast [Resolve](resolve-message.md) message with a unicast [ResolveMatch](resolvematches-message.md) message.
-   The XAddr of the [ResolveMatch](resolvematches-message.md) message must match the https device address. For more information, see [XAddr Validation Rules](xaddr-validation-rules.md).

A secure WSD device should meet the following directed discovery requirement.

-   A secure device should support directed discovery using the secure channel.

If directed discovery over a secure channel is supported, then a device must meet the following directed discovery requirements.

-   A secure device must listen on an https URL for a directed discovery [Probe](probe-message.md) message.
-   The secure device must respond to the [Probe](probe-message.md) message with a [ProbeMatch](probematches-message.md) message.
-   The [ProbeMatch](probematches-message.md) message must use an https URL for the \[address\] property of the endpoint reference.
-   The XAddr of the [ProbeMatch](probematches-message.md) message must match the \[address\] property of the endpoint reference. For more information, see [XAddr Validation Rules](xaddr-validation-rules.md).

## Discovery Messages

A secure WSD device must meet the following discovery messaging requirements.

-   The [Hello](hello-message.md) message sent by a secure device must use an https scheme URL as the \[address\] property of its endpoint reference.
-   The [ProbeMatch](probematches-message.md) message sent by a secure device must use an https scheme URL as the \[address\] property of its endpoint reference.
-   The [ResolveMatch](resolvematches-message.md) message sent by a secure device must use an https scheme URL as the \[address\] property of its endpoint reference.
-   If an XAddr is used a [Hello](hello-message.md), [ProbeMatch](probematches-message.md), or [ResolveMatch](resolvematches-message.md) message, the XAddr entry must match the \[address\] property of endpoint reference. For more information, see [XAddr Validation Rules](xaddr-validation-rules.md).

Windows Vista does not implement signatures on [WS-Discovery](Http://go.microsoft.com/fwlink/p/?linkid=84391) messages.

## Certificates

A secure WSD device must meet the following certificate requirement.

-   A secure device must have an X.509 public key certificate.
-   The Enhanced Key Usage section of the certificate must contain the Server Authentication (1.3.6.1.5.5.7.3.1) object identifier (OID).

A Windows-based WSD client must be correctly configured to use certificates before interacting with a secure WSD device. For more information about Windows-based client configuration, see [Configuring WSDAPI Applications to Use a Secure Channel](configuring-wsdapi-applications-to-use-a-secure-channel.md).

A Windows-based WSD client also performs the following checks before interacting with a secure WSD device.

-   The Windows-based WSD client checks if the server certificate chains up to a trusted root Certificate Authority.
-   The Windows-based WSD client checks if the host name of the device matches the common name in the server certificate.
-   The Windows-based WSD client checks if the server certificate has expired.
-   The Windows-based WSD client checks if the server certificate has been revoked. The client may use the Online Certificate Status Protocol (OCSP) to check for revocation. The client may use a Certificate Revocation List (CRL) to check for revocation. If the server certificate specifies a CRL distribution point, then the CRL should be online.

Should any of these checks fail, the secure device will not be able to communicate with the Windows-based WSD client over a secure channel.

## Metadata Exchange

A secure WSD device must meet the following metadata exchange requirements.

-   A secure device must support secure metadata exchange using a WS-Transfer [Get](get--metadata-exchange--http-request-and-message.md) operation over a secure channel using the TLS protocol.
-   The metadata must contain the endpoint references for the hosted services on the secure device.
-   A secure hosted service must use an https URL as the \[address\] property of its endpoint reference.

The secure client uses the endpoint references to communicate with the hosted services. To prevent spoofing, the endpoint reference for a secure hosted service must be sent via secure metadata exchange.

## Eventing

A secure WSD device must meet the following eventing requirements.

-   A secure device must provide a https URL for the address in a Subscribe response.
-   When sending an event notification to the event sink, a secure device must use the https protocol and pass the appropriate Identifier value in a SOAP header.

The event sink uses the Identifier value to authenticate the event source. The Identifier value is a randomly generated secret that is only known to the event sink and the event source. The Subscribe message is sent over an encrypted channel, so an attacker can't get the Identifier value from sniffing the Subscribe message. The event notification is also sent over an encrypted channel, so an attacker can't get the Identifier value from sniffing an event notification message. The Identifier value is randomly generated and should be 128 bits long.

## Authenticating clients using HTTP authentication

A secure WSD device that requires Windows-based WSD clients (Windows 8 or later) to authenticate using HTTP authentication, must meet the following requirements:

-   The device must support TLS 1.0 and request http authentication inside the TLS session.

-   The device must not require client authentication for directed discovery messages and WS-Transfer Get (metadata exchange) operations. It may require client authentication for all or a subset of the other WS operations that it supports.

-   If the HTTP POST request from the client does not contain authentication, the device must respond with a '401 Unauthorized' response. The 401 response must include a WWW-Authenticate header field containing a list of supported authentication schemes, listed in the order of preference.

-   Clients may send a HTTP HEAD request without authorization to check whether the device needs authentication or not. The device must respond with a '401 Unauthorized' response to the HEAD request and must include a WWW-Authenticate header field containing a list of supported authentication schemes, listed in the order of preference.

-   The device must support the NTLM or Negotiate (which can resolve into either NTLM or Kerberos) authentication schemes.

-   To prevent Man-In-The-Middle (MITM) attacks, the device should request the client to send the Channel-binding-token (CBT) in HTTP requests. The CBT binds the outer TLS secure channel with the inner http authentication protocol.

-   When sending WS operations that contain large Message Transmission Optimization Mechanism (MTOM) attachments, it may not be possible to transmit the authorization headers as part of the HTTP POST requests, if the authentication protocol involves multiple challenge-response legs (e.g., NTLM). In such cases, the device must allow the client to authenticate the TCP connection first using an authenticated HEAD request and then send the WS operation with MTOM attachments.

## Related topics

<dl> <dt>

[Secure WSD Client Development](secure-wsd-client-development.md)
</dt> <dt>

[WSD Device Development](wsd-device-development.md)
</dt> </dl>

 

 



