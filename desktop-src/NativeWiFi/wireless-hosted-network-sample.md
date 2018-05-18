---
Description: 'Demonstrates the use of wireless Hosted Network functions.'
ms.assetid: '3da903c2-bdfa-4c1f-92e7-962551f0e08e'
title: Wireless Hosted Network Sample
---

# Wireless Hosted Network Sample

A wireless Hosted Network sample that demonstrates the use of wireless Hosted Network functions is included with the Microsoft Windows Software Development Kit (SDK). The latest version of the Windows SDK is available from the [Download Center](http://go.microsoft.com/fwlink/p/?linkid=102968).

By default, the wireless Hosted Network sample source code is installed in the following directory:

**C:\\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\NetDs\\Wlan**

The wireless Hosted Network sample is located under the following folder:

**WirelessHostedNetwork**

The Wireless Hosted Network sample can be compiled on the Windows SDK for Windows 7. The Wireless Hosted Network sample can be run on Windows 7 and on Windows Server 2008 R2 with the Wireless LAN Service installed.

On Windows 7 and on Windows Server 2008 R2 with the Wireless LAN Service installed, the operating system installs a virtual device if a Hosted Network capable wireless adapter is present on the machine. This virtual device normally shows up in the "Network Connections Folder" as "Wireless Network Connection 2" with a Device Name of "Microsoft Virtual WiFi Miniport adapter" if the computer has a single wireless network adapter. This virtual device is used exclusively for performing software access point (SoftAP) connections. The lifetime of this virtual device is tied to the physical wireless adapter. If the physical wireless adapter is disabled, this virtual device will be removed as well.

The wireless Hosted Network functions are used to start and stop the wireless Hosted Network, configure or change settings, or query for information.

## Related topics

<dl> <dt>

[About the Wireless Hosted Network](about-the-wireless-hosted-network.md)
</dt> <dt>

[Using Hosted Network and Internet Connection Sharing](using-hosted-network-and-internet-connection-sharing.md)
</dt> <dt>

[**WlanHostedNetworkForceStart**](wlanhostednetworkforcestart.md)
</dt> <dt>

[**WlanHostedNetworkInitSettings**](wlanhostednetworkinitsettings.md)
</dt> <dt>

[**WlanHostedNetworkQueryProperty**](wlanhostednetworkqueryproperty.md)
</dt> <dt>

[**WlanHostedNetworkQuerySecondaryKey**](wlanhostednetworkquerysecondarykey.md)
</dt> <dt>

[**WlanHostedNetworkQueryStatus**](wlanhostednetworkquerystatus.md)
</dt> <dt>

[**WlanHostedNetworkRefreshSecuritySettings**](wlanhostednetworkrefreshsecuritysettings.md)
</dt> <dt>

[**WlanHostedNetworkSetProperty**](wlanhostednetworksetproperty.md)
</dt> <dt>

[**WlanHostedNetworkSetSecondaryKey**](wlanhostednetworksetsecondarykey.md)
</dt> <dt>

[**WlanHostedNetworkStartUsing**](wlanhostednetworkstartusing.md)
</dt> <dt>

[**WlanHostedNetworkStopUsing**](wlanhostednetworkstopusing.md)
</dt> <dt>

[**WlanRegisterVirtualStationNotification**](wlanregistervirtualstationnotification.md)
</dt> </dl>

 

 



