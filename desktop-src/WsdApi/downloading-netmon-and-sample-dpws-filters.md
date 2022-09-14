---
description: Microsoft Network Monitor 3 (Netmon) is a packet analyzer used to inspect network traffic.
ms.assetid: 015a6a6d-9e07-4f22-b931-dcce77051bef
title: Downloading Netmon and Sample DPWS Filters
ms.topic: article
ms.date: 05/31/2018
---

# Downloading Netmon and Sample DPWS Filters

Microsoft Network Monitor 3 (Netmon) is a packet analyzer used to inspect network traffic. Netmon must be downloaded before the troubleshooting steps given in [Inspecting Network Traces for UDP WS-Discovery](inspecting-network-traces-for-udp-ws-discovery.md) and [Inspecting Network Traces for HTTP Metadata Exchange](inspecting-network-traces-for-http-metadata-exchange.md) can be followed. After Netmon has been downloaded, DPWS filters can be used to help isolate traffic of interest.

## Downloading Netmon

To download Netmon, go to [Microsoft Network Monitor](https://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=983b941d-06cb-4658-b7f6-3088333d062f) and follow the instructions. For more information about Netmon, see "Information about Network Monitor 3.0" in the Help and Support Knowledge Base at [https://support.microsoft.com/kb/933741](https://support.microsoft.com/kb/933741).

## Sample DPWS Filters

Sometimes, WS-Discovery and metadata exchange troubleshooting must take place on a busy network. The sample filters can be used to help limit the Netmon output to traffic of interest. For more information about using Netmon filters, see [https://support.microsoft.com/kb/933741](https://support.microsoft.com/kb/933741).

The following example shows a filter that limits output to all broadcast WS-Discovery traffic.

> [!Note]  
> This filter does not capture traffic from stacks that do not respond to multicast WS-Discovery messages that originate at port 3702. If such a stack is being used, then this sample filter must be modified before use.

 

``` syntax
// All broadcast WS-Discovery traffic
UDP.Port == 3702
```

The following example shows a filter that limits output to HTTP messages sent to WSDAPI stacks on the default port.

> [!Note]  
> Services may send relevant HTTP messages from ports other than 5357. If traffic from other ports is of interest, then this sample filter must be modified before use.

 

``` syntax
// HTTP messages sent to WSDAPI stacks on default port
TCP.Port == 5357
```

The following example shows a filter that limits output to IPv4 multicast traffic.

``` syntax
// All IPv4 multicast traffic
IPv4.DestinationAddress == 239.255.255.250
```

The following example shows a filter that limits output to IPv6 multicast traffic.

``` syntax
// All IPv6 multicast traffic
IPv6.DestinationAddress == FF02::C
```

Some filters can be combined to further limit results. The following example shows a filter that limits output to IPv4 multicast WS-Discovery traffic.

``` syntax
// All IPv4 multicast WS-Discovery traffic
UDP.Port==3702 && IPv4.DestinationAddress=239.255.255.250
```

When these filters are used, relevant traffic may be excluded from the Netmon results. Exclusion can occur when services reside at ports other than the default ports (5357/5358) and when a DPWS stack does not respond to messages using the default port. In these cases, the filters must be modified before use.

## Related topics

<dl> <dt>

[WSDAPI Diagnostic Procedures](wsdapi-diagnostic-procedures.md)
</dt> <dt>

[Getting Started with WSDAPI Troubleshooting](getting-started-with-wsdapi-troubleshooting.md)
</dt> </dl>

 

 



