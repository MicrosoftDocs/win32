---
description: The wireless ad hoc programming interface is composed of the following interfaces.
ms.assetid: 8e975750-cfcc-4e36-a3d1-539b7c077459
title: Wireless Ad Hoc Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Wireless Ad Hoc Interfaces

The wireless ad hoc programming interface is composed of the following interfaces.



| Interface Name                                                                       | Description                                                                                            |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**IDot11AdHocInterface**](/windows/desktop/api/adhoc/nn-adhoc-idot11adhocinterface)                                 | Represents a wireless network interface card (NIC).                                                    |
| [**IDot11AdHocInterfaceNotificationSink**](/windows/desktop/api/adhoc/nn-adhoc-idot11adhocinterfacenotificationsink) | Defines the notifications supported by [**IDot11AdHocInterface**](/windows/desktop/api/adhoc/nn-adhoc-idot11adhocinterface).           |
| [**IDot11AdHocManager**](/windows/desktop/api/adhoc/nn-adhoc-idot11adhocmanager)                                     | Creates and manages 802.11 ad hoc networks.                                                            |
| [**IDot11AdHocManagerNotificationSink**](/windows/desktop/api/adhoc/nn-adhoc-idot11adhocmanagernotificationsink)     | Defines the notifications supported by the [**IDot11AdHocManager**](/windows/desktop/api/adhoc/nn-adhoc-idot11adhocmanager) interface. |
| [**IDot11AdHocNetwork**](/windows/desktop/api/adhoc/nn-adhoc-idot11adhocnetwork)                                     | Represents an available ad hoc network destination within connection range.                            |
| [**IDot11AdHocNetworkNotificationSink**](/windows/desktop/api/adhoc/nn-adhoc-idot11adhocnetworknotificationsink)     | Defines the notifications supported by the [**IDot11AdHocNetwork**](/windows/desktop/api/adhoc/nn-adhoc-idot11adhocnetwork) interface. |
| [**IDot11AdHocSecuritySettings**](/windows/desktop/api/adhoc/nn-adhoc-idot11adhocsecuritysettings)                   | Specifies the security settings for a wireless ad hoc network.                                         |
| [**IEnumDot11AdHocInterfaces**](/windows/desktop/api/adhoc/nn-adhoc-ienumdot11adhocinterfaces)                       | Represents the collection of currently visible 802.11 ad hoc network interfaces.                       |
| [**IEnumDot11AdHocNetworks**](/windows/desktop/api/adhoc/nn-adhoc-ienumdot11adhocnetworks)                           | Represents the collection of currently visible 802.11 ad hoc networks.                                 |
| [**IEnumDot11AdHocSecuritySettings**](/windows/desktop/api/adhoc/nn-adhoc-ienumdot11adhocsecuritysettings)           | Represents the collection of security settings associated with each visible wireless ad hoc network.   |



 

> [!Note]  
> Ad hoc mode might not be available in future versions of Windows. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](about-the-wi-fi-direct-api.md) instead.

 

 

 



