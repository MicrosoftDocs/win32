---
title: CAHashListParams Complex Type
description: Learn about the CAHashListParams complex type. This type holds a list of certificate authority issuer hashes.
ms.assetid: 5310fcb4-49c1-4da3-ab4e-33ef79d17be8
ms.topic: article
ms.date: 07/07/2023
---

# CAHashListParams Complex Type

The **CAHashListParams** complex type holds a list of certificate authority issuer hashes.

```XML
<xs:complexType name="CAHashListParams">
    <xs:sequence>
        <xs:element name="IssuerHash" type="xs:hexBinary" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
    <xs:attribute name="Enabled" type="xs:boolean" use="optional" default="false"/>
</xs:complexType>
```

## Remarks

The **CAHashListParams** element is optional.

*IssuerHash* is the thumbprint of a root certification authority that issues certificates that can be allowed on a client for authentication. It is represented as the hexadecimal encoding of the SHA-1 hash of the certificate. It is optional, but multiple such elements can be present.

*Enabled* indicates whether the certificates on the client are to be filtered based on the CA hash as specified by one or more *IssuerHash* elements. If set to `TRUE`, certificates are filtered based on specified CAs. If set to `FALSE` (default), certificate filtering is not done based on CAs.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eaptlsconnectionpropertiesv3](eaptlsconnectionpropertiesv3schema-schema.md)
- [eaptlsconnectionpropertiesv3 Complex Types](eaptlsconnectionpropertiesv3schema-complex-types.md)
- [Extensions (ExtensionParams)](eaptlsconnectionpropertiesv3schema-extensions-extensionparams-element.md)
