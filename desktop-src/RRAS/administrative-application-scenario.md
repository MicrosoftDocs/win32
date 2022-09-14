---
title: Administrative Application Scenario
description: Administrative applications call a subset of MGM functions that are related to enumerating multicast forwarding entries (MFEs) and MFE statistics.
ms.assetid: ed172425-6d1e-45d8-8076-7705e833bfd5
ms.topic: article
ms.date: 05/31/2018
---

# Administrative Application Scenario

Administrative applications call a subset of MGM functions that are related to enumerating multicast forwarding entries (MFEs) and MFE statistics. An application does not need to register with the multicast group manager to use these functions (that is, the application does not need a handle).

## Enumerating MFEs

The following table summarizes a series of steps in an interactions between an administrative application and the multicast group manager. The first column describes the actions that the administrative application performs and the administrative application's responses to the multicast group manager. The second column describes the multicast group manager's responses to the administrative application. The third column presents any additional information.

Each row of the table represents one step.



| Administrative application action                                                                                                                                                                                      | Multicast group manager action                                                                                                                                                                                                                                                              | Notes                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Obtain one or more MFEs using the [**MgmGetFirstMfe**](/windows/desktop/api/Mgm/nf-mgm-mgmgetfirstmfe) function.                                                                                                                                   | Return as many MFEs as fit in the buffer supplied by the client. If no MFEs can be returned in the supplied buffer, return ERROR\_INSUFFICIENT\_BUFFER and the size of the buffer that is needed to return one MFE.<br/>                                                              | Clients can also retrieve MFE statistics using the corresponding statistics functions, [**MgmGetFirstMfeStats**](/windows/desktop/api/Mgm/nf-mgm-mgmgetfirstmfestats) and [**MgmGetNextMfeStats**](/windows/desktop/api/Mgm/nf-mgm-mgmgetnextmfestats). |
| If ERROR\_INSUFFICIENT\_BUFFER is received, call the [**MgmGetFirstMfe**](/windows/desktop/api/Mgm/nf-mgm-mgmgetfirstmfe) function again using a buffer of the size indicated.                                                                     |                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                 |
| Continue calling the [**MgmGetNextMfe**](/windows/desktop/api/Mgm/nf-mgm-mgmgetnextmfe) function, supplying as one of the parameters the last MFE that was returned by the previous call to the [**MgmGetFirstMfe**](/windows/desktop/api/Mgm/nf-mgm-mgmgetfirstmfe) function. | Return as many MFEs as fit in the buffer supplied by the client. If no MFEs can be returned in the supplied buffer, return ERROR\_INSUFFICIENT\_BUFFER and the size of the buffer that is needed for one MFE.<br/> Return ERROR\_NO\_MORE\_ITEMS when no more MFEs remain.<br/> |                                                                                                                                                                                                 |
| Continue the enumeration until ERROR\_NO\_MORE\_ITEMS is received.                                                                                                                                                     |                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                 |



 

> [!Note]  
> Use the [**MgmGetMfe**](/windows/desktop/api/Mgm/nf-mgm-mgmgetmfe) and [**MgmGetMfeStats**](/windows/desktop/api/Mgm/nf-mgm-mgmgetmfestats) functions to retrieve a specific MFE or specific set of MFE statistics.

 

 

 





