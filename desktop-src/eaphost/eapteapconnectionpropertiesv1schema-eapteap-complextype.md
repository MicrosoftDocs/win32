---
title: EapTeap Complex Type
description: Learn about the EapTeap complex type. This type contains the EAP configuration required for EAP-TEAP.
ms.assetid: 8a9b7cda-0e12-4866-93b2-bed4102db091
ms.topic: article
ms.date: 07/11/2023
---

# EapTeap Complex Type

The **EapTeap** complex type contains the EAP configuration required for EAP-TEAP.

```XML
<xs:complexType name="EapTeap">
    <xs:complexContent>
        <xs:extension base="TeapConfig"/>
    </xs:complexContent>
</xs:complexType>
```

## Remarks

The **EapTeap** element is required.

The configuration content, defined by [TeapConfig](eapteapconnectionpropertiesv1schema-teapconfig-complextype.md), specifies the EAP configuration required for EAP-TEAP.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eapteapconnectionpropertiesv1 Schema](eapteapconnectionpropertiesv1schema-schema.md)
- [eapteapconnectionpropertiesv1 Complex Types](eapteapconnectionpropertiesv1schema-complex-types.md)
- [eapTeap (EapTeap)](eapteapconnectionpropertiesv1schema-eapteap-eapteap-element.md)
