---
title: EKUListParams Complex Type
description: Learn about the EKUListParams complex type. This type holds a list of EKUListPair elements for specifying the EKUs to be used for filtering certificates on the client.
ms.assetid: 46d713b9-6701-4f70-bcff-305c2f613220
ms.topic: article
ms.date: 07/07/2023
---

# EKUListParams Complex Type

The **EKUListParams** complex type holds a list of [EKUListPair](eaptlsconnectionpropertiesv3schema-ekulistpair-complextype.md) elements for specifying the EKUs to be used for filtering certificates on the client.

```XML
<xs:complexType name="EKUListParams">
    <xs:sequence>
        <xs:element name="EKUMapInList" type="EKUListPair" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
    <xs:attribute name="Enabled" type="xs:boolean" use="optional" default="false"/>
</xs:complexType>
```

## Remarks

The **EKUListParams** element is optional.

The *EKUMapInList* element can be present multiple times, indicating multiple EKUs. The EKUMapping element is an element of type **EKUListPair**.

The *Enabled* parameter indicates whether the certificates on the client are to be filtered based on the EKU list as specified by one or more *EKUMapInList* elements. If set to `TRUE`, certificates are filtered based on the specified EKU list. If set to `FALSE`, certificate filtering is not done based on the EKU list.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eaptlsconnectionpropertiesv3](eaptlsconnectionpropertiesv3schema-schema.md)
- [eaptlsconnectionpropertiesv3 Complex Types](eaptlsconnectionpropertiesv3schema-complex-types.md)
- [Extensions (ExtensionParams)](eaptlsconnectionpropertiesv3schema-extensions-extensionparams-element.md)
