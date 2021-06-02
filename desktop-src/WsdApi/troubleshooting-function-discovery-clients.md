---
description: Lists the diagnostic procedures to use when troubleshooting Function Discovery clients.
ms.assetid: e488882a-fadd-4150-89ef-b958c3df34c6
title: Troubleshooting Function Discovery Clients
ms.topic: article
ms.date: 05/31/2018
---

# Troubleshooting Function Discovery Clients

Function Discovery clients:

-   Always use UDP WS-Discovery for device discovery
-   Always initiate HTTP or HTTPS connections for metadata exchange
-   Sometimes use directed discovery
-   Sometimes use a secure channel (HTTPS) for metadata exchange

The following list shows the typical sequence of messages sent and received by Function Discovery clients. Not all messages are mandatory.

1.  The client sends a [Probe](probe-message.md) message to discover devices and services. If the client is using directed discovery then this message is sent over HTTP or HTTPS; otherwise, the message is sent by UDP multicast to port 3702.
2.  The client receives [ProbeMatches](probematches-message.md) messages from matching devices or services. Directed discovery messages are sent over HTTP or HTTPS; otherwise, these messages are sent by UDP unicast and originate from port 3702.
3.  If no XAddrs were included in the ProbeMatches message, then the client will send a [Resolve](resolve-message.md) message by UDP multicast to port 3702.
4.  If a [Resolve](resolve-message.md) message was sent, then the client receives a [ResolveMatches](resolvematches-message.md) message from matching services. This message is sent by UDP unicast from port 3702 to the port where the Resolve message originated.
5.  The client sends a [Get](get--metadata-exchange--http-request-and-message.md) message to request metadata from the device or service. This message is sent by HTTP or HTTPS.
6.  The client receives a [GetResponse](getresponse--metadata-exchange--message.md) message with the device or service metadata. This message is sent by HTTP or HTTPS.

The following diagnostic procedures should be used (in order) to help identify problems with a Function Discovery client.

**To troubleshoot a Function Discovery client**

1.  If directed discovery is used, [troubleshoot directed discovery](troubleshooting-applications-using-directed-discovery.md).
2.  [Inspect adapter and firewall settings](inspecting-adapter-and-firewall-settings.md).
3.  [Use a generic host and client for UDP WS-Discovery](using-a-generic-host-and-client-for-udp-ws-discovery.md).
4.  [Use WSD Debug Client to verify multicast traffic](using-wsddebug-client-to-verify-multicast-traffic.md).
5.  [Inspect network traces for UDP WS-Discovery](inspecting-network-traces-for-udp-ws-discovery.md).
6.  [Use a generic host and client for HTTP metadata exchange](using-a-generic-host-and-client-for-http-metadata-exchange.md).
7.  [Use WinHTTP logging to verify Get traffic](using-winhttp-logging-to-verify-get-traffic.md).
8.  [Inspect network traces for HTTP metadata exchange](inspecting-network-traces-for-http-metadata-exchange.md).

If the source of the problem cannot be identified using the above diagnostic procedures, follow the directions in [Enabling WSDAPI Tracing](enabling-wsdapi-tracing.md) and contact Microsoft support.

## Related topics

<dl> <dt>

[Getting Started with WSDAPI Troubleshooting](getting-started-with-wsdapi-troubleshooting.md)
</dt> </dl>

 

 



