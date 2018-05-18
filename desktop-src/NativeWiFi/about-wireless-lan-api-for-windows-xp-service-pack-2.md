---
Description: 'A subset of the Native Wifi API functionality is supported on Windows XP with Service Pack 2 (SP2) and Windows XP with Service Pack 3 (SP3).'
ms.assetid: 'd32c4a03-59e8-4fdd-9d5a-e7ef0eb25e84'
title: Native Wifi API Support on Windows XP
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

-   [**WLAN\_NOTIFICATION\_CALLBACK**](notif-callback.md)
-   [**WlanAllocateMemory**](wlanallocatememory.md)
-   [**WlanCloseHandle**](wlanclosehandle.md)
-   [**WlanConnect**](wlanconnect.md)
-   [**WlanDeleteProfile**](wlandeleteprofile.md)
-   [**WlanDisconnect**](wlandisconnect.md)
-   [**WlanEnumInterfaces**](wlanenuminterfaces.md)
-   [**WlanFreeMemory**](wlanfreememory.md)
-   [**WlanGetAvailableNetworkList**](wlangetavailablenetworklist.md)
-   [**WlanGetProfile**](wlangetprofile.md)
-   [**WlanGetProfileList**](wlangetprofilelist.md)
-   [**WlanOpenHandle**](wlanopenhandle.md)
-   [**WlanQueryInterface**](wlanqueryinterface.md)
-   [**WlanReasonCodeToString**](wlanreasoncodetostring.md)
-   [**WlanRegisterNotification**](wlanregisternotification.md)
-   [**WlanScan**](wlanscan.md)
-   [**WlanSetInterface**](wlansetinterface.md)
-   [**WlanSetProfile**](wlansetprofile.md)
-   [**WlanSetProfileEapXmlUserData**](wlansetprofileeapxmluserdata.md)
-   [**WlanSetProfileList**](wlansetprofilelist.md)
-   [**WlanSetProfilePosition**](wlansetprofileposition.md)

## Related topics

<dl> <dt>

[http://support.microsoft.com/kb/918997](Http://go.microsoft.com/fwlink/p/?linkid=83994)
</dt> <dt>

[About Native Wifi](about-native-wifi.md)
</dt> </dl>

 

 



