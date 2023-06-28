---
title: connectivity (MSM) element
description: Contains various connectivity settings.
ms.topic: reference
ms.date: 06/25/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- connectivity
api_type: 
- Schema
api_location: 
ms.assetid: 2938f607-47a1-49eb-bf3f-247cab8637ec
---

# connectivity (MSM) element

The connectivity (MSM) element contains various connectivity settings.

```XSD
<xs:element name="connectivity"
    minOccurs="0"
 >
    <xs:complexType>
        <xs:sequence>
            <xs:element name="phyType"
                minOccurs="0"
                maxOccurs="6"
             >
                <xs:simpleType>
                    <xs:restriction base="xs:string">
                        <xs:enumeration value="a">
                        <xs:enumeration value="b">
                        <xs:enumeration value="g">
                        <xs:enumeration value="n">
                        <xs:enumeration value="ac">
                        <xs:enumeration value="ad">
                        <xs:enumeration value="ax">
                        <xs:enumeration value="be">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="QoSDSCPToUPMappingAllowed"
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

* [**MSM (WLANProfile)**](./wlan-profileschema-msm-wlanprofile-element.md)

## Child elements

| Element | Type | Description |
| - | - | - |
| [**phyType**](#phytype) | | Specifies the 802.11 wireless LAN standard used on a wireless LAN. |
| [**QoSDSCPToUPMappingAllowed**](#qosdscptoupmappingallowed) | boolean | Configures whether mapping Quality of Service (QoS) DSCP to UP is allowed. |

### phyType

Specifies the 802.11 wireless LAN standard used on a wireless LAN.

You can specify multiple **phyType** elements. If no **phyType** is specified, then the profile can be used to connect to any **phyType**. The value "n" is supported only on Windows Vista with Service Pack 1 (SP1) and later versions of the operating system.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element isn't supported.

### QoSDSCPToUPMappingAllowed

Configures whether mapping Quality of Service (QoS) DSCP to UP is allowed.

## Examples

To view sample profiles that use the **connectivity** element, see [Wireless profile samples](wireless-profile-samples.md).

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows Vista, Windows XP with SP3 \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
| Redistributable | Wireless LAN API for Windows XP with SP2 |
