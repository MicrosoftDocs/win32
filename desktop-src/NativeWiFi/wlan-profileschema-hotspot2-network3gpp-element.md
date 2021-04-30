---
description: A list of Public Land Mobile Network (PLMN) IDs.
ms.assetid: 2e5e23c0-e98f-48f8-97b8-c5f88c80c51e
title: Network3GPP (Hotspot2) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Network3GPP
api_type: 
- Schema
api_location: 
---

# Network3GPP (Hotspot2) Element

A list of Public Land Mobile Network (PLMN) IDs.

``` syntax
<xs:element name="Network3GPP"
    minOccurs="0"
>
    <xs:complexType>
        <xs:sequence>
            <xs:element name="PLMNID"
                minOccurs="0"
                maxOccurs="256"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="string"
                    >
                        <xs:minLength
                            value="5"
                         />
                        <xs:maxLength
                            value="6"
                         />
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

The element is defined by the [**Hotspot2**](wlan-profileschema-hotspot2-element.md) element.

## Child elements



| Element | Type | Description                                                                                                             |
|---------|------|-------------------------------------------------------------------------------------------------------------------------|
| PLMNID  |      | An individual PLMN ID. This is a 5 or 6 digit decimal number corresponding to the MCC/MNC of a 3GPP network.<br/> |



 

 




