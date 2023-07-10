---
title: FilterInfoParams Complex Type
description: Learn about the FilterInfoParams complex type. This type enables future enhancements to the schema.
ms.assetid: ff133035-cbbf-4c52-bc40-e3cbce7de309
ms.topic: article
ms.date: 07/07/2023
---

# FilterInfoParams Complex Type

The **FilterInfoParams** complex type enables future enhancements to the schema.

```XML
<xs:complexType name="FilterInfoParams">
    <xs:sequence>
        <xs:element name="AllPurposeEnabled" type="xs:boolean" minOccurs="0" maxOccurs="1"/>
        <xs:element name="CAHashList" type="CAHashListParams" minOccurs="0" maxOccurs="1"/>
        <xs:element name="EKUMapping" type="EKUMapParams" minOccurs="0" maxOccurs="1"/>
        <xs:element name="ClientAuthEKUList" type="EKUListParams" minOccurs="0" maxOccurs="1"/>
        <xs:element name="AnyPurposeEKUList" type="EKUListParams" minOccurs="0" maxOccurs="1"/>
    </xs:sequence>
</xs:complexType>
```

## Remarks

The **FilterInfoParams** element is optional.

*AllPurposeEnabled* is an optional Boolean that indicates whether all-purpose certificates are allowed for authentication on the client. If set to `TRUE`, all-purpose certificates are allowed. If set to `FALSE` or not set, all-purpose certificates are not allowed.

*CAHashList* is an element of type [CAHashListParams](eaptlsconnectionpropertiesv3schema-cahashlistparams-complextype.md) containing one or more issuer hashes (thumbprints of a root certification authority that issues certificates that can be allowed on a client for authentication).

*EKUMapping* is an optional element of type [EKUMapParams](eaptlsconnectionpropertiesv3schema-ekumapparams-complextype.md) that contains EKU Name and OID mapping(s).

*ClientAuthEKUList* is an optional element of type [EKUListParams](eaptlsconnectionpropertiesv3schema-ekulistparams-complextype.md) for specifying the EKUs to be used for filtering certificates on the client.

*AnyPurposeEKUList* is an optional element of type **EKUListParams** for specifying EKUs.

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eaptlsconnectionpropertiesv3](eaptlsconnectionpropertiesv3schema-schema.md)
- [eaptlsconnectionpropertiesv3 Complex Types](eaptlsconnectionpropertiesv3schema-complex-types.md)
- [FilteringInfo (FilterInfoParams)](eaptlsconnectionpropertiesv3schema-filteringinfo-filterinfoparams-element.md)
