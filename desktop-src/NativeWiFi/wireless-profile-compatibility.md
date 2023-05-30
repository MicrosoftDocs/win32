---
description: Because of underlying architectural differences in the operating system, Windows XP with Service Pack 3 (SP3) and Wireless LAN API for Windows XP with Service Pack 2 (SP2) support only a subset of the elements described in the WLAN\_profile Schema and OneX Schema reference material.
ms.assetid: 28c956c0-a0e2-4843-956d-abeab418604e
title: Wireless Profile Compatibility
ms.topic: article
ms.date: 05/31/2018
---

# Wireless Profile Compatibility

Because of underlying architectural differences in the operating system, Windows XP with Service Pack 3 (SP3) and Wireless LAN API for Windows XP with Service Pack 2 (SP2) support only a subset of the elements described in the [WLAN\_profile Schema](wlan-profileschema-schema.md) and [OneX Schema](onexschema-schema.md) reference material.

All profiles that conform to Windows XP with SP3 and Wireless LAN API for Windows XP with SP2 requirements can also be used on Windows Vista and Windows Server 2008.

## WLAN\_profile Support

The following WLAN\_profile elements are not supported in Windows XP with SP3 or Wireless LAN API for Windows XP with SP2:

-   connectivity (IHV)
-   IHV (WLANProfile)
-   OUI (OUIHeader)
-   phyType (connectivity)
-   PMKCacheMode (security)
-   PMKCacheSize (security)
-   PMKCacheTTL (security)
-   preAuthMode (security)
-   preAuthThrottle (security)
-   security (IHV)
-   type (OUIHeader)
-   useMSOneX (IHV)

The following table shows WLAN\_profile elements with constrained values for Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:



| Element                                                                               | Constraint                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**name (WLANProfile)**](wlan-profileschema-wlanprofile-element.md#name)             | The name element is ignored when the profile is saved in the profile store. The name of the profile is derived automatically from the SSID of the network. For infrastructure network profiles, the name of the profile is the SSID of the network. For ad hoc network profiles, the name of the profile is the SSID of the ad hoc network followed by `-adhoc`. |
| [**protected (sharedKey)**](wlan-profileschema-sharedkey-security-element.md#protected)       | Must have a value of FALSE.                                                                                                                                                                                                                                                                                                                                      |
| [**SSIDConfig (WLANProfile)**](wlan-profileschema-ssidconfig-wlanprofile-element.md) | Restricted to one child [**SSID (SSIDConfig)**](wlan-profileschema-ssid-ssidconfig-element.md) element.                                                                                                                                                                                                                                                         |



 

## OneX Support

Only the [**EAPConfig**](onexschema-eapconfig-onex-element.md) element is supported on Windows XP with SP3 and Wireless LAN API for Windows XP with SP2. Other OneX elements, if present in a profile, will be ignored.

## Related topics

<dl> <dt>

[About the Native Wifi API](about-the-native-wifi-api.md)
</dt> <dt>

[Native Wifi API Support on Windows XP](about-wireless-lan-api-for-windows-xp-service-pack-2.md)
</dt> </dl>

 

 



