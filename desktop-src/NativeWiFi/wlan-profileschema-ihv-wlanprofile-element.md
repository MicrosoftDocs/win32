---
title: IHV (WLANProfile) element
description: Contains various settings for independent hardware vendors.
ms.topic: reference
ms.date: 05/25/2023
ms.assetid: 4ad8c991-7849-41d6-9852-1ecadc372a2d
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IHV
api_type: 
- Schema
api_location: 
---

# IHV (WLANProfile) element

The IHV (WLANProfile) element contains various settings for independent hardware vendors. If a profile includes IHV security settings, they override any Microsoft-defined security.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported.

``` syntax
<xs:element name="IHV"
    minOccurs="0"
>
    <xs:complexType>
        <xs:sequence>
            <xs:element name="OUIHeader"
                ...
            />
            <xs:element name="connectivity"
                minOccurs="0"
            >
                <xs:complexType>
                    <xs:sequence>
                        <xs:any
                            processContents="lax"
                            namespace="##other"
                         />
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="security"
                minOccurs="0"
            >
                <xs:complexType>
                    <xs:sequence>
                        <xs:any
                            processContents="lax"
                            namespace="##other"
                         />
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="useMSOneX"
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

## Parent elements

* [**WLANProfile**](wlan-profileschema-wlanprofile-element.md)

## Child elements

| Element | Type | Description |
|-|-|-|
| [**connectivity**](#connectivity) | | Contains IHV-related connectivity settings. It isn't currently implemented. |
| [**OUIHeader**](wlan-profileschema-ouiheader-ihv-element.md) | | Identifies the IHV. |
| [**security**](#security) | | Contains various security settings used by independent hardware vendors (IHVs). |
| [**useMSOneX**](#usemsonex) | [boolean](/dotnet/api/system.boolean) | Specifies the origin of 802.1X security settings used by an IHV security component. When [**useMSOneX**](wlan-profileschema-ihv-wlanprofile-element.md#usemsonex) is true, IHV security components use Microsoft-defined 802.1X settings. When **useMSOneX** is false, IHV security components use vendor-supplied 802.1X settings. By default, **useMSOneX** is false. This element is optional. |

### connectivity

Contains IHV-related connectivity settings. It isn't currently implemented.

### security

Contains various security settings used by independent hardware vendors (IHVs).

Microsoft security settings and IHV security settings are mutually exclusive. If both sets of security settings are present in the same profile, then the profile is invalid.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported.

### useMSOneX

Specifies the origin of 802.1X security settings used by an IHV security component.

When **useMSOneX** is true, IHV security components use Microsoft-defined 802.1X settings. When **useMSOneX** is false, IHV security components use vendor-supplied 802.1X settings.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported.

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client | Windows Vista \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
