---
title: Phase1IdentityParameters Complex Type
description: Learn about the Phase1IdentityParameters complex type. This optional type specifies identity parameters for EAP-TTLS.
ms.assetid: 221e5b93-0953-434f-a030-2c9bbffbca77
ms.topic: article
ms.date: 07/10/2023
---

# Phase1IdentityParameters Complex Type

The **Phase1IdentityParameters** complex type specifies the identity parameters for EAP-TTLS.

```XML
<xs:complexType name="Phase1IdentityParameters">
    <xs:sequence>
        <xs:element name="IdentityPrivacy" type="xs:boolean" default="true" minOccurs="0"/>
        <xs:element name="AnonymousIdentity" type="xs:string" minOccurs="0"/>
    </xs:sequence>
</xs:complexType>
```

## Remarks

The **Phase1IdentityParameters** element is optional.

*IdentityPrivacy* is an optional Boolean that indicates whether identity privacy is enabled. If `TRUE`, an anonymous identity is substituted for the user's true identity. The default value is `TRUE`.

*AnonymousIdentity* contains a Unicode string specifying an alternate identity used in place of a user's true identity. It is sent in the EAP identity response message during the TTLS authentication. Anonymous identity usage is determined by the *IdentityPrivacy* element.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eapttlsconnectionpropertiesv1 Schema](eapttlsconnectionpropertiesv1schema-schema.md)
- [eapttlsconnectionpropertiesv1 Complex Types](eapttlsconnectionpropertiesv1schema-complex-types.md)
- [TtlsConfig](eapttlsconnectionpropertiesv1schema-ttlsconfig-complextype.md)
