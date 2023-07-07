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

## See also

- [EAPHost and Legacy Schema](eaphost-schemas.md)
- [eaptlsconnectionpropertiesv3](eaptlsconnectionpropertiesv3schema-schema.md)
- [eaptlsconnectionpropertiesv3 Complex Types](eaptlsconnectionpropertiesv3schema-complex-types.md)
- [FilteringInfo (FilterInfoParams)](eaptlsconnectionpropertiesv3schema-filteringinfo-filterinfoparams-element.md)
