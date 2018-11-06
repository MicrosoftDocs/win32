---
title: Change Notification Flags
description: Change Notification Flags
ms.assetid: 1f1aef71-a2b7-49ad-a0bc-f61f10b701c9
keywords:
- Change
- Change Notification Flags
ms.topic: article
ms.date: 05/31/2018
---

# Change Notification Flags



| Constant                         | Value      | Description                                                                                                                                                           |
|----------------------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RTM\_NUM\_CHANGE\_TYPES          | 3          | Specifies the number of change types that are currently used by the routing table manager.                                                                            |
| RTM\_CHANGE\_TYPE\_ALL           | 0x0001     | Notifies the client of any change to a destination.                                                                                                                   |
| RTM\_CHANGE\_TYPE\_BEST          | 0x0002     | Notifies the client of changes to the best route, or when the best route changes.                                                                                     |
| RTM\_CHANGE\_TYPE\_FORWARDING    | 0x0004     | Notifies the client of any best route changes that affect forwarding (such as next hop changes).                                                                      |
| RTM\_NOTIFY\_ONLY\_MARKED\_DESTS | 0x00010000 | Notifies the client of changes to destinations that the client has marked. If this flag is not specified, change notification messages for all destinations are sent. |



 

 

 




