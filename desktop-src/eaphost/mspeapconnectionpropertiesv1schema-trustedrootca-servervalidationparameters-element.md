---
title: TrustedRootCA (ServerValidationParameters) Element (v1)
description: Captures the thumb print of root certificate authorities (CAs) that are trusted by the client. | TrustedRootCA (ServerValidationParameters) Element
ms.assetid: f0485dcc-8610-4c5b-b4db-6f2a77057489
keywords:
- TrustedRootCA element EAPHost
topic_type:
- apiref
api_name:
- TrustedRootCA
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# TrustedRootCA (ServerValidationParameters) Element

The **TrustedRootCA (ServerValidationParameters)** element element captures the thumb print of root certificate authorities (CAs) that are trusted by the client.

``` syntax
<xs:element name="TrustedRootCA"
    type="hexBinary"
 />
```

The **TrustedRootCA** element is defined by the [**ServerValidationParameters**](mspeapconnectionpropertiesv1schema-servervalidationparameters-complextype.md) complex type.

## Remarks

The thumb print is a hexadecimal string that contains the SHA-1 hash of the certificate. The **TrustedRootCA** element is optional.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**ServerValidationParameters**](mspeapconnectionpropertiesv1schema-servervalidationparameters-complextype.md)
</dt> <dt>

**Possible immediate parent elements in schema instance**
</dt> <dt>

[**ServerValidation (EapType)**](mspeapconnectionpropertiesv1schema-servervalidation-eaptype-element.md)
</dt> <dt>


</dt> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[mspeapconnectionpropertiesv1 Schema](mspeapconnectionpropertiesv1schema-schema.md)
</dt> <dt>

[mspeapconnectionpropertiesv1 Schema Elements](mspeapconnectionpropertiesv1schema-elements.md)
</dt> </dl>

 

 





