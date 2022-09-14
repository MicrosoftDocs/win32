---
description: What's New in Native Wifi
ms.assetid: 76d60b95-a34a-4747-b0fa-9230aa60bd63
title: What's New in Native Wifi
ms.topic: article
ms.date: 05/31/2018
---

# What's New in Native Wifi

## Windows 10, version 2004

See [Provision a Wi-Fi profile via a website](prov-wifi-profile-via-website.md).

## Windows 10

Support for Hotspot 2.0 has been added to the [WLAN\_profile schema](wlan-profileschema-schema.md). Hotspot 2.0 enables automatic connection to public Wi-Fi services using existing credentials and membership in service provider networks. Service providers specify how connections are made using the new schema elements to describe which networks to use, and how to authenticate to them. See the [**Hotspot2**](wlan-profileschema-hotspot2-element.md) element documentation for details.

## Windows 8 and Windows Server 2012

The following features have been added to the Native Wifi APIs on Windows 8 and Windows Server 2012.

A Wi-Fi Direct feature based on the development of the Wi-Fi Peer-to-Peer Technical Specification v1.1 by the Wi-Fi Alliance (see [Wi-Fi Alliance Published Specifications](https://www.wi-fi.org/)). The goal of the Wi-Fi Peer-to-Peer Technical Specification is to provide a solution for Wi-Fi device-to-device connectivity without the need for either a Wireless Access Point (wireless AP) to setup the connection or the use of the existing Wi-Fi adhoc (IBSS) mechanism.

The following functions support the Wi-Fi Direct feature.

-   [**WFD\_OPEN\_SESSION\_COMPLETE\_CALLBACK**](/windows/desktop/api/wlanapi/nc-wlanapi-wfd_open_session_complete_callback)
-   [**WFDCancelOpenSession**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdcancelopensession)
-   [**WFDCloseHandle**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdclosehandle)
-   [**WFDCloseSession**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdclosesession)
-   [**WFDOpenHandle**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdopenhandle)
-   [**WFDOpenLegacySession**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdopenlegacysession)
-   [**WFDStartOpenSession**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdstartopensession)
-   [**WFDUpdateDeviceVisibility**](/windows/desktop/api/wlanapi/nf-wlanapi-wfdupdatedevicevisibility)

## Windows 7 and Windows Server 2008 R2

The following features have been added to the Native Wifi APIs on Windows 7 and Windows Server 2008 R2.

The wireless Hosted Network allows a single physical wireless adapter to connect as a client to a hardware access point (AP), while at the same time acting as a software AP allowing other wireless-capable devices to connect to it.

The following functions support the wireless Hosted Network feature.

-   [**WlanHostedNetworkForceStart**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkforcestart)
-   [**WlanHostedNetworkForceStop**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkforcestop)
-   [**WlanHostedNetworkInitSettings**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkinitsettings)
-   [**WlanHostedNetworkQueryProperty**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkqueryproperty)
-   [**WlanHostedNetworkQuerySecondaryKey**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkquerysecondarykey)
-   [**WlanHostedNetworkQueryStatus**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkquerystatus)
-   [**WlanHostedNetworkRefreshSecuritySettings**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkrefreshsecuritysettings)
-   [**WlanHostedNetworkSetProperty**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworksetproperty)
-   [**WlanHostedNetworkSetSecondaryKey**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworksetsecondarykey)
-   [**WlanHostedNetworkStartUsing**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkstartusing)
-   [**WlanHostedNetworkStopUsing**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkstopusing)
-   [**WlanRegisterVirtualStationNotification**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanregistervirtualstationnotification)

The following new structures that work with wireless Hosted Network.

-   [**WLAN\_HOSTED\_NETWORK\_CONNECTION\_SETTINGS**](/windows/desktop/api/Wlanapi/ns-wlanapi-wlan_hosted_network_connection_settings)
-   [**WLAN\_HOSTED\_NETWORK\_DATA\_PEER\_STATE\_CHANGE**](/windows/desktop/api/Wlanapi/ns-wlanapi-wlan_hosted_network_data_peer_state_change)
-   [**WLAN\_HOSTED\_NETWORK\_PEER\_STATE**](/windows/desktop/api/Wlanapi/ns-wlanapi-wlan_hosted_network_peer_state)
-   [**WLAN\_HOSTED\_NETWORK\_RADIO\_STATE**](/windows/desktop/api/Wlanapi/ns-wlanapi-wlan_hosted_network_radio_state)
-   [**WLAN\_HOSTED\_NETWORK\_SECURITY\_SETTINGS**](/windows/desktop/api/Wlanapi/ns-wlanapi-wlan_hosted_network_security_settings)
-   [**WLAN\_HOSTED\_NETWORK\_STATE\_CHANGE**](/windows/desktop/api/Wlanapi/ns-wlanapi-wlan_hosted_network_state_change)
-   [**WLAN\_HOSTED\_NETWORK\_STATUS**](/windows/desktop/api/Wlanapi/ns-wlanapi-wlan_hosted_network_status)

The following new enumerations that work with wireless Hosted Network.

-   [**WLAN\_HOSTED\_NETWORK\_NOTIFICATION\_CODE**](/windows/desktop/api/Wlanapi/ne-wlanapi-wlan_hosted_network_notification_code)
-   [**WLAN\_HOSTED\_NETWORK\_OPCODE**](/windows/desktop/api/Wlanapi/ne-wlanapi-wlan_hosted_network_opcode)
-   [**WLAN\_HOSTED\_NETWORK\_PEER\_AUTH\_STATE**](/windows/desktop/api/Wlanapi/ne-wlanapi-wlan_hosted_network_peer_auth_state)
-   [**WLAN\_HOSTED\_NETWORK\_REASON**](/windows/desktop/api/Wlanapi/ne-wlanapi-wlan_hosted_network_reason)
-   [**WLAN\_HOSTED\_NETWORK\_STATE**](/windows/desktop/api/Wlanapi/ne-wlanapi-wlan_hosted_network_state)

## Related topics

<dl> <dt>

[About the Wireless Hosted Network](about-the-wireless-hosted-network.md)
</dt> <dt>

[Using Wireless Hosted Network and Internet Connection Sharing](using-hosted-network-and-internet-connection-sharing.md)
</dt> </dl>

 

 



