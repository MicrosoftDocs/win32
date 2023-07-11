---
title: Phase2AuthenticationParameters Complex Type
description: Learn about the Phase2AuthenticationParameters complex type. This optional type specifies authentication information for EAP-TTLS.
ms.assetid: dfd01f68-831b-439f-b3e7-99b115997557
ms.topic: article
ms.date: 07/10/2023
---

# Phase2AuthenticationParameters Complex Type

The **Phase2AuthenticationParameters** complex type specifies the authentication information for EAP-TTLS.

```XML
<xs:complexType name="Phase2AuthenticationParameters">
    <xs:sequence>
        <xs:choice>
            <xs:element ref="baseEap:Eap" minOccurs="0" maxOccurs="unbounded"/>
            <xs:element name="PAPAuthentication" type="emptyString" minOccurs="0"/>
            <xs:element name="CHAPAuthentication" type="emptyString" minOccurs="0"/>
            <xs:element name="MSCHAPAuthentication" type="emptyString" minOccurs="0"/>
            <xs:element name="MSCHAPv2Authentication" type="MSCHAPv2AuthenticationParameters" minOccurs="0"/>
        </xs:choice>
    </xs:sequence>
</xs:complexType>
```

## Remarks

The **Phase2AuthenticationParameters** element is optional.

*Eap* is an element of type **BaseEap** containing parameters for the inner EAP method.

*PAPAuthentication* is an empty string whose presence indicates that TTLS will attempt PAP authentication protocol after the phase 1 tunnel is established.

*CHAPAuthentication* is an empty string whose presence indicates that TTLS will attempt CHAP authentication protocol after the phase 1 tunnel is established.

*MSCHAPAuthentication* is an empty string whose presence indicates that TTLS will attempt MSCHAP authentication protocol after the phase 1 tunnel is established.

*MSCHAPv2Authentication* is an element of [MSCHAPv2AuthenticationParameters](eapttlsconnectionpropertiesv1schema-mschapv2authenticationparameters-complextype.md) type whose presence indicates that TTLS will attempt MSCHAPv2 authentication protocol after the phase 1 tunnel is established. The **MSCHAPv2AuthenticationParameters** type is a complex element.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eapttlsconnectionpropertiesv1 Schema](eapttlsconnectionpropertiesv1schema-schema.md)
- [eapttlsconnectionpropertiesv1 Complex Types](eapttlsconnectionpropertiesv1schema-complex-types.md)
- [TtlsConfig](eapttlsconnectionpropertiesv1schema-ttlsconfig-complextype.md)
