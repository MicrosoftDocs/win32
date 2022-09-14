---
title: Manual SA
description: The Manual Security Association (SA) IPsec policy scenario allows callers to bypass the built-in IPsec keying modules (IKE and AuthIP) by directly specifying IPsec SAs to secure any network traffic.
ms.assetid: 2bcc0b40-ca43-43c6-b1e4-b64426ef7ff4
ms.topic: article
ms.date: 05/31/2018
---

# Manual SA

The Manual Security Association (SA) IPsec policy scenario allows callers to bypass the built-in IPsec keying modules (IKE and AuthIP) by directly specifying IPsec SAs to secure any network traffic.

An example of a possible Manual SA scenario is "Add an IPsec SA pair to secure all unicast data traffic between IP addresses 1.1.1.1 & 2.2.2.2, except ICMP, using IPsec transport mode."

> [!Note]  
> The following steps must be executed on both machines with IP addresses appropriately set.

 

To implement this example programmatically, use the following WFP configuration.

<dl>

**At FWPM\_LAYER\_INBOUND\_TRANSPORT\_V{4\|6} setup inbound per-packet filtering rules**  

1.  Add a filter with the following properties. 

    | Filter property                                                   | Value                                                         |
    |-------------------------------------------------------------------|---------------------------------------------------------------|
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS\_TYPE** filtering condition | [NlatUnicast](/windows/win32/api/nldef/ne-nldef-nl_address_type) |
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS**                           | The appropriate local address (1.1.1.1 or 2.2.2.2).           |
    | **FWPM\_CONDITION\_IP\_REMOTE\_ADDRESS**                          | The appropriate remote address (1.1.1.1 or 2.2.2.2).          |
    | **action.type**                                                   | **FWP\_ACTION\_CALLOUT\_TERMINATING**                         |
    | **action.calloutKey**                                             | **FWPM\_CALLOUT\_IPSEC\_INBOUND\_TRANSPORT\_V{4\|6}**         |

        
2.  Exempt ICMP traffic from IPsec by adding a filter with the following properties. 

    | Filter property                                                   | Value                                                                      |
    |-------------------------------------------------------------------|----------------------------------------------------------------------------|
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS\_TYPE** filtering condition | NlatUnicast                                                                |
    | **FWPM\_CONDITION\_IP\_PROTOCOL** filtering condition             | **IPPROTO\_ICMP{V6}**These constants are defined in winsock2.h.<br/> |
    | **action.type**                                                   | **FWP\_ACTION\_PERMIT**                                                    |
    | **weight**                                                        | [**FWPM\_WEIGHT\_RANGE\_IKE\_EXEMPTIONS**](filter-weight-identifiers.md)  |

        

**At FWPM\_LAYER\_OUTBOUND\_TRANSPORT\_V{4\|6} setup outbound per-packet filtering rules**  

1.  Add a filter with the following properties. 

    | Filter property                                                   | Value                                                  |
    |-------------------------------------------------------------------|--------------------------------------------------------|
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS\_TYPE** filtering condition | NlatUnicast                                            |
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS** filtering condition       | The appropriate local address (1.1.1.1 or 2.2.2.2).    |
    | **FWPM\_CONDITION\_IP\_REMOTE\_ADDRESS** filtering condition      | The appropriate remote address (1.1.1.1 or 2.2.2.2).   |
    | **action.type**                                                   | **FWP\_ACTION\_CALLOUT\_TERMINATING**                  |
    | **action.calloutKey**                                             | **FWPM\_CALLOUT\_IPSEC\_OUTBOUND\_TRANSPORT\_V{4\|6}** |

        
2.  Exempt ICMP traffic from IPsec by adding a filter with the following properties. 

    | Filter property                                                   | Value                                                                      |
    |-------------------------------------------------------------------|----------------------------------------------------------------------------|
    | **FWPM\_CONDITION\_IP\_LOCAL\_ADDRESS\_TYPE** filtering condition | NlatUnicast                                                                |
    | **FWPM\_CONDITION\_IP\_PROTOCOL** filtering condition             | **IPPROTO\_ICMP{V6}**These constants are defined in winsock2.h.<br/> |
    | **action.type**                                                   | **FWP\_ACTION\_PERMIT**                                                    |
    | **weight**                                                        | **FWPM\_WEIGHT\_RANGE\_IKE\_EXEMPTIONS**                                   |

        

**Setup inbound and outbound security associations**

1.  Call [**IPsecSaContextCreate0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextcreate0), with the *outboundTraffic* parameter containing the IP addresses as 1.1.1.1 & 2.2.2.2, and **ipsecFilterId** as the LUID of the outbound transport layer IPsec callout filter added above.
2.  Call [**IPsecSaContextGetSpi0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextgetspi0), with the *id* parameter containing the context ID returned from [**IPsecSaContextCreate0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextcreate0), and the *getSpi* parameter containing the IP addresses as 1.1.1.1 & 2.2.2.2, and **ipsecFilterId** as the LUID of the inbound transport layer IPsec callout filter added above. The returned SPI value is meant to be used as the inbound SA SPI by the local machine and as the outbound SA SPI by the corresponding remote machine. Both machines must use some out-of-band means to exchange the SPI values.
3.  Call [**IPsecSaContextAddInbound0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextaddinbound0), with the *id* parameter containing the context ID returned from [**IPsecSaContextCreate0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextcreate0), and the *inboundBundle* parameter describing the properties of the inbound SA bundle (such as the inbound SA SPI, transform type, algorithm types, keys, etc).
4.  Call [**IPsecSaContextAddOutbound0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextaddoutbound0), with the *id* parameter containing the context ID returned from [**IPsecSaContextCreate0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextcreate0), and the *outboundBundle* parameter describing the properties of the outbound SA bundle (such as the outbound SA SPI, transform type, algorithm types, keys, etc).

  
</dl>

## Related topics

<dl> <dt>

[Sample code: Manual SA Keying](manual-sa-keying.md)
</dt> <dt>

[**Built-in Callout Identifiers**](built-in-callout-identifiers.md)
</dt> <dt>

[**Filtering Layer Identifiers**](management-filtering-layer-identifiers-.md)
</dt> <dt>

[**FWPM\_ACTION0**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_action0)
</dt> </dl>

 

