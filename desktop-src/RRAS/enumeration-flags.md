---
title: Enumeration Flags
description: Enumeration Flags
ms.assetid: d5677e3a-c0c1-4768-aae4-f6564a40ee99
keywords:
- Enumeration
- Enumeration Flags
ms.topic: article
ms.date: 05/31/2018
---

# Enumeration Flags



| Constant               | Value      | Description                                                                                                                                               |
|------------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| RTM\_ENUM\_START       | 0x00000000 | Enumerate routes or destinations starting at 0/0.                                                                                                         |
| RTM\_ENUM\_NEXT        | 0x00000001 | Enumerate routes or destinations starting at the specified address/mask length (such as 10/8). The enumeration continues to the end of the routing table. |
| RTM\_ENUM\_RANGE       | 0x00000002 | Enumerate routes or destinations in the specified subtree specified by the address/mask length (such as 10/8).                                            |
| RTM\_ENUM\_ALL\_DESTS  | 0x00000000 | Return all destinations.                                                                                                                                  |
| RTM\_ENUM\_OWN\_DESTS  | 0x01000000 | Return only those destinations that the client owns.                                                                                                      |
| RTM\_ENUM\_ALL\_ROUTES | 0x00000000 | Return all routes.                                                                                                                                        |
| RTM\_ENUM\_OWN\_ROUTES | 0x00010000 | Return only those routes that the client owns.                                                                                                            |



 

 

 




