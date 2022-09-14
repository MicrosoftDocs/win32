---
title: AnonymousUserName (IdentityPrivacyParameters) Element
description: Contains an anonymous identity used in place of a user's true identify. It is sent during the 1st Phase of PEAP authentication when Identity is sent as plain text.
ms.assetid: 74a33a75-cf21-4346-a984-f2f8564c3b57
keywords:
- AnonymousUserName element EAPHost
topic_type:
- apiref
api_name:
- Username
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# AnonymousUserName (IdentityPrivacyParameters) Element

The **AnonymousUserName (IdentityPrivacyParameters)** element contains an anonymous identity used in place of a user's true identify. It is sent during the 1st Phase of PEAP authentication when **Identity** is sent as plain text.

Anonymous identity usage is determined by the [**EnableIdentityPrivacy**](mspeapconnectionpropertiesv2-enableidentityprivacy-identityprivacyparameters-element.md) element.

``` syntax
<xs:element name="AnonymousUserName"
    type="xs:String"
    minOccurs="0"
 />
```

The **AnonymousUserName** element is defined by the [IdentityPrivacyParameters](mspeapconnectionpropertiesv2-identityprivacyparameters-complextype.md) .

## Remarks

The **AnonymousUserName** element is optional.

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

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[mspeapconnectionpropertiesv2 Schema](mspeapconnectionpropertiesv2schema-schema.md)
</dt> <dt>

[mspeapconnectionpropertiesv2 Schema Elements](mspeapconnectionpropertiesv2schema-elements.md)
</dt> </dl>

 

 





