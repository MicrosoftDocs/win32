---
title: WLANProfile element
description: Contains a wireless LAN profile.
ms.topic: reference
ms.date: 05/25/2023
ms.assetid: bc97cb49-3891-4a4a-aab4-895cd9ce6908
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WLANProfile
api_type: 
- Schema
api_location: 
---

# WLANProfile element

The **WLANProfile** element contains a wireless LAN profile. This element is the unique root element for a wireless profile.

The target namespace for the WLANProfile element is `https://www.microsoft.com/networking/WLAN/profile/v1`.

``` syntax
<xs:element name="WLANProfile">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="name"
                type="nameType"
             />
            <xs:element name="SSIDConfig"
                maxOccurs="256"
                ...
            />
            <xs:element name="connectionType">
                <xs:simpleType>
                    <xs:restriction
                        base="string"
                    >
                        <xs:enumeration
                            value="IBSS"
                         />
                        <xs:enumeration
                            value="ESS"
                         />
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="connectionMode"
                minOccurs="0"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="string"
                    >
                        <xs:enumeration
                            value="auto"
                         />
                        <xs:enumeration
                            value="manual"
                         />
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="autoSwitch"
                type="boolean"
                minOccurs="0"
             />
            <xs:any
                processContents="lax"
                minOccurs="0"
                maxOccurs="unbounded"
                namespace="##other"
             />
            <xs:element name="MSM"
                minOccurs="0"
                ...
            />
            <xs:element name="IHV"
                minOccurs="0"
                ...
            />
            <xs:element name="Hotspot2"
                ...
            />
            <xs:element name="MacRandomization"
                ...
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

None.

## Child elements

| Element | Type | Description |
|-|-|-|
| [**autoSwitch**](#autoswitch) | [boolean](/dotnet/api/system.boolean) | Determines the roaming behavior of an auto-connected network when a more preferred network is in range. This element is optional, and has no effect on a manually connected network.|
| [**connectionMode**](#connectionmode) | | Indicates whether connection to the wireless LAN should be automatic ("auto") or initiated ("manual") by user. This element is optional. |
| [**connectionType**](#connectiontype) | | Indicates whether the network is infrastructure ("ESS") or ad-hoc ("IBSS"). |
| [**Hotspot2**](wlan-profileschema-hotspot2-wlanprofile-element.md) | | Extends the WLAN Profile Schema v1 to support Hotspot 2.0 networks. |
| [**IHV**](wlan-profileschema-ihv-wlanprofile-element.md) | | Contains optional independent hardware vendor (IHV) settings.<br/> **Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported. |
| [**MSM**](wlan-profileschema-msm-wlanprofile-element.md) | | Contains various MSM settings. This element is optional. |
| [**MacRandomization**](wlan-profileschema-macrandomization-wlanprofile-element.md) | | Configures the randomization of MAC addresses. |
| [**name**](#name) | [**nameType**](wlan-profileschema-simple-types.md#nametype) | Name of the WLAN profile. |
| [**SSIDConfig**](wlan-profileschema-ssidconfig-wlanprofile-element.md) | | Contains one or more SSIDs along with other common settings. <br/> A profile can have multiple [**SSIDConfig**](wlan-profileschema-ssidconfig-wlanprofile-element.md) elements and each [**SSIDConfig**](wlan-profileschema-ssidconfig-wlanprofile-element.md) element can have multiple [**SSID**](wlan-profileschema-ssid-ssidconfig-element.md) elements. However, Windows only ever considers the first [**SSIDConfig**](wlan-profileschema-ssidconfig-wlanprofile-element.md) element in a [**WLANProfile**](wlan-profileschema-wlanprofile-element.md) element.<br/> **Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** At most one [**SSID**](wlan-profileschema-ssid-ssidconfig-element.md) element can appear in a profile. |

### autoSwitch

Determines the roaming behavior of an auto-connected network when a more preferred network is in range. This element is optional.

If autoSwitch is "true" and [**connectionMode**](#connectionmode) is set to "auto", a connection to a more preferred network must be attempted whenever a more preferred network comes into range. A more preferred network is one that is ordered higher in the list of preferred wireless networks. This connection attempt occurs when connected to another network.

If [**connectionMode**](#connectionmode) is set to "auto", this value can be either "true" or "false".

If [**connectionMode**](#connectionmode) is set to "manual", this value must be set to "false". This element has no effect on a manually connected network.

An autoSwitch value set to "true" results in a higher frequency of periodic scanning for new networks. This may result in increased radio frequency pollution from these periodic scans and increased power consumption used by the wireless network adapter.

**Windows 7 and Windows Server 2008 R2 with the Wireless LAN Service installed:** Changes are implemented on Windows 7 and Windows Server 2008 R2 with the Wireless LAN Service installed to optimize wireless networking performance. These changes are designed to reduce radio frequency pollution, power consumption, and disruption to real-time traffic over wireless networks. The default setting for **autoSwitch** when this element is not set in a wireless LAN profile has changed. The default setting is changed to "false" on Windows 7 and Windows Server 2008 R2 with the Wireless LAN Service installed. The default setting was "true" on Windows Server 2008 and Windows Vista. It is recommended that the value of the **autoSwitch** element used by an application in a wireless LAN profile be set to "false" to reduce the frequency of periodic scanning for new networks, unless it is absolutely necessary for an application to set this value to "true".

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported.

### connectionMode

The connectionMode (WLANProfile) element indicates whether connection to a wireless LAN should be automatic or initiated by user.

If [**connectionType**](wlan-profileschema-wlanprofile-element.md#connectiontype) is set to ESS, this value can be either auto or manual. The default value is auto if this element is absent.

If [**connectionType**](wlan-profileschema-wlanprofile-element.md#connectiontype) is set to IBSS, this value must be manual.

``` syntax
<xs:element name="connectionMode">
    <xs:simpleType>
        <xs:restriction
            base="string"
        >
            <xs:enumeration
                value="auto"
             />
            <xs:enumeration
                value="manual"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The following table describes the enumeration values.

| Value  | Description                                                                                                |
|--------|------------------------------------------------------------------------------------------------------------|
| auto   | The connection to the wireless network should be initiated automatically whenever the network is in range. |
| manual | The connection to the wireless network is only initated upon the explicit request of a user.               |

### connectionType

The connectionType element indicates the operating mode of the network. A value of **ESS** indicates an infrastructure network, while **IBSS** indicates an ad-hoc network.

### name

Contains the name of a wireless LAN profile.

A **name** is case-sensitive.

For Windows XP with Service Pack 3 (SP3) and Wireless LAN API for Windows XP with Service Pack 2 (SP2), the **name** element is ignored when the profile is saved in the profile store. The name of the profile is derived from the SSID of the network. For infrastructure network profiles, the name of the profile is the SSID of the network. For ad hoc network profiles, the name of the profile is the SSID of the ad hoc network followed by `-adhoc`. XML escape characters, such as &, are not displayed. Avoid using XML escape characters in SSID names for profiles deployed on Windows XP with SP3 or Wireless LAN API for Windows XP with SP2.

For any network profile intended for use only on Windows Vista or Windows Server 2008, the name can be any string.

## Remarks

Most child elements of the WLANProfile element are in the `https://www.microsoft.com/networking/WLAN/profile/v1` namespace. There are two exceptions: the [**FIPSMode**](wlan-profileschema-authencryption-security-element.md#fipsmode) element is in the `https://www.microsoft.com/networking/WLAN/profile/v2` namespace, and the [**OneX**](onexschema-onex-element.md) element is in the `https://www.microsoft.com/networking/OneX/v1` namespace.

To view the list of child elements in a tree-like structure, see [WLAN\_profile Schema Elements](wlan-profileschema-elements.md).

## Examples

To view sample profiles, see [Wireless profile samples](wireless-profile-samples.md).

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client | Windows Vista, Windows XP with SP3 \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
| Redistributable | Wireless LAN API for Windows XP with SP2 |
