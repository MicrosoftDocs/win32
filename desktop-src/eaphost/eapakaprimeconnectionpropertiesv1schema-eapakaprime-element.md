---
title: EapAkaPrime element (eapakaprimeconnectionpropertiesv1)
description: This element is a derived type of the EapType element from the BaseEapConnectionProperties schema. For the eapakaprimeconnectionpropertiesv1.
ms.assetid: 94cb001a-f0ee-4f4c-b654-b3c61004e588
keywords:
- EapAkaPrime element EAPHost
topic_type:
- apiref
api_name:
- EapAkaPrime
api_type:
- Schema
ms.topic: reference
ms.date: 07/12/2023
api_location: 
ROBOTS: INDEX,FOLLOW
---

# EapAkaPrime element (eapakaprimeconnectionpropertiesv1)

The **EapAkaPrime** element is a derived type of the [**EapType**](baseeapconnectionpropertiesv1schema-eaptype-element.md) element from the [BaseEapConnectionProperties](baseeapconnectionpropertiesv1schema-schema.md) schema.

This derived **EapAkaPrime** element contains the following elements:

- [IgnoreNetworkNameMismatch](eapakaprimeconnectionpropertiesv1schema-ignorenetworknamemismatch-eapakaprime-element.md)
- [EnableFastReauth](eapakaprimeconnectionpropertiesv1schema-enablefastreauth-eapakaprime-element.md)
- [DontRevealPermanentID](eapakaprimeconnectionpropertiesv1schema-dontrevealpermanentid-eapakaprime-element.md)
- [ProviderName](eapakaprimeconnectionpropertiesv1schema-providername-eapakaprime-element.md)
- [Realm](eapakaprimeconnectionpropertiesv1schema-realm-eapakaprime-element.md)

``` xml
<xs:element name="EapAkaPrime">              
    <xs:complexType>
            <xs:sequence>
                <xs:element name="IgnoreNetworkNameMismatch" type="xs:boolean" minOccurs="0" maxOccurs="1"/>
                <xs:element name="EnableFastReauth" type="xs:boolean" minOccurs="0" maxOccurs="1"/>
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
- [eapakaprimeconnectionpropertiesv1 Schema](eapakaprimeconnectionpropertiesv1schema-schema.md)
- [eapakaprimeconnectionpropertiesv1 Schema Elements](eapakaprimeconnectionpropertiesv1schema-elements.md)
