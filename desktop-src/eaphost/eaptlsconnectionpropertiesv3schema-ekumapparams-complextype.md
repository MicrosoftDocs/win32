---
title: EKUMapParams Complex Type
description: Learn about the EKUMapParams complex type. This type contains a list of EKUMapPair elements.
ms.assetid: 5c8c7a6f-9f6e-45eb-8894-503ca6f0e315
ms.topic: article
ms.date: 07/07/2023
---

# EKUMapParams Complex Type

The **EKUMapParams** complex type contains a list of [EKUMapPair](eaptlsconnectionpropertiesv3schema-ekumappair-complextype.md) elements.

```XML
<xs:complexType name="EKUMapParams">
    <xs:sequence>
        <xs:element name="EKUMap" type="EKUMapPair" minOccurs="1" maxOccurs="unbounded"/>
    </xs:sequence>
</xs:complexType>
```

## Remarks

The **EKUMapParams** element is optional.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eaptlsconnectionpropertiesv3](eaptlsconnectionpropertiesv3schema-schema.md)
- [eaptlsconnectionpropertiesv3 Complex Types](eaptlsconnectionpropertiesv3schema-complex-types.md)
- [Extensions (ExtensionParams)](eaptlsconnectionpropertiesv3schema-extensions-extensionparams-element.md)
