---
title: WFP Operation
description: Windows Filtering Platform (WFP) performs its tasks by integrating the following basic entities Layers, Filters, Shims, and Callouts.
ms.assetid: bf88ace7-1160-434b-9be0-3f9db6aa2e87
ms.topic: article
ms.date: 05/31/2018
---

# WFP Operation

Windows Filtering Platform (WFP) performs its tasks by integrating the following basic entities: *Layers*, *Filters*, *Shims*, and *Callouts*.

## Layers

A *layer* is a container managed by the filter engine whose function is to organize filters into sets. A layer is not a module in the network stack. Each layer has a schema that defines the type of filters that can be added to it. See [Filtering Conditions Available at Each Filtering Layer](filtering-conditions-available-at-each-filtering-layer.md) for more information.

Layers may contain sub-layers to manage conflicting filter requirements such as "Block TCP ports above 1024" and "Open port 1080". The rules for managing filtering conflicts are determined by [Filter Arbitration](filter-arbitration.md).

WFP contains a set of [built-in sub-layers](management-filtering-sublayer-identifiers.md). Every layer inherits all the built-in sub-layers. Users can also add their own sub-layers.

The list of filter engine layers is provided in the reference section topic [**Filtering Layer Identifiers**](management-filtering-layer-identifiers-.md).

## Filters

A *filter* is a rule that is matched against incoming or outgoing packets. The rule tells the filtering engine what to do with the packet, including to call a callout module for deep packet or stream inspection. For example, a filter may specify "Block traffic with a TCP port greater than 1024" or "Call out to IDS for all traffic that is not secured."

A boot-time filter is a filter that is enforced at boot-time as soon as the TCP/IP stack driver (tcpip.sys) starts. A boot-time filter is disabled when BFE starts. A filter is marked as boot-time by setting the [**FWPM\_FILTER\_FLAG\_BOOTTIME**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_filter0) flag when [**FwpmFilterAdd0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfilteradd0) is invoked.

A run-time filter is a filter that is enforced after BFE starts. A run-time filter can be static, dynamic, or persistent depending on the way it was created. See [Object Management](object-management.md) for more information on the different types of run-time filters and their lifetime.

## Shims

A *shim* is a kernel-mode component that makes filtering decisions by classifying against the filter engine layers. Each shim classifies against one or more layers. For example, the Transport Layer Module shim classifies against the Inbound Transport layer, the Outbound Transport layer, and the ALE Connect and Receive-Accept layers for the first packet of a flow.

As packets, streams, and events traverse the network stack, the shims parse them to extract the classifiable conditions and values, and then call into the filter engine to evaluate them against the filters in a given layer. The filter engine may invoke one or more callouts as part of the classification. The shims do the actual dropping of packets, streams, and events based on the result of the classification performed by the filter engine.

## Callouts

A *callout* is a set of functions exposed by a driver and used for specialized filtering. They are used to perform analysis and manipulation of the packets, such as virus scan, parental controls scan for inappropriate content, packet data parsing for monitoring tools. Some callouts, such as the Network Address Translation (NAT) driver, are built into the operating system. Others, such as an HTTP Parental Control callout or the Intrusion Detection System (IDS) callout, can be provided by independent software vendors (ISVs). The callout functions are invoked by the filter engine when a corresponding callout filter is matched at a given layer.

Callouts can be registered at any of the kernel-mode WFP layers. Callouts can return an action ("Block", "Permit", and, when performing stream inspection, "Defer", "Need more data", "Drop connection") and can modify and secure inbound and outbound network traffic.

Once a callout is registered with the filter engine, it can receive network traffic to process. The traffic may be packets, streams, or events depending on the layer. An application or firewall agent causes traffic to be passed to a callout by adding a filter whose action is "Callout" and whose callout ID is that callout's identifier. Callouts can instruct the filter engine to return "Block" or "Permit" to the shim. Callouts can also return "Continue" to allow other filters to process the packet.

Multiple callouts may be exposed by one callout driver.

A callout needs to be added (with [**FwpmCalloutAdd0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmcalloutadd0)) and registered (with [FwpsCalloutRegister](/windows-hardware/drivers/ddi/_netvista/)) before it can be used. A call to **FwpmCalloutAdd0** is required before the creation of filters that reference the callout. A call to FwpsCalloutRegister is required before WFP can invoke the callout when the callout filters are matched. By default filters that reference callouts that have been added but have not yet registered with the filter engine are treated as "Block" filters. The order of calling **FwpmCalloutAdd0** and FwpsCalloutRegister does not matter. A persistent callout needs to be added just once and needs to be registered every time the driver that implements the callout starts (for example, after a reboot).

## Classification

Classification is the process of applying filters to network traffic (packet, stream, or event) in order to determine a result of "Permit" or "Block" for that traffic. For one packet, stream, or event there is one classification call per layer.

During classification, the properties (for example, source address) of the packet, stream, or event are compared with filter conditions set on filters at the layer where the classification is invoked. When matches are found, the [Filter Arbitration](filter-arbitration.md) algorithm is used to determines the result of the classification process.

A classification request is triggered by a shim.

Classification actions could be either:

-   Permit
-   Block
-   Callout
    -   Permit
    -   Block
    -   Continue
    -   Defer
    -   Need more data
    -   Drop connection

## WFP Operation

At boot-time, as soon as the TCP/IP stack driver (tcpip.sys) starts, the kernel-mode filter engine enforces the security policy of the system through boot-time filters.

Once the Base Filtering Engine (BFE) starts in user mode, persistent filters are added to the platform, boot-time filters are disabled, and notifications are sent to those callout drivers that subscribed using [FwpmBfeStateSubscribeChanges0](/windows-hardware/drivers/ddi/fwpmk/nf-fwpmk-fwpmbfestatesubscribechanges0). The notifications are dispatched immediately after the BFE initialization is completed. The platform is now ready for callouts to be registered and for run-time objects to be added.

The transition from boot-time to persistent filters could be several seconds, or even longer on a slow machine. It is atomic, so if a provider has both a boot-time and a persistent filter, there will never be a window when neither is in effect.

After BFE starts, run-time filters can be added by firewall agents, or by custom firewall solutions. BFE processes these filters and sends them to the appropriate filter engine layer for enforcement. BFE also accepts authentication settings and sends these settings to the IPsec keying modules (IKE/AuthIP). See [IPsec Configuration](ipsec-configuration.md) for more information.

At any time, filters and authentication settings can be added, removed or changed in the system through the RPC interface exposed by the BFE. Sub-layers and callout modules can likewise be added or removed.

Data flow:

1.  A packet comes into the network stack.
2.  The network stack finds and calls a shim.
3.  The shim invokes the classification process at a particular layer.
4.  During classification, filters are matched and the resultant action is taken. (See [Filter Arbitration](filter-arbitration.md).)
5.  If any callout filters are matched during the classification process, the corresponding callouts are invoked.
6.  The shim acts on the final filtering decision (for example, drop the packet).

Outbound data flow follows a similar pattern.

The following topics further describe the operation of the WFP.

-   [TCP Packet Flows](tcp-packet-flows.md)
-   [UDP Packet Flows](udp-packet-flows.md)
-   [Filter Arbitration](filter-arbitration.md)

## Related topics

<dl> <dt>

[Object Model](object-model.md)
</dt> <dt>

[Object Management](object-management.md)
</dt> </dl>

 

 