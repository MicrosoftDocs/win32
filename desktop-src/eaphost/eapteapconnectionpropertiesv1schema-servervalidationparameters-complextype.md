---
title: ServerValidationParameters Complex Type for EAP-TEAP
description: Learn about the ServerValidationParameters complex type. This optional type specifies server information for EAP-TEAP.
ms.assetid: 6688b699-d96f-416e-bb20-b9e77f06a6aa
ms.topic: article
ms.date: 07/11/2023
---

# ServerValidationParameters Complex Type for EAP-TEAP

The **ServerValidationParameters** complex type specifies the server information for EAP-TEAP.

```XML
<xs:complexType name="ServerValidationParameters">
    <xs:sequence>
        <xs:element name="ServerNames" type="xs:string" minOccurs="0"/>
        <xs:element name="TrustedRootCAHash" type="xs:hexBinary" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="DownloadTrustedServerRoot" type="xs:boolean" default="false" minOccurs="0"/>
        <xs:element name="DisablePrompt" type="xs:boolean" default="false" minOccurs="0" />
        <xs:any processContents="lax" minOccurs="0" maxOccurs="unbounded" namespace="##other"/>
    </xs:sequence>
</xs:complexType>
```

## Remarks

The **ServerValidationParameters** element is optional.

*ServerNames* is an optional string that specifies the list of servers to which the client can authenticate.

*TrustedRootCAHash* is the thumbprint of a root certification authority that is trusted to issue server certificates, represented as a hexadecimal string of the certificate's [SHA256](https://go.microsoft.com/fwlink/?LinkId=90514) hash. Zero or more elements can be present.

*DownloadTrustedServerRoot* is an optional Boolean that specifies method behavior in case the server's certificate is not trusted and the user manually accepts the certificate. If `TRUE`, additional server certificates pushed by the server will be added to the **TrustedRootCAHash** element after a successful connection. If `FALSE`, no additional certificates pushed by the server will be added to the **TrustedRootCAHash** element.

*DisablePrompt* is an optional Boolean that specifies method behavior in case the server's certificate is not trusted as per the TEAP connection profile. If `TRUE`, certificate errors will cause the connection to be refused. If `FALSE`, the user is prompted to manually accept or reject the certificate.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eapteapconnectionpropertiesv1 Schema](eapteapconnectionpropertiesv1schema-schema.md)
- [eapteapconnectionpropertiesv1 Complex Types](eapteapconnectionpropertiesv1schema-complex-types.md)
- [TeapConfig](eapteapconnectionpropertiesv1schema-teapconfig-complextype.md)
