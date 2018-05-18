---
Description: 'Describes certificate configuration for WSDAPI client and host applications that communicate over a secure channel.'
ms.assetid: 'ae3be598-3230-4e5e-a084-d407d17489e6'
title: Configuring WSDAPI Applications to Use a Secure Channel
---

# Configuring WSDAPI Applications to Use a Secure Channel

WSDAPI client and host applications that communicate over a secure channel use certificates when establishing a connection. WSDAPI does not manage certificates, bind certificates to a port, or validate certificates.

## Certificates for Client Applications

The computer hosting the WSDAPI client application (the client computer) must trust the certificate installed on the device host. That means that the root certificate of the certificate installed on the device host must be stored in the client computer's Trusted Root Certification Authorities store.

If the device host requires client authentication, then a certificate on the client computer must be configured as follows.

-   An appropriate and valid X.509 certificate must be installed in the local machine store on the client computer. This certificate is used for authentication.
-   The client application must be granted access to the private key of the certificate.
-   The LocalService account must be granted access to the private key of the certificate. This enables secure device discovery (either by the **Network Explorer** or by other applications that use [Function Discovery](https://msdn.microsoft.com/library/windows/desktop/aa814070) for device discovery) and [PnP-X](https://msdn.microsoft.com/library/windows/desktop/aa814083) secure device support. WSDAPI does not support secure discovery.

Certificates are also required for eventing. The client computer must have a server certificate installed. The server certificate is used by the event sink. The event source on the device host must trust the server certificate used by the event sink. By default, the event sink on the client computer receives event notifications on port 5358. The HTTP Server API must be used to configure port 5358 with the server certificate for the event sink.

It is possible to specify a port other than 5358 for secure communications. You can specify this port when calling [**WSDCreateDeviceProxy**](wsdcreatedeviceproxy.md) or [**WSDCreateDeviceProxyAdvanced**](wsdcreatedeviceproxyadvanced.md). If a port other than 5358 is used, the HTTP Server API must be configured to reserve the URL for this port, unless the application has full administrative rights. For more information, see [Configuring the HTTP Server API](#binding-certificates-using-the-http-server-api).

Authentication of the device sending the event is done after the secure channel is established. Therefore, it is not necessary to configure the certificate to request a client certificate for accepting events or for the certificate to be trusted.

## Certificates for Device Host Applications

If an application uses the WSDAPI hosting feature to implement a device that has a secure channel, then the appropriate and valid X.509 certificate must be installed on the computer. The certificate chain must extend to a root authority that is trusted by the client.

It is possible to specify a port other than 5358 for secure communications. You can specify this port when calling [**WSDCreateDeviceHost**](wsdcreatedevicehost.md) or [**WSDCreateDeviceHostAdvanced**](wsdcreatedevicehostadvanced.md). If a port other than 5358 is used, the HTTP Server API must be configured to reserve the URL for this port, unless the application has full administrative rights. If no port is specified, then port 443 is used for secure communications, and that port must be configured using the HTTP Server API. For more information, see [Configuring the HTTP Server API](#binding-certificates-using-the-http-server-api).

If the device host is used for eventing and the event sinks require authentication of the event source, then the event sink must trust the event source certificate installed on the device host.

## Binding Certificates Using the HTTP Server API

WSDAPI device hosts can use the [HTTP Server API](https://msdn.microsoft.com/library/windows/desktop/aa364510) to receive messages. WSDAPI clients may use the HTTP Server API to receive event notifications. TCP port 5358 has been reserved to receive secure messages and secure event notifications. An URL reservation on the HTTP server enables all accounts to listen on port 5358.

If an application running without administrator privileges uses a port other than 5358 for receiving secure data, then an administrator must configure the selected port with a server certificate in order to receive event notifications via the SSL/TLS protocol. The configuration can be performed by calling [**HttpSetServiceConfiguration**](https://msdn.microsoft.com/library/windows/desktop/aa364503). The [**HTTP\_SERVICE\_CONFIG\_SSL\_SET**](https://msdn.microsoft.com/library/windows/desktop/aa364649) structure passed to the *pConfigInformation* parameter contains the SSL configuration information.

The SSL configuration specifies the identifier of the server certificate to be used on the port. It also specifies whether a client certificate is required, and whether client certificates should be checked for revocation. The SSL configuration can optionally specify a certificate trust list, which can be used to restrict the group of certificate issuers to be trusted.

## Binding Certificates Using Netsh

Certificates can be bound to the eventing or hosting port using the **netsh** command-line utility.

The following example shows a **netsh** call used to bind a certificate to port 5358 on a specified machine using IPv4 addresses.

``` syntax
netsh http add sslcert ipport=0.0.0.0:5358 certhash=0102030405060708090A0B0C0D0E0F1011121314 appid={00112233-4455-6677-8899-AABBCCDDEEFF} 
```

The following example shows a similar **netsh** call that also explicitly allows client certificate negotiation.

``` syntax
netsh http add sslcert ipport=0.0.0.0:5358 certhash=0102030405060708090A0B0C0D0E0F1011121314 appid={00112233-4455-6677-8899-AABBCCDDEEFF} clientcertnegotiation=enable
```

The following example shows a **netsh** call used to bind a certificate to port 5358.

``` syntax
netsh http add sslcert ipport=[::]:5358 certhash=0102030405060708090A0B0C0D0E0F1011121314 appid={00112233-4455-6677-8899-AABBCCDDEEFF} 
```

For these examples, **certhash** represents the thumbprint of the server certificate.

## Related topics

<dl> <dt>

[WSD Application Development on Windows](wsd-application-development-on-windows.md)
</dt> <dt>

[Using WSDAPI with a Secure Channel](using-wsdapi-with-a-secure-channel.md)
</dt> <dt>

[Troubleshooting HTTPS Secure Channel Communication](troubleshooting-https-secure-channel-communication.md)
</dt> </dl>

 

 



