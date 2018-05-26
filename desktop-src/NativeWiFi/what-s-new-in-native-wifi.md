---
Description: Whats New in Native Wifi
ms.assetid: 76d60b95-a34a-4747-b0fa-9230aa60bd63
title: Whats New in Native Wifi
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# What's New in Native Wifi

## Windows 10

Support for Hotspot 2.0 has been added to the [WLAN\_profile schema](wlan-profileschema-schema.md). Hotspot 2.0 enables automatic connection to public Wi-Fi services using existing credentials and membership in service provider networks. Service providers specify how connections are made using the new schema elements to describe which networks to use, and how to authenticate to them. See the [**Hotspot2**](wlan-profileschema-hotspot2-element.md) element documentation for details.

## Windows 8 and Windows Server 2012

The following features have been added to the Native Wifi APIs on Windows 8 and Windows Server 2012.

A Wi-Fi Direct feature based on the development of the Wi-Fi Peer-to-Peer Technical Specification v1.1 by the Wi-Fi Alliance (see [Wi-Fi Alliance Published Specifications](http://go.microsoft.com/fwlink/p/?linkid=253656)). The goal of the Wi-Fi Peer-to-Peer Technical Specification is to provide a solution for Wi-Fi device-to-device connectivity without the need for either a Wireless Access Point (wireless AP) to setup the connection or the use of the existing Wi-Fi adhoc (IBSS) mechanism.

The following functions support the Wi-Fi Direct feature.

-   [**WFD\_OPEN\_SESSION\_COMPLETE\_CALLBACK**](/windows/win32/wlanapi/nc-wlanapi-wfd_open_session_complete_callback?branch=master)
-   [**WFDCancelOpenSession**](/windows/win32/wlanapi/nf-wlanapi-wfdcancelopensession?branch=master)
-   [**WFDCloseHandle**](/windows/win32/wlanapi/nf-wlanapi-wfdclosehandle?branch=master)
-   [**WFDCloseSession**](/windows/win32/wlanapi/nf-wlanapi-wfdclosesession?branch=master)
-   [**WFDOpenHandle**](/windows/win32/wlanapi/nf-wlanapi-wfdopenhandle?branch=master)
-   [**WFDOpenLegacySession**](/windows/win32/wlanapi/nf-wlanapi-wfdopenlegacysession?branch=master)
-   [**WFDStartOpenSession**](/windows/win32/wlanapi/nf-wlanapi-wfdstartopensession?branch=master)
-   [**WFDUpdateDeviceVisibility**](/windows/win32/wlanapi/nf-wlanapi-wfdupdatedevicevisibility?branch=master)

## Windows 7 and Windows Server 2008 R2

The following features have been added to the Native Wifi APIs on Windows 7 and Windows Server 2008 R2.

The wireless Hosted Network allows a single physical wireless adapter to connect as a client to a hardware access point (AP), while at the same time acting as a software AP allowing other wireless-capable devices to connect to it.

The following functions support the wireless Hosted Network feature.

-   [**WlanHostedNetworkForceStart**](/windows/win32/Wlanapi/nf-wlanapi-wlanhostednetworkforcestart?branch=master)
-   [**WlanHostedNetworkForceStop**](/windows/win32/Wlanapi/nf-wlanapi-wlanhostednetworkforcestop?branch=master)
-   [**WlanHostedNetworkInitSettings**](/windows/win32/Wlanapi/nf-wlanapi-wlanhostednetworkinitsettings?branch=master)
-   [**WlanHostedNetworkQueryProperty**](/windows/win32/Wlanapi/nf-wlanapi-wlanhostednetworkqueryproperty?branch=master)
-   [**WlanHostedNetworkQuerySecondaryKey**](/windows/win32/Wlanapi/nf-wlanapi-wlanhostednetworkquerysecondarykey?branch=master)
-   [**WlanHostedNetworkQueryStatus**](/windows/win32/Wlanapi/nf-wlanapi-wlanhostednetworkquerystatus?branch=master)
-   [**WlanHostedNetworkRefreshSecuritySettings**](/windows/win32/Wlanapi/nf-wlanapi-wlanhostednetworkrefreshsecuritysettings?branch=master)
-   [**WlanHostedNetworkSetProperty**](/windows/win32/Wlanapi/nf-wlanapi-wlanhostednetworksetproperty?branch=master)
-   [**WlanHostedNetworkSetSecondaryKey**](/windows/win32/Wlanapi/nf-wlanapi-wlanhostednetworksetsecondarykey?branch=master)
-   [**WlanHostedNetworkStartUsing**](/windows/win32/Wlanapi/nf-wlanapi-wlanhostednetworkstartusing?branch=master)
-   [**WlanHostedNetworkStopUsing**](/windows/win32/Wlanapi/nf-wlanapi-wlanhostednetworkstopusing?branch=master)
-   [**WlanRegisterVirtualStationNotification**](/windows/win32/Wlanapi/nf-wlanapi-wlanregistervirtualstationnotification?branch=master)

The following new structures that work with wireless Hosted Network.

-   [**WLAN\_HOSTED\_NETWORK\_CONNECTION\_SETTINGS**](/windows/win32/Wlanapi/ns-wlanapi-_wlan_hosted_network_connection_settings?branch=master)
-   [**WLAN\_HOSTED\_NETWORK\_DATA\_PEER\_STATE\_CHANGE**](/windows/win32/Wlanapi/ns-wlanapi-_wlan_hosted_network_data_peer_state_change?branch=master)
-   [**WLAN\_HOSTED\_NETWORK\_PEER\_STATE**](/windows/win32/Wlanapi/ns-wlanapi-_wlan_hosted_network_peer_state?branch=master)
-   [**WLAN\_HOSTED\_NETWORK\_RADIO\_STATE**](/windows/win32/Wlanapi/ns-wlanapi-_wlan_hosted_network_radio_state?branch=master)
-   [**WLAN\_HOSTED\_NETWORK\_SECURITY\_SETTINGS**](/windows/win32/Wlanapi/ns-wlanapi-_wlan_hosted_network_security_settings?branch=master)
-   [**WLAN\_HOSTED\_NETWORK\_STATE\_CHANGE**](/windows/win32/Wlanapi/ns-wlanapi-_wlan_hosted_network_state_change?branch=master)
-   [**WLAN\_HOSTED\_NETWORK\_STATUS**](/windows/win32/Wlanapi/ns-wlanapi-_wlan_hosted_network_status?branch=master)

The following new enumerations that work with wireless Hosted Network.

-   [**WLAN\_HOSTED\_NETWORK\_NOTIFICATION\_CODE**](/windows/win32/Wlanapi/ne-wlanapi-_wlan_hosted_network_notification_code?branch=master)
-   [**WLAN\_HOSTED\_NETWORK\_OPCODE**](/windows/win32/Wlanapi/ne-wlanapi-_wlan_hosted_network_opcode?branch=master)
-   [**WLAN\_HOSTED\_NETWORK\_PEER\_AUTH\_STATE**](/windows/win32/Wlanapi/ne-wlanapi-_wlan_hosted_network_peer_auth_state?branch=master)
-   [**WLAN\_HOSTED\_NETWORK\_REASON**](/windows/win32/Wlanapi/ne-wlanapi-_wlan_hosted_network_reason?branch=master)
-   [**WLAN\_HOSTED\_NETWORK\_STATE**](/windows/win32/Wlanapi/ne-wlanapi-_wlan_hosted_network_state?branch=master)

## Related topics

<dl> <dt>

[About the Wireless Hosted Network](about-the-wireless-hosted-network.md)
</dt> <dt>

[Using Wireless Hosted Network and Internet Connection Sharing](using-hosted-network-and-internet-connection-sharing.md)
</dt> </dl>

 

 



