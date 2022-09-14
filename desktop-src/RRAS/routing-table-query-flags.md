---
title: Routing Table Query Flags
description: Use these constants for router table queries.
ms.assetid: 345a8edc-c2aa-483e-8685-15a692bbfd56
keywords:
- Routing Table Query Flags
ms.topic: article
ms.date: 05/31/2018
---

# Routing Table Query Flags

Use these constants for router table queries.



| Constant              | Value      | Description                                                                |
|-----------------------|------------|----------------------------------------------------------------------------|
| RTM\_MATCH\_NONE      | 0x00000000 | Matches none of the criteria; all routes for the destination are returned. |
| RTM\_MATCH\_OWNER     | 0x00000001 | Matches routes with same owner.                                            |
| RTM\_MATCH\_NEIGHBOUR | 0x00000002 | Matches routes with the same neighbor.                                     |
| RTM\_MATCH\_PREF      | 0x00000004 | Matches routes that have the same preference.                              |
| RTM\_MATCH\_NEXTHOP   | 0x00000008 | Matches routes that have the same next hop.                                |
| RTM\_MATCH\_INTERFACE | 0x00000010 | Matches routes that are on the same interface.                             |
| RTM\_MATCH\_FULL      | 0x0000FFFF | Matches routes with all criteria.                                          |
| RTM\_BEST\_PROTOCOL   | 0          | Returns a route regardless of which protocol owns it.                      |
| RTM\_THIS\_PROTOCOL   | ~0         | Returns the best route for the calling protocol.                           |



 

 

 




