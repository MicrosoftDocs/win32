---
title: Realm (EapSim) element
description: Learn about the Realm (EapSim) element. This string element denotes the realm to be used while sending the client identity to the server. | Realm (EapSim) element
ms.assetid: 63fb93ba-f8db-4649-8a06-54948811188a
keywords:
- Realm (EapSim) element EAPHost
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

# Realm (EapSim) element

**Realm (EapSim)** is a string element denoting the realm to be used while sending the client identity to the server. It also contains the *Enabled* attribute, which specifies whether the **Realm** string is to be used. If *Enabled* is set to `TRUE` and no **Realm** string is specified, the derived realm is used. If *Enabled* is set to `FALSE`, any **Realm** string, if specified, is not used.

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

The **Realm (EapSim)** element is defined as part of a sequence in a complex type within the **EapSim** element.

## Remarks

The **Realm (EapSim)** element is required.

## Requirements

| Role | Minimum OS version |
|------|--------------------|
| Client | Windows 8 \[desktop apps only\] |
| Server | Windows Server 2012 \[desktop apps only\] |

## See also

### Definition context of element in schema

- [EapSim](eapsimconnectionpropertiesv1schema-eapsim-element.md)

### Related links

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eapteapconnectionpropertiesv1](eapteapconnectionpropertiesv1schema-schema.md)
- [eapteapconnectionpropertiesv1 Schema Elements](eapteapconnectionpropertiesv1schema-elements.md)
