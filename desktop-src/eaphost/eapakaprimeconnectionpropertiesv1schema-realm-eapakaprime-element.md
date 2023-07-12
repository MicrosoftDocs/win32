---
title: Realm (EapAkaPrime) element
description: Learn about the Realm (EapAkaPrime) element. This string element denotes the realm to be used while sending the client identity to the server. | Realm (EapAkaPrime) element
ms.assetid: acf3b683-890c-4864-b650-45beb6a04a39
keywords:
- Realm (EapAkaPrime) element EAPHost
topic_type:
- apiref
api_name:
- Realm
api_type:
- Schema
ms.topic: reference
ms.date: 07/12/2023
api_location: 
ROBOTS: INDEX,FOLLOW
---

# Realm (EapAkaPrime) element

**Realm (EapAkaPrime)** is a string element denoting the realm to be used while sending the client identity to the server. It also contains the *Enabled* attribute, which specifies whether the **Realm** string is to be used. If *Enabled* is set to `TRUE` and no **Realm** string is specified, the derived realm is used. If *Enabled* is set to `FALSE`, any **Realm** string, if specified, is not used.

``` xml
<xs:element name="Realm">
    <xs:complexType>
        <xs:simpleContent>
        <xs:extension base="xs:string">
            <xs:attribute name="Enabled" type="xs:boolean" use="required"/>
        </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
```

The **Realm (EapAkaPrime)** element is defined as part of a sequence in a complex type within the **EapAkaPrime** element.

## Remarks

The **Realm (EapAkaPrime)** element is required.

## Requirements

| Role | Minimum OS version |
|------|--------------------|
| Client | Windows 8 \[desktop apps only\] |
| Server | Windows Server 2012 \[desktop apps only\] |

## See also

### Definition context of element in schema

- [EapAkaPrime](eapakaprimeconnectionpropertiesv1schema-eapakaprime-element.md)

### Related links

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eapakaprimeconnectionpropertiesv1](eapakaprimeconnectionpropertiesv1schema-schema.md)
- [eapakaprimeconnectionpropertiesv1 Schema Elements](eapakaprimeconnectionpropertiesv1schema-elements.md)
