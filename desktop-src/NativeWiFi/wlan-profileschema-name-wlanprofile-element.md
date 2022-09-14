---
description: Contains the name of a wireless LAN profile.
ms.assetid: b8977183-7b5d-4c79-9065-ade85ed45716
title: name (WLANProfile) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- name
api_type: 
- Schema
api_location: 
---

# name (WLANProfile) Element

The name (WLANProfile) element contains the name of a wireless LAN profile.

``` syntax
<xs:element name="name"
    type="nameType"
 />
```

The **name** element is defined by the [**WLANProfile**](wlan-profileschema-wlanprofile-element.md) element.

## Remarks

Names are case-sensitive.

For Windows XP with Service Pack 3 (SP3) and Wireless LAN API for Windows XP with Service Pack 2 (SP2), the name element is ignored when the profile is saved in the profile store. The name of the profile is derived from the SSID of the network. For infrastructure network profiles, the name of the profile is the SSID of the network. For ad hoc network profiles, the name of the profile is the SSID of the ad hoc network followed by `-adhoc`. XML escape characters, such as &, are not displayed. Avoid using XML escape characters in SSID names for profiles deployed on Windows XP with SP3 or Wireless LAN API for Windows XP with SP2.

For any network profile intended for use only on Windows Vista or Windows Server 2008, the name can be any string.

## Examples

To view sample profiles that use the **name** element, see [Wireless Profile Samples](wireless-profile-samples.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista, Windows XP with SP3 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                |
| Redistributable<br/>          | Wireless LAN API for Windows XP with SP2<br/>                 |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**WLANProfile**](wlan-profileschema-wlanprofile-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**WLANProfile**](wlan-profileschema-wlanprofile-element.md)
</dt> </dl>

 

 




