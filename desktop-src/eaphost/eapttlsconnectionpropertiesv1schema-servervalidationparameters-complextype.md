---
title: ServerValidationParameters Complex Type
description: Learn about the ServerValidationParameters complex type. This optional type specifies server information for EAP-TTLS.
ms.assetid: 41f5d116-2df3-49b6-b48f-227e412455fa
ms.topic: article
ms.date: 07/10/2023
---

# ServerValidationParameters Complex Type

The **ServerValidationParameters** complex type specifies the server information for EAP-TTLS.

```XML
<xs:complexType name="ServerValidationParameters">
    <xs:sequence>
        <xs:element name="ServerNames" type="xs:string" minOccurs="0"/>
        <xs:element name="TrustedRootCAHashes" type="xs:hexBinary" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="DisablePrompt" type="xs:boolean" default="false" minOccurs="0"/>
    </xs:sequence>
</xs:complexType>
```

## Remarks

The **ServerValidationParameters** element is optional.

*ServerNames* is an optional string that specifies the list of servers to which the client can authenticate.

*TrustedRootCAHashes* is the thumbprint of a root certification authority that is trusted to issue server certificates, represented as a hexadecimal string of the certificate's SHA-1 hash. Zero or more elements can be present.

*DisablePrompt* is an optional Boolean that specifies method behavior in case the server's certificate is not trusted as per the TTLS connection profile. If `TRUE`, certificate errors will cause the connection to be refused. If `FALSE`, the user is prompted to manually accept or reject the certificate.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eapttlsconnectionpropertiesv1 Schema](eapttlsconnectionpropertiesv1schema-schema.md)
- [eapttlsconnectionpropertiesv1 Complex Types](eapttlsconnectionpropertiesv1schema-complex-types.md)
- [TtlsConfig](eapttlsconnectionpropertiesv1schema-ttlsconfig-complextype.md)
