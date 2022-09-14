---
title: DifferentUsername (EapType) Element
description: Learn about the DifferentUsername (EapType) element. This element determines which user name EAP-TLS is to use.
ms.assetid: f0ce41a9-c774-4d12-8a5a-a8eb1eb84cb0
keywords:
- DifferentUsername element EAPHost
topic_type:
- apiref
api_name:
- DifferentUsername
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# DifferentUsername (EapType) Element

The **DifferentUsername (EapType)** element determines which user name EAP-TLS is to use.

``` syntax
<xs:element name="DifferentUsername"
    type="boolean"
 />
```

The **DifferentUsername** element is defined by the [**EapType**](eaptlsconnectionpropertiesv1schema-eaptype-element.md) element.

## Remarks

If the **DifferentUserName** element is TRUE, EAP-TLS should use a user name other than the name that appears on the certificate. If the **DifferentUserName** element is FALSE, EAP-TLS uses the user name that appears on the certificate.

The **DifferentUserName** element is optional.

## Requirements



| Role | Minimum supported OS version |
|------|------------------------------|
| Client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**EapType**](eaptlsconnectionpropertiesv1schema-eaptype-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**EapType**](eaptlsconnectionpropertiesv1schema-eaptype-element.md)
</dt> <dt>


</dt> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[eaptlsconnectionpropertiesv1 Schema](eaptlsconnectionpropertiesv1schema-schema.md)
</dt> <dt>

[eaptlsconnectionpropertiesv1 Schema Elements](eaptlsconnectionpropertiesv1schema-elements.md)
</dt> </dl>

 

 





