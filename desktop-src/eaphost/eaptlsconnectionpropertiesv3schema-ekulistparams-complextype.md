---
title: EKUListParams Complex Type
description: Learn about the EKUListParams complex type. This type holds a list of EKUListPair elements.
ms.assetid: 46d713b9-6701-4f70-bcff-305c2f613220
ms.topic: article
ms.date: 07/07/2023
---

# EKUListParams Complex Type

The **EKUListParams** complex type holds a list of EKUListPair elements.

```XML
<xs:complexType name="EKUListParams">
    <xs:sequence>
        <xs:element name="EKUMapInList" type="EKUListPair" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
    <xs:attribute name="Enabled" type="xs:boolean" use="optional" default="false"/>
</xs:complexType>
```

## Remarks

The **EKUListParams** element is optional.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eaptlsconnectionpropertiesv3](eaptlsconnectionpropertiesv3schema-schema.md)
- [eaptlsconnectionpropertiesv3 Complex Types](eaptlsconnectionpropertiesv3schema-complex-types.md)
- [Extensions (ExtensionParams)](eaptlsconnectionpropertiesv3schema-extensions-extensionparams-element.md)
