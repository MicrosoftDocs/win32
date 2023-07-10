---
title: CAHashListParams Complex Type
description: Learn about the CAHashListParams complex type. This type holds a list of certificate authority issuer hashes.
ms.assetid: 5310fcb4-49c1-4da3-ab4e-33ef79d17be8
ms.topic: article
ms.date: 07/07/2023
---

# CAHashListParams Complex Type

The **CAHashListParams** complex type holds a list of certificate authority issuer hashes.

```XML
<xs:complexType name="CAHashListParams">
    <xs:sequence>
        <xs:element name="IssuerHash" type="xs:hexBinary" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
    <xs:attribute name="Enabled" type="xs:boolean" use="optional" default="false"/>
</xs:complexType>
```

## Remarks

The **CAHashListParams** element is optional.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eaptlsconnectionpropertiesv3](eaptlsconnectionpropertiesv3schema-schema.md)
- [eaptlsconnectionpropertiesv3 Complex Types](eaptlsconnectionpropertiesv3schema-complex-types.md)
- [Extensions (ExtensionParams)](eaptlsconnectionpropertiesv3schema-extensions-extensionparams-element.md)
