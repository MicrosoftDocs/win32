---
title: View Flags
description: Use the View Flags to control routing table views.
ms.assetid: 836e3400-0dca-4a21-9a5c-7da357ed72ea
ms.topic: article
ms.date: 05/31/2018
---

# View Flags

Use the View Flags to control routing table views.



| Constant                 | Value      | Description                                                      |
|--------------------------|------------|------------------------------------------------------------------|
| RTM\_MAX \_ADDRESS\_SIZE | 16         | Max address size for an address family.                          |
| RTM\_MAX\_VIEWS          | 32         | Maximum number of views that can be active in the routing table. |
| RTM\_VIEW\_ID\_UCAST     | 0          | Specifies a unicast view.                                        |
| RTM\_VIEW\_ID\_MCAST     | 1          | Specifies a multicast view.                                      |
| RTM\_VIEW\_MASK\_SIZE    | 0x20       | Specifies the maximum number of views that can be configured.    |
| RTM\_VIEW\_MASK\_NONE    | 0x00000000 | Returns information regardless of the view.                      |
| RTM\_VIEW\_MASK\_ANY     | 0x00000000 | Returns destinations from all views. This is the default value.  |
| RTM\_VIEW\_MASK\_UCAST   | 0x00000001 | Returns destinations from the unicast view.                      |
| RTM\_VIEW\_MASK\_MCAST   | 0x00000002 | Returns destinations from the multicast view.                    |
| RTM\_VIEW\_MASK\_ALL     | 0xFFFFFFFF | Returns information from all views.                              |



 

 

 




