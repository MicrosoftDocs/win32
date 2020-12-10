---
title: CertificateStore (CredentialsSourceParameters) Element
description: Indicates that EAP-TLS should read the certificate from the user's My Store, or the machine being authenticated.
ms.assetid: 6b15c7cc-b686-4419-a962-e3dd6b4b84a6
keywords:
- CertificateStore element EAPHost
topic_type:
- apiref
api_name:
- CertificateStore
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# CertificateStore (CredentialsSourceParameters) Element

The **CertificateStore (CredentialsSourceParameters)** element indicates that EAP-TLS should read the certificate from the user's My Store, or the machine being authenticated.

``` syntax
<xs:element name="CertificateStore"
    type="CertSelection"
 />
```

The **CertificateStore** element is defined by the [**CredentialsSourceParameters**](eaptlsconnectionpropertiesv1schema-credentialssourceparameters-complextype.md) complex type.

## Remarks

The **CertificateStore** and [**SmartCard**](eaptlsconnectionpropertiesv1schema-smartcard-credentialssourceparameters-element.md) elements cannot both be used simultaneously.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**CredentialsSourceParameters**](eaptlsconnectionpropertiesv1schema-credentialssourceparameters-complextype.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**CredentialsSource (EapType)**](eaptlsconnectionpropertiesv1schema-credentialssource-eaptype-element.md)
</dt> <dt>


</dt> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[eaptlsconnectionpropertiesv1 Schema](eaptlsconnectionpropertiesv1schema-schema.md)
</dt> <dt>

[eaptlsconnectionpropertiesv1 Schema Elements](eaptlsconnectionpropertiesv1schema-elements.md)
</dt> </dl>

 

 





