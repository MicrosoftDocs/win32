---
description: Learn about inspecting network traces for HTTP metadata exchange. Use a network packet analyzer that displays raw packets.
ms.assetid: b3b6c4d1-5fa3-41fb-ae1d-067638e385b0
title: Inspecting Network Traces for HTTP Metadata Exchange
ms.topic: article
ms.date: 05/31/2018
---

# Inspecting Network Traces for HTTP Metadata Exchange

Any network packet analyzer that can display raw packets can be used to inspect HTTP metadata exchange requests. Microsoft Network Monitor 3 (Netmon) is recommended. For more information about Netmon, see [Downloading Netmon and Sample DPWS Filters](downloading-netmon-and-sample-dpws-filters.md).

This diagnostic procedure may not be as useful for clients and hosts using a secure channel for communications because the message contents are encrypted.

**To inspect network traces for HTTP metadata exchange**

1.  Configure the host and client to run across the network (that is, make sure that the host and client will operate on different machines).
2.  Install the packet analyzer (Netmon) on either the client or the host.
3.  Configure the packet analyzer to capture traffic on the network adapter connecting the host and the client.
4.  Reproduce the failure by starting the host and client or by pressing F5 in the Network Explorer.
5.  Filter the results to isolate WS-Discovery and metadata exchange traffic. To view sample Netmon filters, see [Downloading Netmon and Sample DPWS Filters](downloading-netmon-and-sample-dpws-filters.md).
    > [!Note]  
    > This step is optional.

     

6.  Verify that messages sent between client and host meet basic traffic requirements.

## Verifying that messages meet traffic requirements

WSDAPI clients and hosts must send messages that conform to the following criteria. For general information about message patterns, see [Discovery and Metadata Exchange Message Patterns](discovery-and-metadata-exchange-message-patterns.md).

-   Messages must meet the traffic requirements provided in the topic [Inspecting Network Traces for UDP WS-Discovery](inspecting-network-traces-for-udp-ws-discovery.md), unless it is absolutely certain that WS-Discovery is not being used for metadata exchange.
-   A TCP connection must be established between the client and the first transport address provided in the **XAddrs** element of a [ProbeMatches](probematches-message.md) or [ResolveMatches](resolvematches-message.md) message. The following list shows a typical packet exchange used to establish a TCP connection.
    -   The client sends a TCP SYN packet to the host at a specified port.
    -   The host sends a TCP SYN/ACK packet to the client.
    -   The client sends a TCP ACK packet to the host at a specified port.

    Once the client has sent a TCP ACK packet, the TCP connection is established. Note that this message exchange will not occur if a TCP connection has previously been established.
-   The client must send a valid [Get](get--metadata-exchange--http-request-and-message.md) HTTP request and message.
-   The host must be listening on the URL path specified in the [Get](get--metadata-exchange--http-request-and-message.md) HTTP request.
-   The **To** element of a [Get](get--metadata-exchange--http-request-and-message.md) metadata message must be present and not empty. The value of the **To** element must match one of the host's endpoint addresses. A host's endpoint address is typically advertised in a [ProbeMatches](probematches-message.md) or [ResolveMatches](resolvematches-message.md) message.
-   The host must send a valid HTTP response header. If the initial request was successful, the response header should contain the HTTP/1.1 200 status code.
-   The host must send a valid [GetResponse](getresponse--metadata-exchange--message.md) message.
-   The **RelatesTo** element of a [GetResponse](getresponse--metadata-exchange--message.md) message must be present and must not be empty. Its value must match the value of the **MessageId** element from the corresponding [Get](get--metadata-exchange--http-request-and-message.md) message.

If the HTTP requests or metadata exchange messages sent by the program do not conform to these traffic requirements, the cause of the problem has been successfully identified and no further troubleshooting steps are necessary. Rewrite the program so that it generates conformant messages and requests and retest the program.

If the source of the problem still cannot be identified, contact Microsoft support for assistance. Before contacting support, collect the appropriate log files to help identify the root cause of the problem. For more information, see [Enabling WSDAPI Tracing](enabling-wsdapi-tracing.md).

## Related topics

<dl> <dt>

[WSDAPI Diagnostic Procedures](wsdapi-diagnostic-procedures.md)
</dt> <dt>

[Getting Started with WSDAPI Troubleshooting](getting-started-with-wsdapi-troubleshooting.md)
</dt> <dt>

[Downloading Netmon and Sample DPWS Filters](downloading-netmon-and-sample-dpws-filters.md)
</dt> </dl>

 

 



