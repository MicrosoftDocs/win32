---
title: Password (EapType) Element
description: Learn about the Password (EapType) element. This element identifies the password of the user or machine being authenticated.
ms.assetid: d3ad95b8-2d98-420f-a680-a83b49ae2992
keywords:
- Password element EAPHost
topic_type:
- apiref
api_name:
- Password
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# Password (EapType) Element

The **Password (EapType)** element identifies the password of the user or machine being authenticated.

``` syntax
<xs:element name="Password"
    type="string"
 />
```

The **Password** element is defined by the [**EapType**](mschapv2userpropertiesv1schema-eaptype-element.md) element.

## Remarks

If the **Password (EapType)** element is not present, the password hash is obtained from winlogon. This element is optional.

## Requirements



| Role | Minimum supported OS version |
|------|------------------------------|
| Client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**EapType**](mschapv2userpropertiesv1schema-eaptype-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**EapType**](mschapv2userpropertiesv1schema-eaptype-element.md)
</dt> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[mschapv2userpropertiesv1 Schema](mschapv2userpropertiesv1schema-schema.md)
</dt> </dl>

 

 





