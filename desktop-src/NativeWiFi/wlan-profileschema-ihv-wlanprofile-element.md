---
description: Contains various settings for independent hardware vendors.
ms.assetid: 4ad8c991-7849-41d6-9852-1ecadc372a2d
title: IHV (WLANProfile) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IHV
api_type: 
- Schema
api_location: 
---

# IHV (WLANProfile) Element

The IHV (WLANProfile) element contains various settings for independent hardware vendors. If a profile includes IHV security settings, they override any Microsoft-defined security.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element is not supported.

``` syntax
<xs:element name="IHV"
    minOccurs="0"
>
    <xs:complexType>
        <xs:sequence>
            <xs:element name="OUIHeader">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="OUI">
                            <xs:simpleType>
                                <xs:restriction
                                    base="hexBinary"
                                >
                                    <xs:length
                                        value="3"
                                     />
                                </xs:restriction>
                            </xs:simpleType>
                        </xs:element>
                        <xs:element name="type">
                            <xs:simpleType>
                                <xs:restriction
                                    base="hexBinary"
                                >
                                    <xs:length
                                        value="1"
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

The element is defined by the [**WLANProfile**](wlan-profileschema-wlanprofile-element.md) element.

## Child elements



| Element                                                             | Type                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------------------------|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**connectivity**](wlan-profileschema-connectivity-ihv-element.md) |                                                                   | Contains IHV-related connectivity settings.<br/>                                                                                                                                                                                                                                                                                                                                            |
| [**OUI**](wlan-profileschema-oui-ouiheader-element.md)             |                                                                   | Contains a 3 byte hexBinary that identifies the IHV.<br/>                                                                                                                                                                                                                                                                                                                                   |
| [**OUIHeader**](wlan-profileschema-ouiheader-ihv-element.md)       |                                                                   | Identifies the IHV.<br/>                                                                                                                                                                                                                                                                                                                                                                    |
| [**security**](wlan-profileschema-security-ihv-element.md)         |                                                                   | Contains IHV-specific security settings. Microsoft security settings and IHV security settings are mutually exclusive. The entire profile is invalid if both security settings are present.<br/>                                                                                                                                                                                            |
| [**type**](wlan-profileschema-type-ouiheader-element.md)           |                                                                   | Contains a 1 byte hexBinary that is used to differentiate NICs by the same IHV.<br/>                                                                                                                                                                                                                                                                                                        |
| [**useMSOneX**](wlan-profileschema-usemsonex-ihv-element.md)       | [boolean](/dotnet/api/system.boolean) | Specifies the origin of 802.1X security settings used by an IHV security component. When [**useMSOneX**](wlan-profileschema-usemsonex-ihv-element.md) is true, IHV security components use Microsoft-defined 802.1X settings. When **useMSOneX** is false, IHV security components use vendor-supplied 802.1X settings. By default, **useMSOneX** is false. This element is optional.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



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

 

 
