---
title: Guaranteed Encryption
description: The Guaranteed Encryption IPsec policy scenario requires IPsec encryption for all matching traffic. This policy must be specified in conjunction with one of the transport mode policy options.
ms.assetid: 68758f0c-f134-4b7a-820a-313e2a82f280
ms.topic: article
ms.date: 05/31/2018
---

# Guaranteed Encryption

The Guaranteed Encryption IPsec policy scenario requires IPsec encryption for all matching traffic. This policy must be specified in conjunction with one of the transport mode policy options.

Guaranteed Encryption is typically used to encrypt sensitive traffic on a per application basis.

An example of a possible Guaranteed Encryption scenario is "Secure all unicast data traffic, except ICMP, using IPsec transport mode, enable negotiation discovery, and require guaranteed encryption for all unicast traffic corresponding to TCP local port 5555."

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

1.  Add one or both of the following QM transport mode policy provider contexts and set the [**IPSEC\_POLICY\_FLAG\_ND\_SECURE**](/windows/desktop/api/Ipsectypes/ns-ipsectypes-ipsec_transport_policy0) flag.  
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

    | Filter property                                               | Value                                                                                              |
    |---------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
    | FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS\_TYPE filtering condition | [NlatUnicast](/windows/win32/api/nldef/ne-nldef-nl_address_type)                                      |
    | **action.type**                                               | **FWP\_ACTION\_CALLOUT\_TERMINATING**                                                              |
    | **action.calloutKey**                                         | **FWPM\_CALLOUT\_IPSEC\_INBOUND\_TRANSPORT\_V{4\|6}**                                              |
    | **rawContext**                                                | [**FWPM\_CONTEXT\_IPSEC\_INBOUND\_PERSIST\_CONNECTION\_SECURITY**](filter-context-identifiers.md) |

        
2.  Exempt ICMP traffic from IPsec by adding a filter with the following properties.

    | Filter property                                                   | Value                                                                      |
    |-------------------------------------------------------------------|----------------------------------------------------------------------------|
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS\_TYPE** filtering condition | NlatUnicast                                                                |
    | **FWPM\_CONDITION\_IP\_PROTOCOL** filtering condition             | **IPPROTO\_ICMP{V6}**These constants are defined in winsock2.h.<br/> |
    | **action.type**                                                   | **FWP\_ACTION\_PERMIT**                                                    |
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

        

**At FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V{4\|6} setup inbound per-connection filtering rules**  

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

        
3.  Add a filter with the following properties. This filter will only permit inbound connections to TCP port 5555 if they are encrypted.

    | Filter property                                                   | Value                                                                                                 |
    |-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS\_TYPE** filtering condition | NlatUnicast                                                                                           |
    | **FWPM\_CONDITION\_IP\_PROTOCOL** filtering condition             | **IPPROTO\_TCP**This constant is defined in winsock2.h.<br/>                                    |
    | **FWPM\_CONDITION\_IP\_LOCAL\_PORT** filtering condition          | 5555                                                                                                  |
    | **action.type**                                                   | **FWP\_ACTION\_CALLOUT\_TERMINATING**                                                                 |
    | **action.calloutKey**                                             | **FWPM\_CALLOUT\_IPSEC\_INBOUND\_INITIATE\_SECURE\_V{4\|6}**                                          |
    | **rawContext**                                                    | [**FWPM\_CONTEXT\_ALE\_SET\_CONNECTION\_REQUIRE\_IPSEC\_ENCRYPTION**](filter-context-identifiers.md) |

        

**At FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V{4\|6} setup outbound per-connection filtering rules**

-   Add a filter with the following properties. This filter will only permit outbound connections from TCP port 5555 if they are encrypted.

    | Filter property                                                   | Value                                                                                                 |
    |-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS\_TYPE** filtering condition | NlatUnicast                                                                                           |
    | **FWPM\_CONDITION\_IP\_PROTOCOL** filtering condition             | **IPPROTO\_TCP**This constant is defined in winsock2.h.<br/>                                    |
    | **FWPM\_CONDITION\_IP\_LOCAL\_PORT** filtering condition          | 5555                                                                                                  |
    | **action.type**                                                   | **FWP\_ACTION\_CALLOUT\_TERMINATING**                                                                 |
    | **action.calloutKey**                                             | **FWPM\_CALLOUT\_IPSEC\_ALE\_CONNECT\_V{4\|6}**                                                       |
    | **rawContext**                                                    | [**FWPM\_CONTEXT\_ALE\_SET\_CONNECTION\_REQUIRE\_IPSEC\_ENCRYPTION**](filter-context-identifiers.md) |

      

  
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

 

