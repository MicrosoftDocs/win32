---
title: On Demand Connection Routing Helper API reference
description: The following topics provide details for the On Demand Connection Routing Helper.
ms.assetid: 39AFFD16-488E-4CA3-9161-9424F0D15948
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# On Demand Connection Routing Helper API reference

The following topics provide details for the On Demand Connection Routing Helper.



| Reference                                                                          | Description                                                                                                                                                                 |
|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**OnDemandGetRoutingHint**](/windows/win32/OnDemandConnRouteHelper/nf-ondemandconnroutehelper-ondemandgetroutinghint?branch=master)                           | Look up a destination in the Route Request cache and, if a match is found, returns the corresponding Interface ID.<br/>                                               |
| [**OnDemandRegisterNotification**](/windows/win32/OnDemandConnRouteHelper/nf-ondemandconnroutehelper-ondemandregisternotification?branch=master)               | Register to be notified when the Route Requests cache is modified.<br/>                                                                                               |
| [**OnDemandUnregisterNotification**](/windows/win32/OnDemandConnRouteHelper/nf-ondemandconnroutehelper-ondemandunregisternotification?branch=master)           | Unregister for notifications and clean up resources.<br/>                                                                                                             |
| [**NET\_INTERFACE\_CONTEXT**](/windows/win32/OnDemandConnRouteHelper/ns-ondemandconnroutehelper-_net_interface_context?branch=master)                           | The interface context that is part of the [**NET\_INTERFACE\_CONTEXT\_TABLE**](/windows/win32/OnDemandConnRouteHelper/ns-ondemandconnroutehelper-_net_interface_context_table?branch=master) structure.<br/>                                       |
| [**NET\_INTERFACE\_CONTEXT\_TABLE**](/windows/win32/OnDemandConnRouteHelper/ns-ondemandconnroutehelper-_net_interface_context_table?branch=master)              | The table of [**NET\_INTERFACE\_CONTEXT**](/windows/win32/OnDemandConnRouteHelper/ns-ondemandconnroutehelper-_net_interface_context?branch=master) structures.<br/>                                                                                |
| [**GetInterfaceContextTableForHostName**](/windows/win32/OnDemandConnRouteHelper/nf-ondemandconnroutehelper-getinterfacecontexttableforhostname?branch=master) | This function retrieves an interface context table for the given hostname and connection profile filter.<br/>                                                         |
| [**FreeInterfaceContextTable**](/windows/win32/OnDemandConnRouteHelper/nf-ondemandconnroutehelper-freeinterfacecontexttable?branch=master)                     | This function frees the interface context table retrieved using the [**GetInterfaceContextTableForHostName**](/windows/win32/OnDemandConnRouteHelper/nf-ondemandconnroutehelper-getinterfacecontexttableforhostname?branch=master) function.<br/> |



 

 

 





