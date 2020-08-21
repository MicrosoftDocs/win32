---
title: SimpleCertSelection (CertSelection) Element
description: Learn about the SimpleCertSelection (CertSelection) element. This element determines how the user selects a certificate.
ms.assetid: 28454877-fd07-4b47-9544-f2b4e91c6651
keywords:
- SimpleCertSelection element EAPHost
topic_type:
- apiref
api_name:
- SimpleCertSelection
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# SimpleCertSelection (CertSelection) Element

The **SimpleCertSelection (CertSelection)** element determines how the user selects a certificate.

``` syntax
<xs:element name="SimpleCertSelection"
    type="boolean"
 />
```

The **SimpleCertSelection** element is defined by the [**CertSelection**](eaptlsconnectionpropertiesv1schema-certselection-complextype.md) complex type.

## Remarks

**SimpleCertSelection** is TRUE by default. If **SimpleCertSelection** is TRUE, EAP-TLS performs a simple certificate search without any drop-down lists for the selection of certificates. If **SimpleCertSelection** is FALSE, EAP-TLS illustrates to the user the suitable certificate to be selected.

## Requirements



| Role | Minimum supported OS |
|------|----------------------|
| Client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**CertSelection**](eaptlsconnectionpropertiesv1schema-certselection-complextype.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**CertificateStore (CredentialsSourceParameters)**](eaptlsconnectionpropertiesv1schema-certificatestore-credentialssourceparameters-element.md)
</dt> <dt>


</dt> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[eaptlsconnectionpropertiesv1 Schema](eaptlsconnectionpropertiesv1schema-schema.md)
</dt> <dt>

[eaptlsconnectionpropertiesv1 Schema Elements](eaptlsconnectionpropertiesv1schema-elements.md)
</dt> </dl>

 

 





