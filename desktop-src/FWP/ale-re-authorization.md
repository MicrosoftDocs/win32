---
title: ALE Reauthorization
description: Network traffic at the Application Layer Enforcement (ALE) layers of the Windows Filtering Platform (WFP) is filtered by ALE flows.
ms.assetid: 3cc7f78e-3f9d-4a91-8ea0-9b64c299068a
ms.topic: article
ms.date: 05/31/2018
---

# ALE Reauthorization

Network traffic at the Application Layer Enforcement (ALE) layers of the Windows Filtering Platform (WFP) is filtered by [ALE flows](ale-stateful-filtering.md). Once an ALE flow has been permitted, all traffic that is part of the ALE flow is permitted. Reauthorization is a request to validate the permissions of the ALE flow, typically due to a change in network policy.

ALE flows are assigned a direction, inbound or outbound, based on the direction of the first packet that triggered the creation and authorization of the flow. Inbound ALE flows are created and authorized at the [**FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6}**](management-filtering-layer-identifiers-.md) layer. Outbound ALE flows are created and authorized at the **FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6}** layer. The direction of the ALE flow does not limit the direction of packets that belong to the flow. ALE flows contain both inbound and outbound packets regardless of the direction of the ALE flow itself.

Reauthorization of an ALE flow is triggered by:

-   A policy change at the layer where the ALE flow was originally authorized or created.
-   An arrival interface different from the interface where the ALE flow was originally authorized or created.
-   A pending connection.

Reauthorization is distinguished from the initial authorization by the presence of the [**FWP\_CONDITION\_FLAG\_IS\_REAUTHORIZE**](filtering-condition-flags-.md) flag.

Reauthorization can take place only at the [**FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6}**](management-filtering-layer-identifiers-.md) and **FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6}** layers.

### Policy-Change Reauthorization

A policy change is implemented as a filter addition or removal at an ALE layer. Once a policy change is detected, the first packet that traverses an ALE flow created at the affected layer will be specified for reauthorization to the layer. Therefore, for reauthorization it is entirely possible that an outbound packet is classified at the [**FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6}**](management-filtering-layer-identifiers-.md) layer and that an inbound packet is classified at the **FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6}** layer.

One reason for this mixed-direction classification is that there might not be further network traffic from the original direction (for example, inbound packet for inbound ALE flow). One such example is one-way UDP streaming after an initial two-way handshake. In this case it is more desirable to tear down the streaming as soon as possible.

### Arrival Interface Reauthorization

Arrival interface reauthorization is available starting with Windows Server 2008 and Windows Vista with Service Pack 1 (SP1).

Packets belonging to the same ALE flow can arrive from multiple interfaces. The first packet to come in over an interface different from the original interface of the ALE flow is reauthorized.

In a strong host model, which is the default security model for the TCP/IP stack, a connection on a network interface accepts only packets that come in on the same interface. Therefore, arrival interface reauthorization is not used on a strong host computer.

In a weak host model, a connection on a network interface allows packets coming in on any other network interface. Arrival interface reauthorization is used on a weak host computer to implement interface-specific policies. For more information, see ["The Cable Guy: Strong and Weak Host Models."](/previous-versions/technet-magazine/cc137807(v=msdn.10))

Some [classifiable fields](filtering-conditions.md) may be unknown during reauthorization. For example, if an outbound packet is being reauthorized at the [**FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6}**](management-filtering-layer-identifiers-.md) layer, all the fields pertaining to the arrival interface are unknown. In that case, the values of the unknown fields are indicated as [**FWP\_EMPTY**](/windows/desktop/api/Fwptypes/ne-fwptypes-fwp_data_type).

Fields of type [**FWP\_EMPTY**](/windows/desktop/api/Fwptypes/ne-fwptypes-fwp_data_type) can be matched with [**FWP\_MATCH\_EQUAL**](/windows/desktop/api/Fwptypes/ne-fwptypes-fwp_match_type). Therefore, a policy can be set to block reauthorizations and tear down an ALE flow when reauthorization requests for the ALE flow arrive.

## Pending Connection Reauthorization

A callout driver may postpone a classify operation at ALE layers and complete it at a later time, when the filtering decision can be safely made. The ALE postpone/complete functionality is supported via the kernel-mode functions [FwpsPendOperation0](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpspendoperation0) and [FwpsCompleteOperation0](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpscompleteoperation0).

The reauthorization is triggered immediately following the FwpsCompleteOperation0 call, and it allows the callout driver to permit or to block the flow.

Only an initial authorization can be postponed. A call to FwpsPendOperation0 will fail if [**FWP\_CONDITION\_FLAG\_IS\_REAUTHORIZE**](filtering-condition-flags-.md) flag is set.

For more information, see the [Windows Driver Kit](/windows-hardware/drivers/ddi/_netvista/) documentation.

## Related topics

<dl> <dt>

[Application Layer Enforcement (ALE)](application-layer-enforcement--ale-.md)
</dt> <dt>

[ALE Layers](ale-layers.md)
</dt> <dt>

[ALE Stateful Filtering](ale-stateful-filtering.md)
</dt> <dt>

[ALE Multicast/Broadcast Traffic](ale-multicast-broadcast-traffic.md)
</dt> <dt>

[ALE Flow Customization](ale-flow-customization.md)
</dt> </dl>

 

 