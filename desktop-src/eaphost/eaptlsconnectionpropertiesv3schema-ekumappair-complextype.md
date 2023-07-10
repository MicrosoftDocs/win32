---
title: EKUMapPair Complex Type
description: Learn about the EKUMapPair complex type. This type holds a Name / ID pair.
ms.assetid: 3afd5dbf-c82b-4542-a5a0-a01c2608df45
ms.topic: article
ms.date: 07/07/2023
---

# EKUMapPair Complex Type

The **EKUMapPair** complex type holds a Name / ID pair.

```XML
<xs:complexType name="EKUMapPair">
    <xs:sequence>
        <xs:element name="EKUName" type="xs:string" minOccurs="1" maxOccurs="1"/>
        <xs:element name="EKUOID" type="xs:string" minOccurs="1" maxOccurs="1"/>
    </xs:sequence>
</xs:complexType>
```

## Remarks

The **EKUMapPair** element is required when an [EKUMapParams](./eaptlsconnectionpropertiesv3schema-ekumapparams-complextype.md) parameter is provided.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eaptlsconnectionpropertiesv3](eaptlsconnectionpropertiesv3schema-schema.md)
- [eaptlsconnectionpropertiesv3 Complex Types](eaptlsconnectionpropertiesv3schema-complex-types.md)
- [Extensions (ExtensionParams)](eaptlsconnectionpropertiesv3schema-extensions-extensionparams-element.md)
