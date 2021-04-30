---
title: EnableIdentityPrivacy (IdentityPrivacyParameters) Element
description: Indicates whether a user's true identity or an anonymous identity is sent. | EnableIdentityPrivacy (IdentityPrivacyParameters) Element
ms.assetid: 7751e5fa-895e-47f7-99d9-aa7ef2451eb1
keywords:
- EnableIdentityPrivacy element EAPHost
topic_type:
- apiref
api_name:
- Username
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# EnableIdentityPrivacy (IdentityPrivacyParameters) Element

The **EnableIdentityPrivacy (IdentityPrivacyParameters)** element Indicates whether a user's true identity or an anonymous identity is sent.

``` syntax
<xs:element name="EnableIdentityPrivacy"
    type="xs:Boolean"
    minOccurs="0"
 />
```

The **EnableIdentityPrivacy** element is defined by the [IdentityPrivacyParameters](mspeapconnectionpropertiesv2-identityprivacyparameters-complextype.md) .

## Remarks

The **EnableIdentityPrivacy** element is optional.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[IdentityPrivacyParameters](mspeapconnectionpropertiesv2-identityprivacyparameters-complextype.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**PeapExtensions**](mspeapconnectionpropertiesv1schema-peapextensions-eaptype-element.md)
</dt> <dt>


</dt> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[mspeapconnectionpropertiesv2 Schema](mspeapconnectionpropertiesv2schema-schema.md)
</dt> <dt>

[mspeapconnectionpropertiesv2 Schema Elements](mspeapconnectionpropertiesv2schema-elements.md)
</dt> </dl>

 

 





