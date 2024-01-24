---
title: SSIDConfig (WLANProfile) element
description: Contains one or more SSIDs for wireless LANs.
ms.topic: reference
ms.date: 06/25/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SSIDConfig
api_type: 
- Schema
api_location: 
ms.assetid: f9c46db8-2933-48e1-8cb3-effeb13c43ed
---

# SSIDConfig (WLANProfile) element

The SSIDConfig (WLANProfile) element contains one or more SSIDs for wireless LANs. **SSID** *maxOccurs* is 1000 in v2; in v1, it's 256.

```XSD
<xs:element name="SSIDConfig"
    maxOccurs="256"
 >
    <xs:complexType>
        <xs:sequence>
            <xs:element name="SSID"
                maxOccurs="1000"
                ...
             />
            <xs:element name="SSIDPrefix"
                ...
             />
            <xs:element name="nonBroadcast"
                minOccurs="0"
                type="boolean"
             />
            <xs:any
                processContents="lax"
                minOccurs="0"
                maxOccurs="unbounded"
                namespace="##other"
             />
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

## Parent elements

* [**WLANProfile**](./wlan-profileschema-wlanprofile-element.md)

## Child elements

| Element | Type | Description |
| - | - | - |
| [**SSID**](./wlan-profileschema-ssid-ssidconfig-element.md) | | Contains an SSID for a wireless LAN. |
| [**SSIDPrefix**](./wlan-profileschema-ssidprefix-ssidconfig-element.md) | | Contains an SSID prefix for a wireless LAN. |
| [**nonBroadcast**](#nonbroadcast) | [boolean](/dotnet/api/system.boolean) | Indicates whether the network broadcasts its SSID.<br/> If [**connectionType**](wlan-profileschema-wlanprofile-element.md#connectiontype) is set to ESS, this value can be either **TRUE** or **FALSE**. The default value is **TRUE** if this element is absent.<br/> If [**connectionType**](wlan-profileschema-wlanprofile-element.md#connectiontype) is set to IBSS, this value must be **FALSE**.<br/> **Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported. |

### nonBroadcast

Specifies whether to connect to a hidden network. If a network doesn't broadcast its SSID, then it's known as a hidden network. If multiple SSIDs are set within the profile, then they must all have the same **nonBroadcast** value.

If [**connectionType**](wlan-profileschema-wlanprofile-element.md#connectiontype) is set to **ESS**, then **nonBroadcast** can be either "true" or "false". If this element is not present, the default value is "false".

If [**connectionType**](wlan-profileschema-wlanprofile-element.md#connectiontype) is set to **IBSS**, then **nonBroadcast** must be "false". If **nonBroadcast** isn't present, then the default value is "false".

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported.

## Examples

To view sample profiles that use the **SSIDConfig** element, see [Wireless profile samples](wireless-profile-samples.md). To view a sample profile that uses the **nonBroadcast** element, see [Non-Broadcast profile sample](non-broadcast-profile-sample.md).

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows Vista, Windows XP with SP3 \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
| Redistributable | Wireless LAN API for Windows XP with SP2 |
