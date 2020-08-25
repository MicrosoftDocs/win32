---
title: CertSelection Complex Type
description: Learn about the CertSelection complex type. This type determines how the user selects a certificate.
ms.assetid: f5a37258-8ab0-4736-9721-6c2800769c74
keywords:
- CertSelection complex type EAPHost
topic_type:
- apiref
api_name:
- CertSelection
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# CertSelection Complex Type

The **CertSelection** complex type determines how the user selects a certificate.

``` syntax
<xs:complexType name="CertSelection">
    <xs:sequence>
        <xs:element name="SimpleCertSelection"
            type="boolean"
            minOccurs="0"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                                                                                                     | Type    | Description                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SimpleCertSelection**](eaptlsconnectionpropertiesv1schema-simplecertselection-certselection-element.md) | boolean | Is TRUE by default. If [**SimpleCertSelection**](eaptlsconnectionpropertiesv1schema-simplecertselection-certselection-element.md) is TRUE, EAP-TLS performs a simple certificate search without any drop-down lists for the selection of certificates. If **SimpleCertSelection** is FALSE, EAP-TLS illustrates to the user the suitable certificate to be selected.<br/> |



## Requirements



| Role | Minimum supported OS version |
|------|------------------------------|
| Client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[eaptlsconnectionpropertiesv1 Schema](eaptlsconnectionpropertiesv1schema-schema.md)
</dt> <dt>

[eaptlsconnectionpropertiesv1 Schema Complex Types](eaptlsconnectionpropertiesv1schema-complex-types.md)
</dt> </dl>

 

 





