---
title: MSCHAPv2AuthenticationParameters Complex Type
description: Learn about the MSCHAPv2AuthenticationParameters complex type. This optional type specifies additional authentication parameters for EAP-TTLS.
ms.assetid: efa72c9d-8f46-4253-8528-18b9fda0d7dd
ms.topic: article
ms.date: 07/10/2023
---

# MSCHAPv2AuthenticationParameters Complex Type

The **MSCHAPv2AuthenticationParameters** complex type specifies additional authentication parameters for EAP-TTLS.

```XML
<xs:complexType name="MSCHAPv2AuthenticationParameters">
    <xs:sequence>
        <xs:element name="UseWinlogonCredentials" type="xs:boolean" default="false" minOccurs="0"/>
    </xs:sequence>
</xs:complexType>
```

## Remarks

The **MSCHAPv2AuthenticationParameters** element is optional.

*UseWinlogonCredentials* is an optional Boolean element. If `TRUE`, MSCHAPv2 attempts to authenticate using the logged-on user's username and password. If `FALSE` or absent, it does not.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eapttlsconnectionpropertiesv1 Schema](eapttlsconnectionpropertiesv1schema-schema.md)
- [eapttlsconnectionpropertiesv1 Complex Types](eapttlsconnectionpropertiesv1schema-complex-types.md)
- [Phase2AuthenticationParameters](eapttlsconnectionpropertiesv1schema-phase2authenticationparameters-complextype.md)
