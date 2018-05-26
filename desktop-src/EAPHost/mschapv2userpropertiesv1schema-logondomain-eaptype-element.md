---
title: LogonDomain (EapType) Element
description: Identifies the domain of the user or machine being authenticated.
ms.assetid: a93793cd-29ee-47f9-8d91-895844c08bae
keywords:
- LogonDomain element EAPHost
topic_type:
- apiref
api_name:
- LogonDomain
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



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

 

 





