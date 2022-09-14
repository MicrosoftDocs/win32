---
title: ALE Multicast/Broadcast Traffic
description: All inbound multicast and broadcast traffic at the Application Layer Enforcement (ALE) layers is mapped to one global ALE flow.
ms.assetid: b10b9758-8fce-4256-a25d-917e01336456
ms.topic: article
ms.date: 05/31/2018
---

# ALE Multicast/Broadcast Traffic

All inbound multicast and broadcast traffic at the Application Layer Enforcement (ALE) layers is mapped to one global [ALE flow](ale-stateful-filtering.md). Response traffic for inbound multicast and broadcast packets is classified at the [**FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6}**](management-filtering-layer-identifiers-.md) layer and separate ALE flows are created for each response.

Outbound multicast and broadcast traffic at the ALE layers creates a 4-second ALE flow. By default, the authorization of an outbound multicast or broadcast ALE packet will permit inbound traffic, whether unicast, multicast, or broadcast, from any remote address for up to 4 seconds. Such an ALE flow can only be refreshed or kept alive by subsequent outbound traffic that matches the ALE flow.

> [!Note]  
> The 4-second lifetime is specified by the built-in callout [**FWPM\_CALLOUT\_SET\_OPTIONS\_AUTH\_CONNECT\_LAYER\_V{4\|6}**](built-in-callout-identifiers.md). To alter the 4-second default lifetime, add a filter that references the **FWPM\_CALLOUT\_SET\_OPTIONS\_AUTH\_CONNECT\_LAYER\_V{4\|6}** callout. See [ALE Flow Customization](ale-flow-customization.md) for more information.

 

## Related topics

<dl> <dt>

[Application Layer Enforcement (ALE)](application-layer-enforcement--ale-.md)
</dt> <dt>

[ALE Layers](ale-layers.md)
</dt> <dt>

[ALE Stateful Filtering](ale-stateful-filtering.md)
</dt> <dt>

[ALE Reauthorization](ale-re-authorization.md)
</dt> <dt>

[ALE Flow Customization](ale-flow-customization.md)
</dt> </dl>

 

 




