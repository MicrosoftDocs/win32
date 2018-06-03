---
Description: Troubleshooting metadata exchange or directed discovery over HTTPS is different than troubleshooting WSDAPI traffic on HTTP. There are special considerations when troubleshooting secure channel communications.
ms.assetid: 1c39556c-c04a-4c3b-8a29-60cea75c1e50
title: Troubleshooting HTTPS Secure Channel Communication
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Troubleshooting HTTPS Secure Channel Communication

Troubleshooting metadata exchange or directed discovery over HTTPS is different than troubleshooting WSDAPI traffic on HTTP. There are special considerations when troubleshooting secure channel communications.

Before troubleshooting HTTPS communication carefully review the HTTPS validation rules described in [Using WSDAPI with a Secure Channel](using-wsdapi-with-a-secure-channel.md). Verify that the client and host conform to the implementation requirements described in that topic.

Also, the XAddrs published for a host must conform to the [XAddr validation rules](xaddr-validation-rules.md). Verify that the host meets the following requirements.

-   The host only advertises an HTTPS address. WSDAPI rejects hosts that advertise both HTTP and HTTPS addresses at the same time.
-   The XAddrs for the host match the device's endpoint address.
-   The host does not advertise a logical address (that is, an address beginning with the `urn:uuid:` prefix).

It is very important to examine the WinHTTP logs when troubleshooting secure communications. These logs contain information about SSL/TLS negotiation, and they also show the conversation contents after the conversation has been decrypted. For more information, see [Capturing WinHTTP Logs](capturing-winhttp-logs.md) and [Using WinHTTP Logging to Verify SSL/TLS Negotiation](using-winhttp-logging-to-verify-ssl-tls-negotiation.md).

It is less important to use a packet analyzer to examine network traffic. This is because the message contents are encrypted. However, network traces can be used to identify when and where HTTPS connections from a client to a host were established. For more information about using a packet analyzer, see [Inspecting Network Traces for HTTP Metadata Exchange](inspecting-network-traces-for-http-metadata-exchange.md).

There are additional requirements that a host must meet to enable secure eventing. For a Windows Vista machine to receive events, a valid server certificate must be installed on the local computer certificate store of the machine and must be bound the port on which it listens for events. The certificate can be bound to the port using **netsh**. For more information, see [Configuring WSDAPI Applications to Use a Secure Channel](configuring-wsdapi-applications-to-use-a-secure-channel.md).

## Related topics

<dl> <dt>

[Getting Started with WSDAPI Troubleshooting](getting-started-with-wsdapi-troubleshooting.md)
</dt> <dt>

[Capturing WinHTTP Logs](capturing-winhttp-logs.md)
</dt> <dt>

[Using WinHTTP Logging to Verify SSL/TLS Negotiation](using-winhttp-logging-to-verify-ssl-tls-negotiation.md)
</dt> <dt>

[Using WSDAPI with a Secure Channel](using-wsdapi-with-a-secure-channel.md)
</dt> <dt>

[Configuring WSDAPI Applications to Use a Secure Channel](configuring-wsdapi-applications-to-use-a-secure-channel.md)
</dt> </dl>

 

 



