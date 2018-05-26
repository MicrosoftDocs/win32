---
Description: A subset of the Native Wifi API functionality is supported on Windows XP with Service Pack 2 (SP2) and Windows XP with Service Pack 3 (SP3).
ms.assetid: d32c4a03-59e8-4fdd-9d5a-e7ef0eb25e84
title: Native Wifi API Support on Windows XP
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Native Wifi API Support on Windows XP

A subset of the Native Wifi API functionality is supported on Windows XP with Service Pack 2 (SP2) and Windows XP with Service Pack 3 (SP3). This functionality is included in Windows XP with SP3 by default. In Windows XP with SP2, this functionality can be added by applying a hotfix, which is known as Wireless LAN API for Windows XP with Service Pack 2 (SP2). For more information or to download the hotfix, see "Developers cannot create wireless client programs that manage wireless profiles and connections over the Wireless Zero Configuration service in Microsoft Windows XP Service Pack 2 (SP2)" in the Help and Support Knowledge Base at [http://support.microsoft.com/kb/918997](Http://go.microsoft.com/fwlink/p/?linkid=83994).

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

-   [**WLAN\_NOTIFICATION\_CALLBACK**](/windows/win32/wlanapi/nc-wlanapi-wlan_notification_callback?branch=master)
-   [**WlanAllocateMemory**](/windows/win32/wlanapi/nf-wlanapi-wlanallocatememory?branch=master)
-   [**WlanCloseHandle**](/windows/win32/wlanapi/nf-wlanapi-wlanclosehandle?branch=master)
-   [**WlanConnect**](/windows/win32/wlanapi/nf-wlanapi-wlanconnect?branch=master)
-   [**WlanDeleteProfile**](/windows/win32/wlanapi/nf-wlanapi-wlandeleteprofile?branch=master)
-   [**WlanDisconnect**](/windows/win32/wlanapi/nf-wlanapi-wlandisconnect?branch=master)
-   [**WlanEnumInterfaces**](/windows/win32/wlanapi/nf-wlanapi-wlanenuminterfaces?branch=master)
-   [**WlanFreeMemory**](/windows/win32/wlanapi/nf-wlanapi-wlanfreememory?branch=master)
-   [**WlanGetAvailableNetworkList**](/windows/win32/wlanapi/nf-wlanapi-wlangetavailablenetworklist?branch=master)
-   [**WlanGetProfile**](/windows/win32/wlanapi/nf-wlanapi-wlangetprofile?branch=master)
-   [**WlanGetProfileList**](/windows/win32/wlanapi/nf-wlanapi-wlangetprofilelist?branch=master)
-   [**WlanOpenHandle**](/windows/win32/wlanapi/nf-wlanapi-wlanopenhandle?branch=master)
-   [**WlanQueryInterface**](/windows/win32/Wlanapi/nf-wlanapi-wlanqueryinterface?branch=master)
-   [**WlanReasonCodeToString**](/windows/win32/wlanapi/nf-wlanapi-wlanreasoncodetostring?branch=master)
-   [**WlanRegisterNotification**](/windows/win32/wlanapi/nf-wlanapi-wlanregisternotification?branch=master)
-   [**WlanScan**](/windows/win32/wlanapi/nf-wlanapi-wlanscan?branch=master)
-   [**WlanSetInterface**](/windows/win32/Wlanapi/nf-wlanapi-wlansetinterface?branch=master)
-   [**WlanSetProfile**](/windows/win32/wlanapi/nf-wlanapi-wlansetprofile?branch=master)
-   [**WlanSetProfileEapXmlUserData**](/windows/win32/wlanapi/nf-wlanapi-wlansetprofileeapxmluserdata?branch=master)
-   [**WlanSetProfileList**](/windows/win32/wlanapi/nf-wlanapi-wlansetprofilelist?branch=master)
-   [**WlanSetProfilePosition**](/windows/win32/wlanapi/nf-wlanapi-wlansetprofileposition?branch=master)

## Related topics

<dl> <dt>

[http://support.microsoft.com/kb/918997](Http://go.microsoft.com/fwlink/p/?linkid=83994)
</dt> <dt>

[About Native Wifi](about-native-wifi.md)
</dt> </dl>

 

 



