---
title: IKE/AuthIP Exemptions
description: Internet Key Exchange (IKE) and Authenticated Internet Protocol (AuthIP), in order to function, need to exempt their network traffic from the IPsec filtering.
ms.assetid: 365bfebc-250a-440f-8056-ff9601daa030
ms.topic: article
ms.date: 05/31/2018
---

# IKE/AuthIP Exemptions

The Internet Protocol security (IPsec) keying modules, Internet Key Exchange (IKE) and Authenticated Internet Protocol (AuthIP), in order to function, need to exempt their network traffic from the IPsec filtering.

In Windows Filtering Platform (WFP) the Base Filtering Engine (BFE) automatically adds IKE and AuthIP exemption filters when the first IKE or AuthIP main mode (MM) policy filter is added and deletes them when the last IKE or AuthIP MM policy filter is deleted. This way, the policy providers do not have to manage IKE and AuthIP filtering exemptions individually.

An IKE MM policy filter is a filter in the engine layer [**FWPM\_LAYER\_IKEEXT\_V{4\|6}**](management-filtering-layer-identifiers-.md) that references a provider context of type [**FWPM\_IPSEC\_IKE\_MM\_CONTEXT**](/windows/desktop/api/Fwpmtypes/ne-fwpmtypes-fwpm_provider_context_type).

An AuthIP MM policy filter is a filter in the engine layer [**FWPM\_LAYER\_IKEEXT\_V{4\|6}**](management-filtering-layer-identifiers-.md) that references a provider context of type [**FWPM\_IPSEC\_AUTHIP\_MM\_CONTEXT**](/windows/desktop/api/Fwpmtypes/ne-fwpmtypes-fwpm_provider_context_type).

An IKE or AuthIP exemption filter is a filter in the engine layer [**FWPM\_LAYER\_INBOUND\_TRANSPORT\_V{4\|6}**](management-filtering-layer-identifiers-.md) or **FWPM\_LAYER\_OUTBOUND\_TRANSPORT\_V{4\|6}** auto-weighted in the [**FWPM\_WEIGHT\_RANGE\_IKE\_EXEMPTIONS**](filter-weight-identifiers.md) weight range.

The IKE and AuthIP exemptions implemented by BFE are as follows.

| IP version      | Port                        | Exemption                                                                                                                                                                                                                             |
|-----------------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IPv4<br/> | UDP:500 UDP:4500<br/> | Permit IKE and AuthIP traffic at the inbound transport layer and at the outbound transport layer. <br/> Permit IKE and AuthIP traffic at the ALE receive/accept and connect layers, but restrict it to local system.<br/> |
| IPv6<br/> | UDP:500<br/>          | Permit IKE and AuthIP traffic at the inbound transport layer and at the outbound transport layer. <br/> Permit IKE and AuthIP traffic at the ALE receive/accept and connect layers, but restrict it to local system.<br/> |



 

The IKE and AuthIP exemption filters are open to all addresses. To implement a firewall with more granular control, policy providers should add filters in a weight range higher than [**FWPM\_WEIGHT\_RANGE\_IKE\_EXEMPTIONS**](filter-weight-identifiers.md).

## Related topics

<dl> <dt>

[IPsec Configuration](ipsec-configuration.md)
</dt> <dt>

[Filter Weight Assignment](filter-weight-assignment.md)
</dt> </dl>

 

 





