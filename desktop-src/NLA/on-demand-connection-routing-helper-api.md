---
title: On Demand Connection Routing Helper API reference
description: The following topics provide details for the On Demand Connection Routing Helper.
ms.assetid: 39AFFD16-488E-4CA3-9161-9424F0D15948
ms.topic: article
ms.date: 05/31/2018
---

# On Demand Connection Routing Helper API reference

The following topics provide details for the On Demand Connection Routing Helper.



| Reference                                                                          | Description                                                                                                                                                                 |
|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**OnDemandGetRoutingHint**](/windows/desktop/api/OnDemandConnRouteHelper/nf-ondemandconnroutehelper-ondemandgetroutinghint)                           | Look up a destination in the Route Request cache and, if a match is found, returns the corresponding Interface ID.<br/>                                               |
| [**OnDemandRegisterNotification**](/windows/desktop/api/OnDemandConnRouteHelper/nf-ondemandconnroutehelper-ondemandregisternotification)               | Register to be notified when the Route Requests cache is modified.<br/>                                                                                               |
| [**OnDemandUnregisterNotification**](/windows/desktop/api/OnDemandConnRouteHelper/nf-ondemandconnroutehelper-ondemandunregisternotification)           | Unregister for notifications and clean up resources.<br/>                                                                                                             |
| [**NET\_INTERFACE\_CONTEXT**](/windows/desktop/api/OnDemandConnRouteHelper/ns-ondemandconnroutehelper-net_interface_context)                           | The interface context that is part of the [**NET\_INTERFACE\_CONTEXT\_TABLE**](/windows/desktop/api/OnDemandConnRouteHelper/ns-ondemandconnroutehelper-net_interface_context_table) structure.<br/>                                       |
| [**NET\_INTERFACE\_CONTEXT\_TABLE**](/windows/desktop/api/OnDemandConnRouteHelper/ns-ondemandconnroutehelper-net_interface_context_table)              | The table of [**NET\_INTERFACE\_CONTEXT**](/windows/desktop/api/OnDemandConnRouteHelper/ns-ondemandconnroutehelper-net_interface_context) structures.<br/>                                                                                |
| [**GetInterfaceContextTableForHostName**](/windows/desktop/api/OnDemandConnRouteHelper/nf-ondemandconnroutehelper-getinterfacecontexttableforhostname) | This function retrieves an interface context table for the given hostname and connection profile filter.<br/>                                                         |
| [**FreeInterfaceContextTable**](/windows/desktop/api/OnDemandConnRouteHelper/nf-ondemandconnroutehelper-freeinterfacecontexttable)                     | This function frees the interface context table retrieved using the [**GetInterfaceContextTableForHostName**](/windows/desktop/api/OnDemandConnRouteHelper/nf-ondemandconnroutehelper-getinterfacecontexttableforhostname) function.<br/> |



 

 

 





