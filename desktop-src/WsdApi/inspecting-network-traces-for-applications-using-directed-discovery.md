---
description: Any network packet analyzer that can display raw packets can be used to inspect HTTP metadata exchange requests. Microsoft Network Monitor 3 (Netmon) is recommended. For more information about Netmon, see Downloading Netmon and Sample DPWS Filters.
ms.assetid: 9b124117-06e7-4637-9863-0f9650861526
title: Inspecting Network Traces for Applications Using Directed Discovery
ms.topic: article
ms.date: 05/31/2018
---

# Inspecting Network Traces for Applications Using Directed Discovery

Any network packet analyzer that can display raw packets can be used to inspect HTTP metadata exchange requests. Microsoft Network Monitor 3 (Netmon) is recommended. For more information about Netmon, see [Downloading Netmon and Sample DPWS Filters](downloading-netmon-and-sample-dpws-filters.md).

**To inspect network traces for directed discovery**

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

-   [Probe](probe-message.md) messages must be sent by HTTP or HTTPS, usually to port 5357 or 5358.
-   The **Types** element of a [Probe](probe-message.md) message must be present and must not be empty. It must contain the types to which a host will respond.
-   A [ProbeMatches](probematches-message.md) message must be sent to the HTTP or HTTPS port from which the [Probe](probe-message.md) was sent.
-   The **RelatesTo** element of a [ProbeMatches](probematches-message.md) message must be present and must not be empty. Its value must match the value of the **MessageId** element from the corresponding [Probe](probe-message.md) message.
-   If an **XAddrs** element was included in the [ProbeMatches](probematches-message.md) message, the supplied transport addresses must be validated. For more information, see [XAddr Validation Rules](xaddr-validation-rules.md).
-   A [ProbeMatches](probematches-message.md) message must be sent within 4 seconds of the corresponding [Probe](probe-message.md) message. The Windows Firewall may drop a ProbeMatches message sent more than 4 seconds after a Probe message.
-   If no **XAddrs** element was included in the [ProbeMatches](probematches-message.md) message, and the client or host will send an HTTP message (such as a [Get](get--metadata-exchange--http-request-and-message.md) metadata exchange request or a service message), then the client or host must send a [Resolve](resolve-message.md) message by HTTP or HTTPS. This message is usually sent to port 5357 or 5358.
-   If a [Resolve](resolve-message.md) message is sent, then a [ResolveMatches](resolvematches-message.md) message must be sent to the HTTP or HTTPS port from which the Resolve message was sent.
-   A [ResolveMatches](resolvematches-message.md) message must be sent within 4 seconds of the corresponding [Resolve](resolve-message.md) message. The Windows Firewall may drop a ResolveMatchesmessage sent more than 4 seconds after a Resolve message.

If the messages sent by the program do not conform to these message requirements, the cause of the problem has been successfully identified and no further troubleshooting steps are necessary. Rewrite the program so that it generates conformant messages and retest the program.

If the source of the problem still cannot be identified, contact Microsoft support for assistance. Before contacting support, collect the appropriate log files to help identify the root cause of the problem. For more information, see [Enabling WSDAPI Tracing](enabling-wsdapi-tracing.md).

## Related topics

<dl> <dt>

[Troubleshooting Applications Using Directed Discovery](troubleshooting-applications-using-directed-discovery.md)
</dt> <dt>

[WSDAPI Diagnostic Procedures](wsdapi-diagnostic-procedures.md)
</dt> <dt>

[Getting Started with WSDAPI Troubleshooting](getting-started-with-wsdapi-troubleshooting.md)
</dt> <dt>

[Downloading Netmon and Sample DPWS Filters](downloading-netmon-and-sample-dpws-filters.md)
</dt> </dl>

 

 



