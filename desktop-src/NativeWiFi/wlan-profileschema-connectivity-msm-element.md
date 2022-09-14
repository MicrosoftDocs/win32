---
description: Contains various connectivity settings.
ms.assetid: 2938f607-47a1-49eb-bf3f-247cab8637ec
title: connectivity (MSM) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- connectivity
api_type: 
- Schema
api_location: 
---

# connectivity (MSM) Element

The connectivity (MSM) element contains various connectivity settings.

``` syntax
<xs:element name="connectivity"
    minOccurs="0"
>
    <xs:complexType>
        <xs:sequence>
            <xs:element name="phyType"
                minOccurs="0"
                maxOccurs="4"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="string"
                    >
                        <xs:enumeration
                            value="a"
                         />
                        <xs:enumeration
                            value="b"
                         />
                        <xs:enumeration
                            value="g"
                         />
                        <xs:enumeration
                            value="n"
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
```

The element is defined by the [**MSM**](wlan-profileschema-msm-wlanprofile-element.md) element.

## Child elements



| Element                                                            | Type |
|--------------------------------------------------------------------|------|
| [**phyType**](wlan-profileschema-phytype-connectivity-element.md) |      |



## Examples

To view sample profiles that use the **connectivity** element, see [Wireless Profile Samples](wireless-profile-samples.md).

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

[**MSM**](wlan-profileschema-msm-wlanprofile-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**MSM (WLANProfile)**](wlan-profileschema-msm-wlanprofile-element.md)
</dt> </dl>

 

 




