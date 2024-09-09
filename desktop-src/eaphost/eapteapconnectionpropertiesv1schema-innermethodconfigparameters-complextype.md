---
title: InnerMethodConfigParameters Complex Type
description: Learn about the InnerMethodConfigParameters complex type. This optional type specifies authentication information for EAP-TEAP.
ms.assetid: f289a967-be7e-4197-8534-a62bc44184c7
ms.topic: article
ms.date: 07/11/2023
---

# InnerMethodConfigParameters Complex Type

The **InnerMethodConfigParameters** complex type specifies the authentication information for EAP-TEAP.

```XML
<xs:complexType name="InnerMethodConfigParameters">
    <xs:sequence>
        <xs:element ref="baseEap:Eap" minOccurs="0" maxOccurs="1"/>
        <xs:element name="Parameters" type="InnerMethodParametersType" minOccurs="0" maxOccurs="1" />
    </xs:sequence>
</xs:complexType>
```

## Remarks

The **InnerMethodConfigParameters** element is optional.

*Eap* is an element of type **BaseEap** containing parameters for the inner EAP method.

*Parameters* is an element of type [InnerMethodParametersType](eapteapconnectionpropertiesv1schema-innermethodparameterstype-complextype.md) containing parameter information for the inner EAP method.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eapteapconnectionpropertiesv1 Schema](eapteapconnectionpropertiesv1schema-schema.md)
- [eapteapconnectionpropertiesv1 Complex Types](eapteapconnectionpropertiesv1schema-complex-types.md)
- [Phase2AuthenticationParameters](eapteapconnectionpropertiesv1schema-phase2authenticationparameters-complextype.md)
