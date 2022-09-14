---
description: Indicates whether to connect to a hidden network.
ms.assetid: 31b859e9-adc7-49e2-91d9-4fb63a35addb
title: nonBroadcast (SSIDConfig) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- nonBroadcast
api_type: 
- Schema
api_location: 
---

# nonBroadcast (SSIDConfig) Element

The nonBroadcast (SSIDConfig) element indicates whether to connect to a hidden network. If a network does not broadcast its SSID, then it is known as a hidden network. If multiple SSIDs are set within the profile, they must all have the same nonBroadcast value.

If [**connectionType**](wlan-profileschema-connectiontype-wlanprofile-element.md) is set to **ESS**, this value can be either "true" or "false". If this element is not present, the default value is "false".

If [**connectionType**](wlan-profileschema-connectiontype-wlanprofile-element.md) is set to **IBSS**, this value must be "false". If this element is not present, the default value is "false".

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element is not supported.

``` syntax
<xs:element name="nonBroadcast"
    type="boolean"
    minOccurs="0"
 />
```

The element is defined by the [**SSIDConfig**](wlan-profileschema-ssidconfig-wlanprofile-element.md) element.

## Examples

To view a sample profile that uses the **nonBroadcast** element, see [Non-Broadcast Profile Sample](non-broadcast-profile-sample.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**SSIDConfig**](wlan-profileschema-ssidconfig-wlanprofile-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**SSIDConfig (WLANProfile)**](wlan-profileschema-ssidconfig-wlanprofile-element.md)
</dt> </dl>

 

 




