---
title: Phase2AuthenticationParameters Complex Type for EAP-TEAP
description: Learn about the Phase2AuthenticationParameters complex type. This optional type specifies authentication information for EAP-TEAP.
ms.assetid: 2f6b6e3c-0e6f-469d-9615-3f299993f225
ms.topic: article
ms.date: 07/11/2023
---

# Phase2AuthenticationParameters Complex Type for EAP-TEAP

The **Phase2AuthenticationParameters** complex type specifies the authentication information for EAP-TEAP.

```XML
<xs:complexType name="Phase2AuthenticationParameters">
    <xs:sequence>
        <xs:element name="InnerMethodConfig" type="InnerMethodConfigParameters"  minOccurs="0" maxOccurs="unbounded"/>
        <xs:any processContents="lax" minOccurs="0" maxOccurs="unbounded" namespace="##other"/>
    </xs:sequence>
</xs:complexType>
```

## Remarks

The **Phase2AuthenticationParameters** element is optional.

*InnerMethodConfig* is an element of type [InnerMethodConfigParameters](eapteapconnectionpropertiesv1schema-innermethodconfigparameters-complextype.md) containing parameters for the inner EAP method.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eapttlsconnectionpropertiesv1 Schema](eapteapconnectionpropertiesv1schema-schema.md)
- [eapttlsconnectionpropertiesv1 Complex Types](eapteapconnectionpropertiesv1schema-complex-types.md)
- [TeapConfig](eapteapconnectionpropertiesv1schema-teapconfig-complextype.md)
