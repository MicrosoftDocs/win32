---
Description: Defines a WLAN profile used by the Native Wifi AutoConfig service.
ms.assetid: 8312d213-1d01-4bd0-a8d9-65ca23560888
title: WLAN\_profile Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WLAN\_profile Schema

The WLAN\_profile Schema defines a WLAN profile used by the Native Wifi AutoConfig service.

The AutoConfig service accepts wireless profiles from the Group Policy Agent, the scripting interface (**netsh**), the user interface, or from the USB flash configuration interface.

A profile received from one of these systems is mapped to the WLAN\_profile schema and stored in the profile store. Profiles can be exported from the profile store using netsh commands or using API elements such as [**WlanGetProfile**](/windows/desktop/api/wlanapi/nf-wlanapi-wlangetprofile).

The root element of a WLAN profile is the [**WLANProfile**](wlan-profileschema-wlanprofile-element.md) element. Each profile will have exactly one root element. The **WLANProfile** element is in the namespace `http://www.microsoft.com/networking/WLAN/profile/v1`.

To view sample WLAN profiles, see [Wireless Profile Samples](wireless-profile-samples.md).

-   [WLAN\_profile Schema Elements](wlan-profileschema-elements.md)
-   [WLAN\_profile Schema Simple Types](wlan-profileschema-simple-types.md)

## Related topics

<dl> <dt>

[Netsh Commands for Wireless Local Area Network (wlan)](Http://go.microsoft.com/fwlink/p/?linkid=120964)
</dt> </dl>

 

 



