---
title: ExtensionParams Complex Type
description: Learn about the ExtensionParams complex type. This type enables future enhancements to the schema.
ms.assetid: 19917856-930a-4521-9929-4e086116017b
ms.topic: article
ms.date: 07/07/2023
---

# ExtensionParams Complex Type

The **ExtensionParams** complex type enables future enhancements to the schema.

```XML
<xs:complexType name="ExtensionParams">
    <xs:sequence>
        <xs:any processContents="lax" minOccurs="0" maxOccurs="unbounded" namespace="##any"/>
    </xs:sequence>
</xs:complexType>
```

## Remarks

The **ExtensionParams** element is optional.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eaptlsconnectionpropertiesv3](eaptlsconnectionpropertiesv3schema-schema.md)
- [eaptlsconnectionpropertiesv3 Complex Types](eaptlsconnectionpropertiesv3schema-complex-types.md)
- [Extensions (ExtensionParams)](eaptlsconnectionpropertiesv3schema-extensions-extensionparams-element.md)
