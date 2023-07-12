---
title: TeapConfig Complex Type
description: Learn about the TeapConfig complex type. This type specifies the EAP configuration required for EAP-TEAP.
ms.assetid: 8ecec9a0-7872-4b7c-8132-bbedc7af6f11
ms.topic: article
ms.date: 07/11/2023
---

# TeapConfig Complex Type

The **TeapConfig** complex type specifies the EAP configuration required for EAP-TEAP as specified in [RFC7170](https://go.microsoft.com/fwlink/?linkid=2116542).

```XML
<xs:complexType name="TeapConfig">
    <xs:sequence>
        <xs:element name="ServerValidation" type="ServerValidationParameters" minOccurs="0"/>
        <xs:element name="Phase2Authentication" type="Phase2AuthenticationParameters" minOccurs="0"/>
        <xs:element name="Phase1Identity"  type="Phase1IdentityParameters" minOccurs="0"/>
        <xs:any processContents="lax" minOccurs="0" maxOccurs="unbounded" namespace="##other"/>
    </xs:sequence>
</xs:complexType>
```

## Remarks

The **TeapConfig** element is required.

*ServerValidation* is an optional element of type [ServerValidationParameters](eapteapconnectionpropertiesv1schema-servervalidationparameters-complextype.md).

*Phase2Authentication* is an optional element of the [Phase2AuthenticationParameters](eapteapconnectionpropertiesv1schema-phase2authenticationparameters-complextype.md) type.

*Phase1Identity* is an optional element of [Phase1IdentityParameters](eapteapconnectionpropertiesv1schema-phase1identityparameters-complextype.md) type.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eapteapconnectionpropertiesv1 Schema](eapteapconnectionpropertiesv1schema-schema.md)
- [eapteapconnectionpropertiesv1 Complex Types](eapteapconnectionpropertiesv1schema-complex-types.md)
- [EapTeap](eapteapconnectionpropertiesv1schema-eapteap-complextype.md)
