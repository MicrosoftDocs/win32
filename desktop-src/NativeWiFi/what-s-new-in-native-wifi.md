---
Description: 'What''s New in Native Wifi'
ms.assetid: '76d60b95-a34a-4747-b0fa-9230aa60bd63'
title: 'What''s New in Native Wifi'
---

# What's New in Native Wifi

## Windows 10

Support for Hotspot 2.0 has been added to the [WLAN\_profile schema](wlan-profileschema-schema.md). Hotspot 2.0 enables automatic connection to public Wi-Fi services using existing credentials and membership in service provider networks. Service providers specify how connections are made using the new schema elements to describe which networks to use, and how to authenticate to them. See the [**Hotspot2**](wlan-profileschema-hotspot2-element.md) element documentation for details.

## Windows 8 and Windows Server 2012

The following features have been added to the Native Wifi APIs on Windows 8 and Windows Server 2012.

A Wi-Fi Direct feature based on the development of the Wi-Fi Peer-to-Peer Technical Specification v1.1 by the Wi-Fi Alliance (see [Wi-Fi Alliance Published Specifications](http://go.microsoft.com/fwlink/p/?linkid=253656)). The goal of the Wi-Fi Peer-to-Peer Technical Specification is to provide a solution for Wi-Fi device-to-device connectivity without the need for either a Wireless Access Point (wireless AP) to setup the connection or the use of the existing Wi-Fi adhoc (IBSS) mechanism.

The following functions support the Wi-Fi Direct feature.

-   [**WFD\_OPEN\_SESSION\_COMPLETE\_CALLBACK**](wfd-open-session-complete-callback.md)
-   [**WFDCancelOpenSession**](wfdcancelopensession.md)
-   [**WFDCloseHandle**](wfdclosehandle.md)
-   [**WFDCloseSession**](wfdclosesession.md)
-   [**WFDOpenHandle**](wfdopenhandle.md)
-   [**WFDOpenLegacySession**](wfdopenlegacysession.md)
-   [**WFDStartOpenSession**](wfdstartopensession.md)
-   [**WFDUpdateDeviceVisibility**](wfdupdatedevicevisibility.md)

## Windows 7 and Windows Server 2008 R2

The following features have been added to the Native Wifi APIs on Windows 7 and Windows Server 2008 R2.

The wireless Hosted Network allows a single physical wireless adapter to connect as a client to a hardware access point (AP), while at the same time acting as a software AP allowing other wireless-capable devices to connect to it.

The following functions support the wireless Hosted Network feature.

-   [**WlanHostedNetworkForceStart**](wlanhostednetworkforcestart.md)
-   [**WlanHostedNetworkForceStop**](wlanhostednetworkforcestop.md)
-   [**WlanHostedNetworkInitSettings**](wlanhostednetworkinitsettings.md)
-   [**WlanHostedNetworkQueryProperty**](wlanhostednetworkqueryproperty.md)
-   [**WlanHostedNetworkQuerySecondaryKey**](wlanhostednetworkquerysecondarykey.md)
-   [**WlanHostedNetworkQueryStatus**](wlanhostednetworkquerystatus.md)
-   [**WlanHostedNetworkRefreshSecuritySettings**](wlanhostednetworkrefreshsecuritysettings.md)
-   [**WlanHostedNetworkSetProperty**](wlanhostednetworksetproperty.md)
-   [**WlanHostedNetworkSetSecondaryKey**](wlanhostednetworksetsecondarykey.md)
-   [**WlanHostedNetworkStartUsing**](wlanhostednetworkstartusing.md)
-   [**WlanHostedNetworkStopUsing**](wlanhostednetworkstopusing.md)
-   [**WlanRegisterVirtualStationNotification**](wlanregistervirtualstationnotification.md)

The following new structures that work with wireless Hosted Network.

-   [**WLAN\_HOSTED\_NETWORK\_CONNECTION\_SETTINGS**](wlan-hosted-network-connection-settings.md)
-   [**WLAN\_HOSTED\_NETWORK\_DATA\_PEER\_STATE\_CHANGE**](wlan-hosted-network-data-peer-state-change.md)
-   [**WLAN\_HOSTED\_NETWORK\_PEER\_STATE**](wlan-hosted-network-peer-state.md)
-   [**WLAN\_HOSTED\_NETWORK\_RADIO\_STATE**](wlan-hosted-network-radio-state.md)
-   [**WLAN\_HOSTED\_NETWORK\_SECURITY\_SETTINGS**](wlan-hosted-network-security-settings.md)
-   [**WLAN\_HOSTED\_NETWORK\_STATE\_CHANGE**](wlan-hosted-network-state-change.md)
-   [**WLAN\_HOSTED\_NETWORK\_STATUS**](wlan-hosted-network-status.md)

The following new enumerations that work with wireless Hosted Network.

-   [**WLAN\_HOSTED\_NETWORK\_NOTIFICATION\_CODE**](wlan-hosted-network-notification-code.md)
-   [**WLAN\_HOSTED\_NETWORK\_OPCODE**](wlan-hosted-network-opcode.md)
-   [**WLAN\_HOSTED\_NETWORK\_PEER\_AUTH\_STATE**](wlan-hosted-network-peer-auth-state.md)
-   [**WLAN\_HOSTED\_NETWORK\_REASON**](wlan-hosted-network-reason.md)
-   [**WLAN\_HOSTED\_NETWORK\_STATE**](wlan-hosted-network-state.md)

## Related topics

<dl> <dt>

[About the Wireless Hosted Network](about-the-wireless-hosted-network.md)
</dt> <dt>

[Using Wireless Hosted Network and Internet Connection Sharing](using-hosted-network-and-internet-connection-sharing.md)
</dt> </dl>

 

 



