---
description: Demonstrates the use of basic wireless network management functions.
ms.assetid: 63af0b88-c20b-4b06-9db3-e8510fc80053
title: Native Wifi API Sample
ms.topic: article
ms.date: 05/31/2018
---

# Native Wifi API Sample

A Native Wifi API sample that demonstrates the use of basic wireless network management functions is included with the Microsoft Windows Software Development Kit (SDK). The latest version of the Windows SDK is available from the [Download Center](https://developer.microsoft.com/windows/downloads).

By default, the Native Wifi sample source code is installed in the following directory:

**C:\\Program Files\\Microsoft SDKs\\Windows\\<version number>\\Samples\\NetDs\\Wlan**

The Native Wifi API sample is located under the following folder:

**autoconfig**

The Native Wifi sample can be compiled and run on Windows Vista and later, Windows XP with Service Pack 3 (SP3), and Wireless LAN API for Windows XP with Service Pack 2 (SP2). Some features of the sample are not supported on Windows XP with SP3 and Wireless LAN API for Windows XP with SP2. For a list of functions supported by Windows XP with SP3 and Wireless LAN API for Windows XP with SP2, see [Native Wifi API Support on Windows XP](about-wireless-lan-api-for-windows-xp-service-pack-2.md).

The Native Wifi sample demonstrates how to perform the following tasks:

-   Enumerate wireless interfaces. See [**WlanEnumInterfaces**](/windows/desktop/api/wlanapi/nf-wlanapi-wlanenuminterfaces).
-   Get the capabilities of an interface. See [**WlanGetInterfaceCapability**](/windows/desktop/api/wlanapi/nf-wlanapi-wlangetinterfacecapability).

    **Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:  ** This feature is not supported.

-   Query an interface. See [**WlanQueryInterface**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanqueryinterface).
-   Set parameters for a network interface. See [**WlanSetInterface**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlansetinterface). This function can be used to turn the wireless radio on and off (and therefore enable or disable wireless network connectivity).
-   Scan for available wireless networks. See [**WlanScan**](/windows/desktop/api/wlanapi/nf-wlanapi-wlanscan).
-   Get the list of available or visible wireless networks. See [**WlanGetAvailableNetworkList**](/windows/desktop/api/wlanapi/nf-wlanapi-wlangetavailablenetworklist).
-   Get, save, or delete a profile. See [**WlanGetProfile**](/windows/desktop/api/wlanapi/nf-wlanapi-wlangetprofile), [**WlanSetProfile**](/windows/desktop/api/wlanapi/nf-wlanapi-wlansetprofile), and [**WlanDeleteProfile**](/windows/desktop/api/wlanapi/nf-wlanapi-wlandeleteprofile).
-   Connect to or disconnect from a wireless network. See [**WlanConnect**](/windows/desktop/api/wlanapi/nf-wlanapi-wlanconnect) and [**WlanDisconnect**](/windows/desktop/api/wlanapi/nf-wlanapi-wlandisconnect).

## Related topics

<dl> <dt>

[Using Native Wifi](using-native-wifi.md)
</dt> <dt>

[Windows Vista Wireless SDK Forum](https://social.msdn.microsoft.com/Forums/b6bbd8f0-a921-480f-9b4b-845336462bc0/welcome-to-the-windows-vista-wireless-sdk-forum)
</dt> <dt>

[Troubleshooting Windows Vista 802.11 Wireless Connections](/previous-versions/windows/it-pro/windows-vista/cc766215(v=ws.10))
</dt> </dl>

 

 
