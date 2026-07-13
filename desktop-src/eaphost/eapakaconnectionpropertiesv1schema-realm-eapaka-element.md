---
title: Realm (EapAka) element
description: Learn about the Realm (EapAka) element. This string element denotes the realm to be used while sending the client identity to the server. | Realm (EapAka) element
ms.assetid: 3553c397-4205-4aa1-ba63-6f3ba75c6b97
keywords:
- Realm (EapAka) element EAPHost
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

# Realm (EapAka) element

**Realm (EapAka)** is a string element denoting the realm to be used while sending the client identity to the server. It also contains the *Enabled* attribute, which specifies whether the **Realm** string is to be used. If *Enabled* is set to `TRUE` and no **Realm** string is specified, the derived realm is used. If *Enabled* is set to `FALSE`, any **Realm** string, if specified, is not used.

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

The **Realm (EapAka)** element is defined as part of a sequence in a complex type within the **EapAka** element.

## Remarks

The **Realm (EapAka)** element is required.

## Requirements

| Role | Minimum OS version |
|------|--------------------|
| Client | Windows 8 \[desktop apps only\] |
| Server | Windows Server 2012 \[desktop apps only\] |

## See also

### Definition context of element in schema

- [EapAka](eapakaconnectionpropertiesv1schema-eapaka-element.md)

### Related links

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eapakaconnectionpropertiesv1](eapakaconnectionpropertiesv1schema-schema.md)
- [eapakaconnectionpropertiesv1 Schema Elements](eapakaconnectionpropertiesv1schema-elements.md)
