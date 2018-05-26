---
Description: Describes development considerations for developers writing applications for clients or devices communicating over a secure channel.
ms.assetid: c2180f42-bce5-420d-8a3e-b6e6f41e8339
title: Using WSDAPI with a Secure Channel
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using WSDAPI with a Secure Channel

The WSDAPI framework supports the use of a secure channel for communication between a device and a client. The secure channel encrypts data transmitted between the client and the device. The channel also authenticates the device to the client, and optionally authenticates the client to the device. A secure channel uses the SSL/TLS protocol, and the URL uses the HTTPS scheme, not the HTTP scheme.

## Device Requirements

A device that communicates over a secure channel must meet the following requirements.

-   The logical or physical address of a device that uses a secure channel is an URL prefixed by https, not the urn:uuid style of identifier used by other WSDAPI devices or clients.
-   The device must advertise an identifier that is an URL prefixed by https.
-   The transport address that the device provides in the Discovery message must be the same URL as the device ID.
-   The device ID must also match the URL used to obtain the device metadata over the secure channel.
-   The device must have server certificates that are trusted by the Windows Vista client. These certificates are used when establishing the secure connection.
-   The device must advertise a HTTPS endpoint and not a HTTP endpoint.

## Implementation Considerations for Client Application Developers

A client application that uses WSDAPI cannot use a device that advertises both a HTTP and a HTTPS endpoint at the same time. In other words, a device that uses a secure channel must only use a secure channel.

For a client to authenticate to the device host, the client must trust the server certificate installed on the device host. That means that the root certificate of the certificate installed on the device host must be stored in the client computer's Trusted Root Certification Authorities store.

When accepting secure connections, it is important that the host name in the URL matches the subject name in the certificate used to accept the connection. For this reason, using a dynamic IP address in the URL is not recommended. Additionally, the use of Link-local IPv6 addresses is also not recommended, as they are not routable. In either scenario, use a host name or a static IP address instead.

If a device requires authentication, the Windows Vista client must have a certificate in the local machine store that will be used as a client certificate when establishing a secure connection to the device. The certificate should be one that the device will trust when authenticating the client to the device.

To receive event messages from the device over a secure channel, the Windows Vista client should also have a server certificate that can be used to accept an SSL/TLS connection from the device on the port used for event notifications. It is possible to have one certificate that is used for both roles.

For more information about addressing and port selection when creating a device proxy for use in your client application, see [**WSDCreateDeviceProxy**](/windows/win32/WsdClient/nf-wsdclient-wsdcreatedeviceproxy?branch=master) and [**WSDCreateDeviceProxyAdvanced**](/windows/win32/WsdClient/nf-wsdclient-wsdcreatedeviceproxyadvanced?branch=master).

## Implementation Considerations for Host Application Developers

You can create a host application using WSDAPI that accepts connections from clients. You can implement a host application that only accepts communication over a secure channel. In this case, the Windows Vista computer on which the host application is installed must have a server certificate that clients will trust. When required by the event sink, the computer must also have a certificate that can be used to establish a secure connection when sending events to the client. It is possible to have one certificate for both roles.

If no port is specified in the device identifier advertised by a host application, then secure communication takes place over port 443 if the device ID is an HTTPS URL. It is recommended that the device identifier explicitly specify port 5358, as this port is reserved for secure connections with WSDAPI.

For more information about addressing and port selection when creating a device host, see [**WSDCreateDeviceHost**](/windows/win32/WsdHost/nf-wsdhost-wsdcreatedevicehost?branch=master) and [**WSDCreateDeviceHostAdvanced**](/windows/win32/WsdHost/nf-wsdhost-wsdcreatedevicehostadvanced?branch=master).

## Related topics

<dl> <dt>

[WSD Application Development on Windows](wsd-application-development-on-windows.md)
</dt> <dt>

[Configuring WSDAPI Applications to Use a Secure Channel](configuring-wsdapi-applications-to-use-a-secure-channel.md)
</dt> <dt>

[Troubleshooting HTTPS Secure Channel Communication](troubleshooting-https-secure-channel-communication.md)
</dt> </dl>

 

 



