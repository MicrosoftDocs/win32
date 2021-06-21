---
title: Negotiation Discovery Transport Mode in Boundary Mode
description: The Negotiation Discovery Transport Mode in Boundary Mode IPsec policy scenario requests IPsec transport mode protection for all matching traffic.
ms.assetid: 36ae74b3-30f5-49bd-8855-6f3c0fb04d70
ms.topic: article
ms.date: 05/31/2018
---

# Negotiation Discovery Transport Mode in Boundary Mode

The Negotiation Discovery Transport Mode in Boundary Mode IPsec policy scenario requests IPsec transport mode protection for all matching traffic. If the IKE/AuthIP negotiation fails, both inbound and outbound connections are allowed to fallback to clear-text .

This IPsec policy is typically used on machines that are accessed by both IPsec capable and non-IPsec capable machines.

An example of a potential Negotiation Discovery Transport Mode scenario is "Secure all unicast data traffic, except ICMP, using IPsec transport mode and enable negotiation discovery in boundary mode."

To implement this example programmatically, use the following WFP configuration.

<dl>

**At FWPM\_LAYER\_IKEEXT\_V{4\|6} setup MM negotiation policy**  

1.  Add one or both of the following MM policy provider contexts.  
    -   For IKE, a policy provider context of type FWPM\_IPSEC\_IKE\_MM\_CONTEXT.
    -   For AuthIP, a policy provider context of type FWPM\_IPSEC\_AUTHIP\_MM\_CONTEXT.

    > [!Note]  
    > A common keying module will be negotiated and the corresponding MM policy will be applied. AuthIP is the preferred keying module if both IKE and AuthIP are supported.

     

2.  For each of the contexts added in step 1, add a filter with the following properties.

    | Filter property        | Value                                            |
    |------------------------|--------------------------------------------------|
    | Filtering conditions   | Empty. All traffic will match the filter.        |
    | **providerContextKey** | GUID of the MM provider context added in step 1. |

        

**At FWPM\_LAYER\_IPSEC\_V{4\|6} setup QM and EM negotiation policy**  

1.  Add one or both of the following QM transport mode policy provider contexts and set the [**IPSEC\_POLICY\_FLAG\_ND\_BOUNDARY**](/windows/desktop/api/Ipsectypes/ns-ipsectypes-ipsec_transport_policy0) flag.  
    -   For IKE, a policy provider context of type **FWPM\_IPSEC\_IKE\_QM\_TRANSPORT\_CONTEXT**.
    -   For AuthIP, a policy provider context of type **FWPM\_IPSEC\_AUTHIP\_QM\_TRANSPORT\_CONTEXT**. This context can optionally contain the AuthIP Extended Mode (EM) negotiation policy.

    > [!Note]  
    > A common keying module will be negotiated and the corresponding QM policy will be applied. AuthIP is the preferred keying module if both IKE and AuthIP are supported.

     

2.  For each of the contexts added in step 1, add a filter with the following properties.

    | Filter property        | Value                                            |
    |------------------------|--------------------------------------------------|
    | Filtering conditions   | Empty. All traffic will match the filter.        |
    | **providerContextKey** | GUID of the QM provider context added in step 1. |

        

**At FWPM\_LAYER\_INBOUND\_TRANSPORT\_V{4\|6} setup inbound per-packet filtering rules**  

1.  Add a filter with the following properties. 

    | Filter property                                                   | Value                                                                                              |
    |-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS\_TYPE** filtering condition | [NlatUnicast](/windows/win32/api/nldef/ne-nldef-nl_address_type)                                      |
    | **action.type**                                                   | **FWP\_ACTION\_CALLOUT\_TERMINATING**                                                              |
    | **action.calloutKey**                                             | **FWPM\_CALLOUT\_IPSEC\_INBOUND\_TRANSPORT\_V{4\|6}**                                              |
    | **rawContext**                                                    | [**FWPM\_CONTEXT\_IPSEC\_INBOUND\_PERSIST\_CONNECTION\_SECURITY**](filter-context-identifiers.md) |

        
2.  Exempt ICMP traffic from IPsec by adding a filter with the following properties.

    | Filter property                                                   | Value                                                                      |
    |-------------------------------------------------------------------|----------------------------------------------------------------------------|
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS\_TYPE** filtering condition | NlatUnicast                                                                |
    | **FWPM\_CONDITION\_IP\_PROTOCOL** filtering condition             | **IPPROTO\_ICMP{V6}**These constants are defined in winsock2.h.<br/> |
    | **action.type**                                                   | FWP\_ACTION\_PERMIT                                                        |
    | **weight**                                                        | [**FWPM\_WEIGHT\_RANGE\_IKE\_EXEMPTIONS**](filter-weight-identifiers.md)  |

        

**At FWPM\_LAYER\_OUTBOUND\_TRANSPORT\_V{4\|6} setup outbound per-packet filtering rules**  

1.  Add a filter with the following properties.

    | Filter property                                                   | Value                                                                                     |
    |-------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS\_TYPE** filtering condition | NlatUnicast                                                                               |
    | **action.type**                                                   | **FWP\_ACTION\_CALLOUT\_TERMINATING**                                                     |
    | **action.calloutKey**                                             | **FWPM\_CALLOUT\_IPSEC\_OUTBOUND\_TRANSPORT\_V{4\|6}**                                    |
    | **rawContext**                                                    | [**FWPM\_CONTEXT\_IPSEC\_OUTBOUND\_NEGOTIATE\_DISCOVER**](filter-context-identifiers.md) |

        
2.  Exempt ICMP traffic from IPsec by adding a filter with the following properties.

    | Filter property                                                   | Value                                                                      |
    |-------------------------------------------------------------------|----------------------------------------------------------------------------|
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS\_TYPE** filtering condition | NlatUnicast                                                                |
    | **FWPM\_CONDITION\_IP\_PROTOCOL** filtering condition             | **IPPROTO\_ICMP{V6}**These constants are defined in winsock2.h.<br/> |
    | **action.type**                                                   | **FWP\_ACTION\_PERMIT**                                                    |
    | **weight**                                                        | **FWPM\_WEIGHT\_RANGE\_IKE\_EXEMPTIONS**                                   |

        

</dl>

> [!Note]  
> As opposed to Negotiation Discovery Transport Mode, for Negotiation Discovery Transport Mode in Boundary Mode policy there is no need to add a filter at the **FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6}** layers because this policy allows inbound unprotected clear-text connections.

 

## Related topics

<dl> <dt>

[Sample code: Using Transport Mode](using-transport-mode.md)
</dt> <dt>

[ALE Layers](ale-layers.md)
</dt> <dt>

[**Built-in Callout Identifiers**](built-in-callout-identifiers.md)
</dt> <dt>

[Filtering Conditions](filtering-conditions.md)
</dt> <dt>

[**Filtering Layer Identifiers**](management-filtering-layer-identifiers-.md)
</dt> <dt>

[**FWPM\_ACTION0**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_action0)
</dt> <dt>

[**FWPM\_PROVIDER\_CONTEXT\_TYPE**](/windows/desktop/api/Fwpmtypes/ne-fwpmtypes-fwpm_provider_context_type)
</dt> </dl>

 

