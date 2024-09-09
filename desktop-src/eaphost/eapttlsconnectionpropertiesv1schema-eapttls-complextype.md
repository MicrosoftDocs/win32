---
title: EapTtls Complex Type
description: Learn about the EapTtls complex type. This type contains the EAP configuration required for EAP-TTLS.
ms.assetid: e1380c07-95c4-4d32-b846-35d0e9b0d96d
ms.topic: article
ms.date: 07/10/2023
---

# EapTtls Complex Type

The **EapTtls** complex type contains the EAP configuration required for EAP-TTLS.

```XML
<xs:complexType name="EapTtls">
    <xs:complexContent>
        <xs:extension base="TtlsConfig"/>
    </xs:complexContent>
</xs:complexType>
```

## Remarks

The **EapTtls** element is required.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eapttlsconnectionpropertiesv1 Schema](eapttlsconnectionpropertiesv1schema-schema.md)
- [eapttlsconnectionpropertiesv1 Complex Types](eapttlsconnectionpropertiesv1schema-complex-types.md)
- [eapTtls (EapTtls)](eapttlsconnectionpropertiesv1schema-eapttls-eapttls-element.md)
