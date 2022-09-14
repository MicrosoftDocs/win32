---
title: Tunnel Mode
description: The Tunnel Mode IPsec policy scenario is used to apply IPsec tunnel mode protection for all matching traffic between two tunnel endpoints.
ms.assetid: 170046c5-28ec-4341-89e2-93494bf9c6b8
ms.topic: article
ms.date: 05/31/2018
---

# Tunnel Mode

The Tunnel Mode IPsec policy scenario is used to apply IPsec tunnel mode protection for all matching traffic between two tunnel endpoints.

This policy scenario is typically used to protect traffic between multiple branch-office subnets, when it gets forwarded between the corresponding gateways on the Internet. It can also be used to secure end-to-end communication between two host machines, also referred to as point-to-point tunnels.

To implement Tunnel Mode policy using the Windows Filtering Platform (WFP), call the [**FwpmIPsecTunnelAdd0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmipsectunneladd0) function that instantiates the appropriate tunnel mode filters at the appropriate layers on behalf of the caller. The caller needs to specify the Main Mode, Quick Mode provider contexts, and the filter conditions describing the traffic that should be secured inside the tunnel.

## Related topics

<dl> <dt>

[Sample code: Using Tunnel Mode](using-tunnel-mode.md)
</dt> <dt>

[**Filtering Layer Identifiers**](management-filtering-layer-identifiers-.md)
</dt> </dl>

 

 




