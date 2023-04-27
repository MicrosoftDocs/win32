---
title: SSIDConfig (WLANProfile) element
description: Contains one or more SSIDs for wireless LANs.
ms.assetid: f9c46db8-2933-48e1-8cb3-effeb13c43ed
ms.topic: reference
ms.date: 04/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SSIDConfig
api_type: 
- Schema
api_location: 
---

# SSIDConfig (WLANProfile) element

The SSIDConfig (WLANProfile) element contains one or more SSIDs for wireless LANs.

``` syntax
<xs:element name="SSIDConfig"
    maxOccurs="256"
>
    <xs:complexType>
        <xs:sequence>
            <xs:element name="SSID"
                maxOccurs="256"
            >
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="hex"
                            minOccurs="0"
                        >
                            <xs:simpleType>
                                <xs:restriction
                                    base="hexBinary"
                                >
                                    <xs:minLength
                                        value="1"
                                     />
                                    <xs:maxLength
                                        value="32"
                                     />
                                </xs:restriction>
                            </xs:simpleType>
                        </xs:element>
                        <xs:element name="name"
                            minOccurs="0"
                        >
                            <xs:simpleType>
                                <xs:restriction
                                    base="string"
                                >
                                    <xs:minLength
                                        value="1"
                                     />
                                    <xs:maxLength
                                        value="32"
                                     />
                                </xs:restriction>
                            </xs:simpleType>
                        </xs:element>
                        <xs:any
                            processContents="lax"
                            minOccurs="0"
                            maxOccurs="unbounded"
                            namespace="##other"
                         />
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="SSIDPrefix"
            >
                <xs:complexType>
                    <xs:sequence>
                        <!-- Either Hex or named SSID must be present. -->
                        <!-- Hex SSID takes precedence over named SSID. -->
                        <xs:element name="hex"
                            minOccurs="0"
                        >
                            <xs:simpleType>
                                <xs:restriction
                                    base="hexBinary"
                                >
                                    <xs:minLength
                                        value="4"
                                     />
                                    <xs:maxLength
                                        value="32"
                                     />
                                </xs:restriction>
                            </xs:simpleType>
                        </xs:element>
                        <xs:element name="name"
                            minOccurs="0"
                        >
                            <xs:simpleType>
                                <xs:restriction
                                    base="string"
                                >
                                    <xs:minLength
                                        value="4"
                                     />
                                    <xs:maxLength
                                        value="32"
                                     />
                                </xs:restriction>
                            </xs:simpleType>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="nonBroadcast"
                type="boolean"
                minOccurs="0"
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

The **SSIDConfig** element is defined by the [**WLANProfile**](wlan-profileschema-wlanprofile-element.md) element.

## Child elements

| Element | Type | Description |
|-|-|-|
| [**SSID**](wlan-profileschema-ssid-ssidconfig-element.md) | | Contains an SSID for a wireless LAN.<br/> **Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** At most one [**SSID**](wlan-profileschema-ssid-ssidconfig-element.md) element can appear in a profile.|
| [**SSIDPrefix**](wlan-profileschema-ssidprefix-ssidconfig-element.md) | | Contains an SSID prefix for a wireless LAN.|
| [**nonBroadcast**](wlan-profileschema-nonbroadcast-ssidconfig-element.md) | [boolean](/dotnet/api/system.boolean) | Indicates whether the network broadcasts its SSID.<br/> If [**connectionType**](wlan-profileschema-connectiontype-wlanprofile-element.md) is set to ESS, this value can be either **TRUE** or **FALSE**. The default value is **TRUE** if this element is absent.<br/> If [**connectionType**](wlan-profileschema-connectiontype-wlanprofile-element.md) is set to IBSS, this value must be **FALSE**.<br/> **Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element is not supported.|

## Examples

To view sample profiles that use the **SSIDConfig** element, see [Wireless Profile Samples](wireless-profile-samples.md).

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
