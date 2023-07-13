---
title: EapAka element (eapakaconnectionpropertiesv1)
description: This element is a derived type of the EapType element from the BaseEapConnectionProperties schema. For the eapakaconnectionpropertiesv1.
ms.assetid: 2ed4b44b-6158-4301-be1c-a3ed7fefac2f
keywords:
- EapAka element EAPHost
topic_type:
- apiref
api_name:
- EapAka
api_type:
- Schema
ms.topic: reference
ms.date: 07/12/2023
api_location: 
ROBOTS: INDEX,FOLLOW
---

# EapAka element (eapakaconnectionpropertiesv1)

The **EapAka** element is a derived type of the [**EapType**](baseeapconnectionpropertiesv1schema-eaptype-element.md) element from the [BaseEapConnectionProperties](baseeapconnectionpropertiesv1schema-schema.md) schema.

This derived **EapAka** element contains the following elements:

- [DontRevealPermanentID](eapakaconnectionpropertiesv1schema-dontrevealpermanentid-eapaka-element.md)
- [ProviderName](eapakaconnectionpropertiesv1schema-providername-eapaka-element.md)
- [Realm](eapakaconnectionpropertiesv1schema-realm-eapaka-element.md)

``` xml
<xs:element name="EapAka">              
    <xs:complexType>
            <xs:sequence>
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
- [eapakaconnectionpropertiesv1 Schema](eapakaconnectionpropertiesv1schema-schema.md)
- [eapakaconnectionpropertiesv1 Schema Elements](eapakaconnectionpropertiesv1schema-elements.md)
