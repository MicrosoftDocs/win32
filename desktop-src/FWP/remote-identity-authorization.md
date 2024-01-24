---
title: Remote Identity Authorization
description: The Remote Identity Authorization IPsec policy scenario requires that inbound connections come from a specific set of remote security principals which are specified in a Windows security descriptor (SD) access control list (ACL).
ms.assetid: 4d9f83d6-6f56-4416-8c35-d0260f9e888c
ms.topic: article
ms.date: 05/31/2018
---

# Remote Identity Authorization

The Remote Identity Authorization IPsec policy scenario requires that inbound connections come from a specific set of remote security principals which are specified in a Windows security descriptor (SD) access control list (ACL). If the remote identity (as determined by IPsec) does not match the set of allowed identities, the connection will be dropped. This policy must be specified in conjunction with one of the transport mode policy options.

If AuthIP is enabled, two security descriptors can be specified, one corresponding to AuthIP main mode, and the other corresponding to AuthIP extended mode.

An example of a possible Negotiation Discovery Transport Mode scenario is "Secure all unicast data traffic, except ICMP, using IPsec transport mode, enable negotiation discovery, and restrict inbound access to remote identities allowed as per security descriptor SD1 (corresponding to IKE/AuthIP main mode) and security descriptor SD2 (corresponding to AuthIP extended mode), for all unicast traffic corresponding to TCP local port 5555."

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

1.  Add one or both of the following QM transport mode policy provider contexts and set the [**IPSEC\_POLICY\_FLAG\_ND\_SECURE**](/windows/desktop/api/Ipsectypes/ns-ipsectypes-ipsec_transport_policy0) flag.  
    -   For IKE, a policy provider context of type **FWPM\_IPSEC\_IKE\_QM\_TRANSPORT\_CONTEXT**.
    -   For AuthIP, a policy provider context of type **FWPM\_IPSEC\_AUTHIP\_QM\_TRANSPORT\_CONTEXT** that contains the AuthIP Extended Mode (EM) negotiation policy.

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

    | Filter property                                                   | Value                                                                  |
    |-------------------------------------------------------------------|------------------------------------------------------------------------|
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS\_TYPE** filtering condition | NlatUnicast                                                            |
    | **FWPM\_CONDITION\_IP\_PROTOCOL** filtering condition             | IPPROTO\_ICMP{V6}These constants are defined in winsock2.h.<br/> |
    | **action.type**                                                   | **FWP\_ACTION\_PERMIT**                                                |
    | **weight**                                                        | **FWPM\_WEIGHT\_RANGE\_IKE\_EXEMPTIONS**                               |

        

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

        
3.  Add a filter with the following properties. This filter will permit inbound connections to TCP port 5555 if the corresponding remote identities are allowed by both SD1 and SD2. 

    | Filter property                                                   | Value                                                              |
    |-------------------------------------------------------------------|--------------------------------------------------------------------|
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS\_TYPE** filtering condition | NlatUnicast                                                        |
    | **FWPM\_CONDITION\_IP\_PROTOCOL** filtering condition             | **IPPROTO\_TCP**This constant is defined in winsock2.h.<br/> |
    | **FWPM\_CONDITION\_IP\_LOCAL\_PORT** filtering condition          | 5555                                                               |
    | **FWPM\_CONDITION\_ALE\_REMOTE\_MACHINE\_ID**                     | SD1                                                                |
    | **FWPM\_CONDITION\_ALE\_REMOTE\_USER\_ID**                        | SD2                                                                |
    | **action.type**                                                   | **FWP\_ACTION\_CALLOUT\_TERMINATING**                              |
    | **action.calloutKey**                                             | **FWPM\_CALLOUT\_IPSEC\_INBOUND\_INITIATE\_SECURE\_V{4\|6}**       |

        
4.  Add a filter with the following properties. This filter will block any other inbound connections to TCP port 5555 that did not match the previous filter. 

    | Filter property                                                   | Value                                                              |
    |-------------------------------------------------------------------|--------------------------------------------------------------------|
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS\_TYPE** filtering condition | NlatUnicast                                                        |
    | **FWPM\_CONDITION\_IP\_PROTOCOL** filtering condition             | **IPPROTO\_TCP**This constant is defined in winsock2.h.<br/> |
    | **FWPM\_CONDITION\_IP\_LOCAL\_PORT** filtering condition          | 5555                                                               |
    | **action.type**                                                   | **FWP\_ACTION\_BLOCK**                                             |

        

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

 

