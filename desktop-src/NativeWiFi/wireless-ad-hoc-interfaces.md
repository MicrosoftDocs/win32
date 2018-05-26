---
Description: The wireless ad hoc programming interface is composed of the following interfaces.
ms.assetid: 8e975750-cfcc-4e36-a3d1-539b7c077459
title: Wireless Ad Hoc Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Wireless Ad Hoc Interfaces

The wireless ad hoc programming interface is composed of the following interfaces.



| Interface Name                                                                       | Description                                                                                            |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**IDot11AdHocInterface**](/windows/win32/adhoc/nn-adhoc-idot11adhocinterface?branch=master)                                 | Represents a wireless network interface card (NIC).                                                    |
| [**IDot11AdHocInterfaceNotificationSink**](/windows/win32/adhoc/nn-adhoc-idot11adhocinterfacenotificationsink?branch=master) | Defines the notifications supported by [**IDot11AdHocInterface**](/windows/win32/adhoc/nn-adhoc-idot11adhocinterface?branch=master).           |
| [**IDot11AdHocManager**](/windows/win32/adhoc/nn-adhoc-idot11adhocmanager?branch=master)                                     | Creates and manages 802.11 ad hoc networks.                                                            |
| [**IDot11AdHocManagerNotificationSink**](/windows/win32/adhoc/nn-adhoc-idot11adhocmanagernotificationsink?branch=master)     | Defines the notifications supported by the [**IDot11AdHocManager**](/windows/win32/adhoc/nn-adhoc-idot11adhocmanager?branch=master) interface. |
| [**IDot11AdHocNetwork**](/windows/win32/adhoc/nn-adhoc-idot11adhocnetwork?branch=master)                                     | Represents an available ad hoc network destination within connection range.                            |
| [**IDot11AdHocNetworkNotificationSink**](/windows/win32/adhoc/nn-adhoc-idot11adhocnetworknotificationsink?branch=master)     | Defines the notifications supported by the [**IDot11AdHocNetwork**](/windows/win32/adhoc/nn-adhoc-idot11adhocnetwork?branch=master) interface. |
| [**IDot11AdHocSecuritySettings**](/windows/win32/adhoc/nn-adhoc-idot11adhocsecuritysettings?branch=master)                   | Specifies the security settings for a wireless ad hoc network.                                         |
| [**IEnumDot11AdHocInterfaces**](/windows/win32/adhoc/nn-adhoc-ienumdot11adhocinterfaces?branch=master)                       | Represents the collection of currently visible 802.11 ad hoc network interfaces.                       |
| [**IEnumDot11AdHocNetworks**](/windows/win32/adhoc/nn-adhoc-ienumdot11adhocnetworks?branch=master)                           | Represents the collection of currently visible 802.11 ad hoc networks.                                 |
| [**IEnumDot11AdHocSecuritySettings**](/windows/win32/adhoc/nn-adhoc-ienumdot11adhocsecuritysettings?branch=master)           | Represents the collection of security settings associated with each visible wireless ad hoc network.   |



 

> [!Note]  
> Ad hoc mode might not be available in future versions of Windows. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](about-the-wi-fi-direct-api.md) instead.

 

 

 



