---
title: EKUListPair Complex Type
description: Learn about the EKUListPair complex type. This type holds a list of Name / ID pairs.
ms.assetid: b587d521-f94a-48d7-9cc2-2898e5bdf0e7
ms.topic: article
ms.date: 07/07/2023
---

# EKUListPair Complex Type

The **EKUListPair** complex type holds a list of Name / ID pairs.

```XML
<xs:complexType name="EKUListPair">
    <xs:sequence>
        <xs:element name="EKUName" type="xs:string" minOccurs="0" maxOccurs="1"/>
        <xs:element name="EKUOID" type="xs:string" minOccurs="0" maxOccurs="1"/>
    </xs:sequence>
</xs:complexType>
```

## Remarks

The **EKUListPair** element is optional.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eaptlsconnectionpropertiesv3](eaptlsconnectionpropertiesv3schema-schema.md)
- [eaptlsconnectionpropertiesv3 Complex Types](eaptlsconnectionpropertiesv3schema-complex-types.md)
- [Extensions (ExtensionParams)](eaptlsconnectionpropertiesv3schema-extensions-extensionparams-element.md)
