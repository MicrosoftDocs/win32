---
Description: 'The following enumerations support the Distributed Routing Table (DRT) API.'
ms.assetid: '38ce95a0-1603-42c2-8a5e-4370f52c8fc9'
title: Distributed Routing Table Enumerations
---

# Distributed Routing Table Enumerations

The following enumerations support the Distributed Routing Table (DRT) API.



| Enumeration                                                            | Description                                                                                                                                                           |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DRT\_SCOPE**](drt-scope.md)                                        | Defines the set of IPv6 scopes in which DRT will operate when using the IPv6 UDP transport created by [**DrtCreateIpv6UdpTransport**](drtcreateipv6udptransport.md). |
| [**DRT\_ADDRESS\_FLAGS**](drt-address-flags.md)                       | Defines the set of responses that may be returned by an intermediate node when performing a search for a key.                                                         |
| [**DRT\_STATUS**](drt-status.md)                                      | Defines the possible connectivity and error states of a local node.                                                                                                   |
| [**DRT\_MATCH\_TYPE**](drt-match-type.md)                             | Defines the exactness of results returned when a search is performed.                                                                                                 |
| [**DRT\_LEAFSET\_KEY\_CHANGE\_TYPE**](drt-leafset-key-change-type.md) | Defines the set of change types that can be performed on a local leaf set node in the local DRT cache.                                                                |
| [**DRT\_EVENT\_TYPE**](drt-event-type.md)                             | Defines the set of events that can be raised by the DRT.                                                                                                              |
| [**DRT\_SECURITY\_MODE**](drt-security-mode.md)                       | Defines the possible security modes of the DRT. This enumeration is a field of the [**DRT\_SETTINGS**](drt-settings.md) structure.                                   |
| [**DRT\_REGISTRATION\_STATE**](drt-registration-state.md)             | Defines the state of a registered key.                                                                                                                                |



 

## Related topics

<dl> <dt>

[Distributed Routing Table Structures](distributed-routing-table-structures.md)
</dt> <dt>

[Distributed Routing Table Functions](distributed-routing-table-functions.md)
</dt> <dt>

[Distributed Routing Table API Reference](distributed-routing-table-api-reference.md)
</dt> </dl>

 

 



