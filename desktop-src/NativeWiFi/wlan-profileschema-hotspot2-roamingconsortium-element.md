---
description: A list of Organizationally Unique Identifiers (OUI) assigned by IEEE.
ms.assetid: 4a9885b6-2e57-4a16-8e1d-b5b0797e09db
title: RoamingConsortium (Hotspot2) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RoamingConsortium
api_type: 
- Schema
api_location: 
---

# RoamingConsortium (Hotspot2) Element

A list of Organizationally Unique Identifiers (OUI) assigned by IEEE.

``` syntax
<xs:element name="RoamingConsortium"
    minOccurs="0"
>
    <xs:complexType>
        <xs:sequence>
            <xs:element name="OUI"
                minOccurs="0"
                maxOccurs="256"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="hexBinary"
                    >
                        <xs:minLength
                            value="3"
                         />
                        <xs:maxLength
                            value="5"
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



| Element | Type | Description                                                               |
|---------|------|---------------------------------------------------------------------------|
| OUI     |      | A single OUI, formatted as a variable size hexadecimal number.<br/> |



 

 




