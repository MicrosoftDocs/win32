---
title: LogonDomain (EapType) Element
description: Learn about the LogonDomain (EapType) element. This element identifies the domain of the user or machine being authenticated.
ms.assetid: a93793cd-29ee-47f9-8d91-895844c08bae
keywords:
- LogonDomain element EAPHost
topic_type:
- apiref
api_name:
- LogonDomain
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# LogonDomain (EapType) Element

The**LogonDomain (EapType)** element identifies the domain of the user or machine being authenticated.

``` syntax
<xs:element name="LogonDomain
          
        "
    type="string"
 />
```

The **LogonDomain** element is defined by the [**EapType**](mschapv2userpropertiesv1schema-eaptype-element.md) element.

## Remarks

If the **LogonDomain (EapType)** element is not present, the domain from winlogon is used. This element is optional.

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

 

 





