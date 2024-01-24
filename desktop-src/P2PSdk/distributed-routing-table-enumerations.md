---
description: The following enumerations support the Distributed Routing Table (DRT) API.
ms.assetid: 38ce95a0-1603-42c2-8a5e-4370f52c8fc9
title: Distributed Routing Table Enumerations
ms.topic: article
ms.date: 05/31/2018
---

# Distributed Routing Table Enumerations

The following enumerations support the Distributed Routing Table (DRT) API.



| Enumeration                                                            | Description                                                                                                                                                           |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DRT\_SCOPE**](/windows/desktop/api/drt/ne-drt-drt_scope)                                        | Defines the set of IPv6 scopes in which DRT will operate when using the IPv6 UDP transport created by [**DrtCreateIpv6UdpTransport**](/windows/desktop/api/drt/nf-drt-drtcreateipv6udptransport). |
| [**DRT\_ADDRESS\_FLAGS**](/windows/desktop/api/drt/ne-drt-drt_address_flags)                       | Defines the set of responses that may be returned by an intermediate node when performing a search for a key.                                                         |
| [**DRT\_STATUS**](/windows/desktop/api/drt/ne-drt-drt_status)                                      | Defines the possible connectivity and error states of a local node.                                                                                                   |
| [**DRT\_MATCH\_TYPE**](/windows/desktop/api/drt/ne-drt-drt_match_type)                             | Defines the exactness of results returned when a search is performed.                                                                                                 |
| [**DRT\_LEAFSET\_KEY\_CHANGE\_TYPE**](/windows/desktop/api/drt/ne-drt-drt_leafset_key_change_type) | Defines the set of change types that can be performed on a local leaf set node in the local DRT cache.                                                                |
| [**DRT\_EVENT\_TYPE**](/windows/desktop/api/drt/ne-drt-drt_event_type)                             | Defines the set of events that can be raised by the DRT.                                                                                                              |
| [**DRT\_SECURITY\_MODE**](/windows/desktop/api/drt/ne-drt-drt_security_mode)                       | Defines the possible security modes of the DRT. This enumeration is a field of the [**DRT\_SETTINGS**](/windows/desktop/api/drt/ns-drt-drt_settings) structure.                                   |
| [**DRT\_REGISTRATION\_STATE**](/windows/desktop/api/drt/ne-drt-drt_registration_state)             | Defines the state of a registered key.                                                                                                                                |



 

## Related topics

<dl> <dt>

[Distributed Routing Table Structures](distributed-routing-table-structures.md)
</dt> <dt>

[Distributed Routing Table Functions](distributed-routing-table-functions.md)
</dt> <dt>

[Distributed Routing Table API Reference](distributed-routing-table-api-reference.md)
</dt> </dl>

 

 



