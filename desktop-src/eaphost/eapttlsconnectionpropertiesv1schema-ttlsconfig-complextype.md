---
title: TtlsConfig Complex Type
description: Learn about the TtlsConfig complex type. This type specifies the EAP configuration required for EAP-TTLS.
ms.assetid: 901d9342-3fb6-4872-9278-06099c5a64c9
ms.topic: article
ms.date: 07/10/2023
---

# TtlsConfig Complex Type

The **TtlsConfig** complex type specifies the EAP configuration required for EAP-TTLS as specified in [RFC5281](https://go.microsoft.com/fwlink/?LinkId=225924).

```XML
<xs:complexType name="TtlsConfig">
    <xs:sequence>
        <xs:element name="ServerValidation" type="ServerValidationParameters" minOccurs="0"/>
        <xs:element name="Phase2Authentication" type="Phase2AuthenticationParameters" minOccurs="0"/>
        <xs:element name="Phase1Identity"  type="Phase1IdentityParameters" minOccurs="0"/>
    </xs:sequence>
</xs:complexType>
```

## Remarks

The **TtlsConfig** element is required.

*ServerValidation* is an optional element of type [ServerValidationParameters](eapttlsconnectionpropertiesv1schema-servervalidationparameters-complextype.md).

*Phase2Authentication* is an optional element of the [Phase2AuthenticationParameters](eapttlsconnectionpropertiesv1schema-phase2authenticationparameters-complextype.md) type.

*Phase1Identity* is an optional element of [Phase1IdentityParameters](eapttlsconnectionpropertiesv1schema-phase1identityparameters-complextype.md) type.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eapttlsconnectionpropertiesv1 Schema](eapttlsconnectionpropertiesv1schema-schema.md)
- [eapttlsconnectionpropertiesv1 Complex Types](eapttlsconnectionpropertiesv1schema-complex-types.md)
- [EapTtls](eapttlsconnectionpropertiesv1schema-eapttls-complextype.md)
