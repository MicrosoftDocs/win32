---
title: Route Flags
description: Route Flags
ms.assetid: 17deae88-573f-48ec-887e-521549b39c32
keywords:
- Route
- Route Flags
ms.topic: article
ms.date: 05/31/2018
---

# Route Flags

## State of the Route Constants



| Constant                    | Value | Description             |
|-----------------------------|-------|-------------------------|
| RTM\_ROUTE\_STATE\_CREATED  | 0     | Route has been created. |
| RTM\_ROUTE\_STATE\_DELETING | 1     | Route is being deleted. |
| RTM\_ROUTE\_STATE\_DELETED  | 2     | Route has been deleted. |



 

## Route Update Flags



| Constant                  | Value      | Description                                                                                                                                                                                |
|---------------------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RTM\_ROUTE\_CHANGE\_FIRST | 0x01       | Indicates that the routing table manager should not check the **Neighbour** member of the [**RTM\_ROUTE\_INFO**](/windows/desktop/api/Rtmv2/ns-rtmv2-rtm_route_info) structure when determining when two routes are equal. |
| RTM\_ROUTE\_CHANGE\_NEW   | 0x02       | Returned by the routing table manager to indicate a new route was created.                                                                                                                 |
| RTM\_ROUTE\_CHANGE\_BEST  | 0x00010000 | Returned by the routing table manager to indicate that the route that was added or updated was the best route, or that because of the change, a new route became the best route.           |



 

## Unicast Flags



| Constant                  | Value  | Description                                                            |
|---------------------------|--------|------------------------------------------------------------------------|
| RTM\_ROUTE\_FLAGS\_LOCAL  | 0x0010 | Indicates a destination is on a directly reachable network.            |
| RTM\_ROUTE\_FLAGS\_REMOTE | 0x0020 | Indicates that the destination is not on a directly reachable network. |
| RTM\_ROUTE\_FLAGS\_MYSELF | 0x0040 | Indicates the destination is one of the router's addresses.            |



 

## Broadcast and Multicast Flags



| Constant                           | Value  | Description                                                                                                                                                                                                |
|------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RTM\_ROUTE\_FLAGS\_MCAST           | 0x0100 | Indicates that this route is a route to a multicast address.                                                                                                                                               |
| RTM\_ROUTE\_FLAGS\_LOCAL\_MCAST    | 0x0200 | Indicates that this route is a route to a local multicast address.                                                                                                                                         |
| RTM\_ROUTE\_FLAGS\_LIMITED\_BC     | 0x0400 | Indicates that this route is a limited broadcast address. Packets to this destination should not be forwarded.                                                                                             |
| RTM\_ROUTE\_FLAGS\_ZEROS\_NETBC    | 0x1000 | Indicates that the destination matches an interface's all-zeros broadcast address. If broadcast forwarding is enabled, packets should be received and resent out all appropriate interfaces.               |
| RTM\_ROUTE\_FLAGS\_ZEROS\_SUBNETBC | 0x2000 | Indicates that the destination matches an interface's all-zeros subnet broadcast address. If subnet broadcast forwarding is enabled, packets should be received and resent out all appropriate interfaces. |
| RTM\_ROUTE\_FLAGS\_ONES\_NETBC     | 0x4000 | Indicates that the destination matches an interface's all-ones broadcast address. If broadcast forwarding is enabled, packets should be received and resent out all appropriate interfaces.                |
| RTM\_ROUTE\_FLAGS\_ONES\_SUBNETBC  | 0x8000 | Indicates that the destination matches an interface's all-ones subnet broadcast address. If subnet broadcast forwarding is enabled, packets should be received and resent out all appropriate interfaces.  |



 

## Grouping of Flags



| Group                            | Members                                                                                                                                                                  | Description                                              |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| RTM\_ROUTE\_FLAGS\_FORWARDING    | RTM\_ROUTE\_FLAGS\_MARTIAN, RTM\_ROUTE\_FLAGS\_BLACKHOLE, RTM\_ROUTE\_FLAGS\_DISCARD, RTM\_ROUTE\_FLAGS\_INACTIVE                                                        | Specifies any forwarding flags.                          |
| RTM\_ROUTE\_FLAGS\_ANY\_UNICAST  | RTM\_ROUTE\_FLAGS\_LOCAL, RTM\_ROUTE\_FLAGS\_REMOTE, RTM\_ROUTE\_FLAGS\_MYSELF                                                                                           | Specifies any unicast flags.                             |
| RTM\_ROUTE\_FLAGS\_ANY\_MCAST    | RTM\_ROUTE\_FLAGS\_MCAST, RTM\_ROUTE\_FLAGS\_LOCAL\_MCAST                                                                                                                | Specifies any unicast flags.                             |
| RTM\_ROUTE\_FLAGS\_SUBNET\_BCAST | RTM\_ROUTE\_FLAGS\_ONES\_SUBNET\_BC, RTM\_ROUTE\_FLAGS\_ZEROS\_SUBNETBC                                                                                                  | Specifies any subnet broadcast flags.                    |
| RTM\_ROUTE\_FLAGS\_NET\_BCAST    | RTM\_ROUTE\_FLAGS\_ONES\_NETBC, RTM\_ROUTE\_FLAGS\_ZEROS\_NETBC                                                                                                          | Specifies any net-wide broadcast flags.                  |
| RTM\_ROUTE\_FLAGS\_ANY\_BCAST    | RTM\_ROUTE\_FLAGS\_LIMITED\_BC, RTM\_ROUTE\_FLAGS\_ONES\_NETBC, RTM\_ROUTE\_FLAGS\_ONES\_SUBNET\_BC, RTM\_ROUTE\_FLAGS\_ZEROS\_NETBC, RTM\_ROUTE\_FLAGS\_ZEROS\_SUBNETBC | Specifies any of the subnet or net-wide broadcast flags. |



 

 

 




