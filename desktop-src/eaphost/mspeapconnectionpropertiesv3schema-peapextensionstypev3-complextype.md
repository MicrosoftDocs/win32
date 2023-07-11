---
title: PeapExtensionsTypeV3 Complex Type
description: Learn about the PeapExtensionsTypeV3 complex type. This type enables future enhancements to the schema.
ms.assetid: 7b4bfe0f-e63c-40f0-930a-ee190879f5b1
ms.topic: article
ms.date: 07/10/2023
---

# PeapExtensionsTypeV3 Complex Type

**PeapExtensionsTypeV3** is an extensible field reserved for future extensions to the Microsoft PEAP implementation.

```XML
<xs:complexType name="PeapExtensionsTypeV3">
    <xs:sequence>
        <xs:any processContents="lax" minOccurs="0" maxOccurs="unbounded" namespace="##other"/>
    </xs:sequence>
</xs:complexType>
```

## Remarks

The **PeapExtensionsTypeV3** element is optional.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [mspeapconnectionpropertiesv3 Schema](mspeapconnectionpropertiesv3schema-schema.md)
- [mspeapconnectionpropertiesv3 Complex Types](mspeapconnectionpropertiesv3schema-complex-types.md)
- [PeapExtensionsTypeV2](mspeapconnectionpropertiesv2-peapextensionstypev2-complextype.md)
