---
description: A subset of the Native Wifi API functionality is supported on Windows XP with Service Pack 2 (SP2) and Windows XP with Service Pack 3 (SP3).
ms.assetid: d32c4a03-59e8-4fdd-9d5a-e7ef0eb25e84
title: Native Wifi API Support on Windows XP
ms.topic: article
ms.date: 05/31/2018
---

# Native Wifi API Support on Windows XP

A subset of the Native Wifi API functionality is supported on Windows XP with Service Pack 2 (SP2) and Windows XP with Service Pack 3 (SP3). This functionality is included in Windows XP with SP3 by default. In Windows XP with SP2, this functionality can be added by applying a hotfix, which is known as Wireless LAN API for Windows XP with Service Pack 2 (SP2).

Because of underlying architectural differences in Windows XP, the Native Wifi API on has some limitations. Here is a list of limitations:

-   At most one SSID can be associated with a profile.
-   Infrastructure networks always appear before ad hoc networks in the profile list.
-   Profile names are derived from the SSID, and cannot be set by the user to an arbitrary string.
-   PHY types are not supported.
-   Pairwise master key (PMK) caching is not supported.
-   Independent hardware vendor (IHV) extensibility functions are not supported.
-   Profile permissions are not supported.
-   Only the wlan\_notification\_acm\_connection\_complete and the wlan\_notification\_acm\_disconnected notifications are available.
-   Global 802.1X and EAPOL configuration settings are not supported.

The following functions are supported by Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:

-   [**WLAN\_NOTIFICATION\_CALLBACK**](/windows/win32/api/wlanapi/nc-wlanapi-wlan_notification_callback)
-   [**WlanAllocateMemory**](/windows/desktop/api/wlanapi/nf-wlanapi-wlanallocatememory)
-   [**WlanCloseHandle**](/windows/desktop/api/wlanapi/nf-wlanapi-wlanclosehandle)
-   [**WlanConnect**](/windows/desktop/api/wlanapi/nf-wlanapi-wlanconnect)
-   [**WlanDeleteProfile**](/windows/desktop/api/wlanapi/nf-wlanapi-wlandeleteprofile)
-   [**WlanDisconnect**](/windows/desktop/api/wlanapi/nf-wlanapi-wlandisconnect)
-   [**WlanEnumInterfaces**](/windows/desktop/api/wlanapi/nf-wlanapi-wlanenuminterfaces)
-   [**WlanFreeMemory**](/windows/desktop/api/wlanapi/nf-wlanapi-wlanfreememory)
-   [**WlanGetAvailableNetworkList**](/windows/desktop/api/wlanapi/nf-wlanapi-wlangetavailablenetworklist)
-   [**WlanGetProfile**](/windows/desktop/api/wlanapi/nf-wlanapi-wlangetprofile)
-   [**WlanGetProfileList**](/windows/desktop/api/wlanapi/nf-wlanapi-wlangetprofilelist)
-   [**WlanOpenHandle**](/windows/desktop/api/wlanapi/nf-wlanapi-wlanopenhandle)
-   [**WlanQueryInterface**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanqueryinterface)
-   [**WlanReasonCodeToString**](/windows/desktop/api/wlanapi/nf-wlanapi-wlanreasoncodetostring)
-   [**WlanRegisterNotification**](/windows/desktop/api/wlanapi/nf-wlanapi-wlanregisternotification)
-   [**WlanScan**](/windows/desktop/api/wlanapi/nf-wlanapi-wlanscan)
-   [**WlanSetInterface**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlansetinterface)
-   [**WlanSetProfile**](/windows/desktop/api/wlanapi/nf-wlanapi-wlansetprofile)
-   [**WlanSetProfileEapXmlUserData**](/windows/desktop/api/wlanapi/nf-wlanapi-wlansetprofileeapxmluserdata)
-   [**WlanSetProfileList**](/windows/desktop/api/wlanapi/nf-wlanapi-wlansetprofilelist)
-   [**WlanSetProfilePosition**](/windows/desktop/api/wlanapi/nf-wlanapi-wlansetprofileposition)

## Related topics

<dl> <dt>

[About Native Wifi](about-native-wifi.md)
</dt> </dl>

 

 
