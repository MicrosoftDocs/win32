---
title: Enumerating Groups (RRAS)
description: The following table summarizes a series of steps in an interaction between a routing protocol and the multicast group manager.
ms.assetid: 30a81946-fa60-4424-9a16-a9b4dfe1961e
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Groups

The following table summarizes a series of steps in an interaction between a routing protocol and the multicast group manager. The first column describes the actions that the routing protocol performs and the routing protocol's responses to the multicast group manager. The second column describes the multicast group manager's responses to the routing protocol. The third column presents any additional information.

Each row of the table represents one step.



| Routing protocol action                                                                                                                                                    | Multicast group manager action                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Obtain a handle to an enumeration using the [**MgmGroupEnumerationStart**](/windows/desktop/api/Mgm/nf-mgm-mgmgroupenumerationstart) function.                                                         | Return a handle.                                                                                                                                                                                                                                                                                             |
| Obtain one or more groups using the [**MgmGroupEnumerationGetNext**](/windows/desktop/api/Mgm/nf-mgm-mgmgroupenumerationgetnext) function.                                                             | Return as many groups as fit in the buffer supplied by the client. If no groups can be returned in the supplied buffer, return ERROR\_INSUFFICIENT\_BUFFER and the size of the buffer that is needed to return one group.<br/> Return ERROR\_NO\_MORE\_ITEMS when there are no more groups.<br/> |
| If ERROR\_INSUFFICIENT\_BUFFER is received, call the [**MgmGroupEnumerationGetNext**](/windows/desktop/api/Mgm/nf-mgm-mgmgroupenumerationgetnext) function again using a buffer of the size indicated. |                                                                                                                                                                                                                                                                                                              |
| Continue calling the [**MgmGroupEnumerationGetNext**](/windows/desktop/api/Mgm/nf-mgm-mgmgroupenumerationgetnext) function until ERROR\_NO\_MORE\_ITEMS is received.                                   |                                                                                                                                                                                                                                                                                                              |
| End the enumeration process using the [**MgmGroupEnumerationEnd**](/windows/desktop/api/Mgm/nf-mgm-mgmgroupenumerationend) function.                                                                   | Destroy the handle.                                                                                                                                                                                                                                                                                          |



 

 

 





