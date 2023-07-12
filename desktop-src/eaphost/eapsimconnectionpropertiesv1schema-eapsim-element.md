---
title: EapSim element (eapsimconnectionpropertiesv1schema)
description: This element is a derived type of the EapType element from the BaseEapConnectionProperties schema. For the eapsimconnectionpropertiesv1schema.
ms.assetid: 13d245a2-fdc3-4727-bd85-baa8978183cc
keywords:
- EapSim element EAPHost
topic_type:
- apiref
api_name:
- EapSim
api_type:
- Schema
ms.topic: reference
ms.date: 07/12/2023
api_location: 
ROBOTS: INDEX,FOLLOW
---

# EapSim element (eapsimconnectionpropertiesv1schema)

The **EapSim** element is a derived type of the [**EapType**](baseeapconnectionpropertiesv1schema-eaptype-element.md) element from the [BaseEapConnectionProperties](baseeapconnectionpropertiesv1schema-schema.md) schema.

This derived **EapSim** element contains the following elements:

- [UseStrongCipherKeys](eapsimconnectionpropertiesv1schema-usestrongcipherkeys-eapsim-element.md)
- [DontRevealPermanentID](eapsimconnectionpropertiesv1schema-dontrevealpermanentid-eapsim-element.md)
- [ProviderName](eapsimconnectionpropertiesv1schema-providername-eapsim-element.md)
- [Realm](eapsimconnectionpropertiesv1schema-realm-eapsim-element.md)

``` xml
<xs:element name="EapSim">
    <xs:complexType>
                <xs:sequence>
                    <xs:element name="UseStrongCipherKeys" type="xs:boolean" minOccurs="0" maxOccurs="1"/>
                    <xs:element name="DontRevealPermanentID" type="xs:boolean" minOccurs="0" maxOccurs="1"/>
                    <xs:element name="ProviderName" type="xs:string" minOccurs="0" maxOccurs="1"/>
                    <xs:element name="Realm">
                    <xs:complexType>
                        <xs:simpleContent>
                        <xs:extension base="xs:string">
                            <xs:attribute name="Enabled" type="xs:boolean" use="required"/>
                        </xs:extension>
                        </xs:simpleContent>
                    </xs:complexType>
                    </xs:element>
                    <!-- extension point for other namespaces -->
                    <xs:any processContents="lax" minOccurs="0" maxOccurs="unbounded" namespace="##other"/>
                </xs:sequence>
    </xs:complexType>
</xs:element>
```

## Requirements

| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\] |
| Minimum supported server | Windows Server 20012 \[desktop apps only\] |

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eaptlsconnectionpropertiesv1 Schema](eaptlsconnectionpropertiesv1schema-schema.md)
- [eaptlsconnectionpropertiesv1 Schema Elements](eaptlsconnectionpropertiesv1schema-elements.md)
