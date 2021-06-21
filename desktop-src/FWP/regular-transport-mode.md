---
title: Transport Mode
description: The Transport Mode IPsec policy scenario requires IPsec transport mode protection for all matching traffic.
ms.assetid: 303f7cdc-fb7a-4e5c-8291-cadcb45035cb
ms.topic: article
ms.date: 05/31/2018
---

# Transport Mode

The Transport Mode IPsec policy scenario requires IPsec transport mode protection for all matching traffic. Any matching clear text traffic is dropped until the IKE or AuthIP negotiation has completed successfully. If the negotiation fails, connectivity with the corresponding IP address will remain broken.

An example of a possible Transport Mode scenario is "Secure all unicast data traffic, except ICMP, using IPsec transport mode."

To implement this example programmatically, use the following WFP configuration.

<dl>

**At FWPM\_LAYER\_IKEEXT\_V{4\|6} setup MM negotiation policy**  

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

        

**At FWPM\_LAYER\_IPSEC\_V{4\|6} setup QM and EM negotiation policy**  

1.  Add one or both of the following QM transport mode policy provider contexts.  
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

    | Filter property                                                   | Value                                                         |
    |-------------------------------------------------------------------|---------------------------------------------------------------|
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS\_TYPE** filtering condition | [NlatUnicast](/windows/win32/api/nldef/ne-nldef-nl_address_type) |
    | **action.type**                                                   | FWP\_ACTION\_CALLOUT\_TERMINATING                             |
    | **action.calloutKey**                                             | FWPM\_CALLOUT\_IPSEC\_INBOUND\_TRANSPORT\_V{4\|6}             |

        
2.  Exempt ICMP traffic from IPsec by adding a filter with the following properties.

    | Filter property                                                  | Value                                                                     |
    |------------------------------------------------------------------|---------------------------------------------------------------------------|
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS\_TYPE**filtering condition | NlatUnicast                                                               |
    | **FWPM\_CONDITION\_IP\_PROTOCOL** filtering condition            | IPPROTO\_ICMP{V6}These constants are defined in winsock2.h.<br/>    |
    | **action.type**                                                  | FWP\_ACTION\_PERMIT                                                       |
    | **weight**                                                       | [**FWPM\_WEIGHT\_RANGE\_IKE\_EXEMPTIONS**](filter-weight-identifiers.md) |

        

**At FWPM\_LAYER\_OUTBOUND\_TRANSPORT\_V{4\|6} setup outbound per-packet filtering rules**  

1.  Add a filter with the following properties.

    | Filter property                                                   | Value                                              |
    |-------------------------------------------------------------------|----------------------------------------------------|
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS\_TYPE** filtering condition | NlatUnicast                                        |
    | **action.type**                                                   | **FWP\_ACTION\_CALLOUT\_TERMINATING**              |
    | **action.calloutKey**                                             | FWPM\_CALLOUT\_IPSEC\_OUTBOUND\_TRANSPORT\_V{4\|6} |

        
2.  Exempt ICMP traffic from IPsec by adding a filter with the following properties.

    | Filter property                                                   | Value                                                                  |
    |-------------------------------------------------------------------|------------------------------------------------------------------------|
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS\_TYPE** filtering condition | NlatUnicast                                                            |
    | **FWPM\_CONDITION\_IP\_PROTOCOL** filtering condition             | IPPROTO\_ICMP{V6}These constants are defined in winsock2.h.<br/> |
    | **action.type**                                                   | FWP\_ACTION\_PERMIT                                                    |
    | **weight**                                                        | FWPM\_WEIGHT\_RANGE\_IKE\_EXEMPTIONS                                   |

        

</dl>

## Related topics

<dl> <dt>

[Sample code: Using Transport Mode](using-transport-mode.md)
</dt> <dt>

[**Filtering Layer Identifiers**](management-filtering-layer-identifiers-.md)
</dt> <dt>

[**Provider Context Types**](/windows/desktop/api/Fwpmtypes/ne-fwpmtypes-fwpm_provider_context_type)
</dt> <dt>

[Filtering Conditions](filtering-conditions.md)
</dt> <dt>

[**FWPM\_ACTION0**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_action0)
</dt> <dt>

[**Built-in Callout Identifiers**](built-in-callout-identifiers.md)
</dt> </dl>

 

