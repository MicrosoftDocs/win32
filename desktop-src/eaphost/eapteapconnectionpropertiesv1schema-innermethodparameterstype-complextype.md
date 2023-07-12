---
title: InnerMethodParametersType Complex Type
description: Learn about the InnerMethodParametersType complex type. This optional type specifies parameter information for EAP-TEAP.
ms.assetid: 51187304-acfa-4c23-9687-674ad89915b6
ms.topic: article
ms.date: 07/11/2023
---

# InnerMethodParametersType Complex Type

The **InnerMethodParametersType** complex type specifies the parameter information for EAP-TEAP.

```XML
<xs:complexType name="InnerMethodParametersType">
    <xs:sequence>
        <xs:any processContents="lax" minOccurs="0" maxOccurs="unbounded" namespace="##other"/>
    </xs:sequence>
</xs:complexType>
```

## Remarks

The **InnerMethodParametersType** element is optional.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eapteapconnectionpropertiesv1 Schema](eapteapconnectionpropertiesv1schema-schema.md)
- [eapteapconnectionpropertiesv1 Complex Types](eapteapconnectionpropertiesv1schema-complex-types.md)
- [InnerMethodConfigParameters](eapteapconnectionpropertiesv1schema-innermethodconfigparameters-complextype.md)
