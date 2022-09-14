---
title: Negotiation Discovery Transport Mode
description: The Negotiation Discovery Transport Mode IPsec policy scenario requires IPsec transport mode protection for all matching inbound traffic, and requests IPsec protection for matching outbound traffic.
ms.assetid: c08d9d03-7d77-43c2-8468-964b498b45f8
ms.topic: article
ms.date: 05/31/2018
---

# Negotiation Discovery Transport Mode

The Negotiation Discovery Transport Mode IPsec policy scenario requires IPsec transport mode protection for all matching inbound traffic, and requests IPsec protection for matching outbound traffic. Therefore, outbound connections are allowed to fallback to clear-text while inbound connections are not.

With this policy, when the host machine attempts a new outbound connection and there is no existing IPsec SA matching the traffic, the host simultaneously sends the packets in clear-text and starts an IKE or AuthIP negotiation. If the negotiation succeeds, the connection is upgraded to IPsec-protected. Otherwise, the connection stays in clear-text. Once IPsec-protected, a connection can never be downgraded to clear-text.

Negotiation Discovery Transport Mode is typically used in environments that include both IPsec capable and non-IPsec capable machines.

An example of a possible Negotiation Discovery Transport Mode scenario is "Secure all unicast data traffic, except ICMP, using IPsec transport mode, and enable negotiation discovery."

To implement this example programmatically, use the following WFP configuration.

<dl>

**At FWPM\_LAYER\_IKEEXT\_V{4\|6} set up MM negotiation policy**  

1.  Add one or both of the following MM policy provider contexts.  
    -   For IKE, a policy provider context of type **FWPM\_IPSEC\_IKE\_MM\_CONTEXT**.
    -   For AuthIP, a policy provider context of type **FWPM\_IPSEC\_AUTHIP\_MM\_CONTEXT**.

    > [!Note]  
    > A common keying module will be negotiated and the corresponding MM policy will be applied. AuthIP is the preferred keying module if both IKE and AuthIP are supported.

     

2.  For each of the contexts added in step 1, add a filter with the following properties. 

    | Filter property        | Value                                            |
    |------------------------|--------------------------------------------------|
    | Filtering conditions   | Empty. All traffic will match the filter.        |
    | **providerContextKey** | GUID of the MM provider context added in step 1. |

        

**At FWPM\_LAYER\_IPSEC\_V{4\|6} set up QM and EM negotiation policy**  

1.  Add one or both of the following QM transport mode policy provider contexts and set the [**IPSEC\_POLICY\_FLAG\_ND\_SECURE**](/windows/desktop/api/Ipsectypes/ns-ipsectypes-ipsec_transport_policy0) flag.  
    -   For IKE, a policy provider context of type FWPM\_IPSEC\_IKE\_QM\_TRANSPORT\_CONTEXT.
    -   For AuthIP, a policy provider context of type FWPM\_IPSEC\_AUTHIP\_QM\_TRANSPORT\_CONTEXT. This context can optionally contain the AuthIP Extended Mode (EM) negotiation policy.

    > [!Note]  
    > A common keying module will be negotiated and the corresponding QM policy will be applied. AuthIP is the preferred keying module if both IKE and AuthIP are supported.

     

2.  For each of the contexts added in step 1, add a filter with the following properties. 

    | Filter property        | Value                                            |
    |------------------------|--------------------------------------------------|
    | Filtering conditions   | Empty. All traffic will match the filter.        |
    | **providerContextKey** | GUID of the QM provider context added in step 1. |

        

**At FWPM\_LAYER\_INBOUND\_TRANSPORT\_V{4\|6} set up inbound per-packet filtering rules**  

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
    | **action.type**                                                   | **FWP\_ACTION\_PERMIT**                                                    |
    | **weight**                                                        | [**FWPM\_WEIGHT\_RANGE\_IKE\_EXEMPTIONS**](filter-weight-identifiers.md)  |

        

**At FWPM\_LAYER\_OUTBOUND\_TRANSPORT\_V{4\|6} set up outbound per-packet filtering rules**  

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

        

**At FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6} set up inbound per-connection filtering rules**  

1.  Add a filter with the following properties. This filter will only allow inbound connection attempts if they are secured by IPsec. 

    | Filter property                                                   | Value                                                        |
    |-------------------------------------------------------------------|--------------------------------------------------------------|
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS\_TYPE** filtering condition | NlatUnicast                                                  |
    | **action.type**                                                   | **FWP\_ACTION\_CALLOUT\_TERMINATING**                        |
    | **action.calloutKey**                                             | **FWPM\_CALLOUT\_IPSEC\_INBOUND\_INITIATE\_SECURE\_V{4\|6}** |

        
2.  Exempt ICMP traffic from IPsec by adding a filter with the following properties.

    | Filter property                                                   | Value                                                                      |
    |-------------------------------------------------------------------|----------------------------------------------------------------------------|
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS\_TYPE** filtering condition | NlatUnicast                                                                |
    | **FWPM\_CONDITION\_IP\_PROTOCOL** filtering condition             | **IPPROTO\_ICMP{V6}**These constants are defined in winsock2.h.<br/> |
    | **action.type**                                                   | **FWP\_ACTION\_PERMIT**                                                    |
    | **weight**                                                        | **FWPM\_WEIGHT\_RANGE\_IKE\_EXEMPTIONS**                                   |

        

</dl>

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

 

