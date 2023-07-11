---
title: Phase1IdentityParameters Complex Type for EAP-TEAP
description: Learn about the Phase1IdentityParameters complex type. This optional type specifies identity parameters for EAP-TEAP.
ms.assetid: 74bbfa9d-7bcf-4893-9699-a65e40d3d570
ms.topic: article
ms.date: 07/11/2023
---

# Phase1IdentityParameters Complex Type for EAP-TEAP

The **Phase1IdentityParameters** complex type specifies the identity parameters for EAP-TEAP.

```XML
<xs:complexType name="Phase1IdentityParameters">
    <xs:sequence>
        <xs:element name="IdentityPrivacy" type="xs:boolean" default="true" minOccurs="0"/>
        <xs:element name="AnonymousIdentity" type="xs:string" minOccurs="0"/>
        <xs:any processContents="lax" minOccurs="0" maxOccurs="unbounded" namespace="##other"/>
    </xs:sequence>
</xs:complexType>
```

## Remarks

The **Phase1IdentityParameters** element is optional.

*IdentityPrivacy* is an optional Boolean that indicates whether identity privacy is enabled during Phase 1 of TEAP authentication when identity is sent as clear text. If `TRUE`, an anonymous identity is substituted for the user's true identity. The identity used is determined by the *AnonymousIdentity* element. If *AnonymousIdentity* is not specified, an empty string identity will be used.

*AnonymousIdentity* contains a Unicode string specifying an alternate identity used in place of a user's true identity. It is sent in the EAP identity response message during TEAP authentication. Anonymous identity usage is determined by the *IdentityPrivacy* element. If *IdentityPrivacy* is `FALSE`, *AnonymousIdentity* is ignored.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eapteapconnectionpropertiesv1 Schema](eapteapconnectionpropertiesv1schema-schema.md)
- [eapteapconnectionpropertiesv1 Complex Types](eapteapconnectionpropertiesv1schema-complex-types.md)
- [TeapConfig](eapteapconnectionpropertiesv1schema-teapconfig-complextype.md)
