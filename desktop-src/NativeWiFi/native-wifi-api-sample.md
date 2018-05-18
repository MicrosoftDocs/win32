---
Description: 'Demonstrates the use of basic wireless network management functions.'
ms.assetid: '63af0b88-c20b-4b06-9db3-e8510fc80053'
title: Native Wifi API Sample
---

# Native Wifi API Sample

A Native Wifi API sample that demonstrates the use of basic wireless network management functions is included with the Microsoft Windows Software Development Kit (SDK). The latest version of the Windows SDK is available from the [Download Center](http://go.microsoft.com/fwlink/p/?linkid=102968).

By default, the Native Wifi sample source code is installed in the following directory:

**C:\\Program Files\\Microsoft SDKs\\Windows\\&lt;version number&gt;\\Samples\\NetDs\\Wlan**

The Native Wifi API sample is located under the following folder:

**autoconfig**

The Native Wifi sample can be compiled and run on Windows Vista and later, Windows XP with Service Pack 3 (SP3), and Wireless LAN API for Windows XP with Service Pack 2 (SP2). Some features of the sample are not supported on Windows XP with SP3 and Wireless LAN API for Windows XP with SP2. For a list of functions supported by Windows XP with SP3 and Wireless LAN API for Windows XP with SP2, see [Native Wifi API Support on Windows XP](about-wireless-lan-api-for-windows-xp-service-pack-2.md).

The Native Wifi sample demonstrates how to perform the following tasks:

-   Enumerate wireless interfaces. See [**WlanEnumInterfaces**](wlanenuminterfaces.md).
-   Get the capabilities of an interface. See [**WlanGetInterfaceCapability**](wlangetinterfacecapability.md).

    **Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:  ** This feature is not supported.

-   Query an interface. See [**WlanQueryInterface**](wlanqueryinterface.md).
-   Set parameters for a network interface. See [**WlanSetInterface**](wlansetinterface.md). This function can be used to turn the wireless radio on and off (and therefore enable or disable wireless network connectivity).
-   Scan for available wireless networks. See [**WlanScan**](wlanscan.md).
-   Get the list of available or visible wireless networks. See [**WlanGetAvailableNetworkList**](wlangetavailablenetworklist.md).
-   Get, save, or delete a profile. See [**WlanGetProfile**](wlangetprofile.md), [**WlanSetProfile**](wlansetprofile.md), and [**WlanDeleteProfile**](wlandeleteprofile.md).
-   Connect to or disconnect from a wireless network. See [**WlanConnect**](wlanconnect.md) and [**WlanDisconnect**](wlandisconnect.md).

## Related topics

<dl> <dt>

[Using Native Wifi](using-native-wifi.md)
</dt> <dt>

[Windows Vista Wireless SDK Forum](http://go.microsoft.com/fwlink/p/?linkid=313706)
</dt> <dt>

[Troubleshooting Windows Vista 802.11 Wireless Connections](http://go.microsoft.com/fwlink/p/?linkid=93832)
</dt> </dl>

 

 



