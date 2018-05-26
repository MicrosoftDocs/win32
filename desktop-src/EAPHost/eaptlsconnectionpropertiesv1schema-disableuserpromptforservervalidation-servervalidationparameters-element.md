---
title: DisableUserPromptForServerValidation (ServerValidationParameters) Element
description: Indicates whether the user should be asked for server validation.
ms.assetid: d1c2f334-286b-4aac-b723-806b90fc7b1f
keywords:
- DisableUserPromptForServerValidation element EAPHost
topic_type:
- apiref
api_name:
- DisableUserPromptForServerValidation
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DisableUserPromptForServerValidation (ServerValidationParameters) Element

The **DisableUserPromptForServerValidation (ServerValidationParameters)** element indicates whether the user should be asked for server validation.

If **DisableUserPromptForServerValidation** is TRUE, then EAP-TLS performs the server validation without user input; if the validation fails, EAP-TLS fails the authentication. If **DisableUserPromptForServerValidation** is FALSE, the user is prompted for a validated server certificate or name, or root certificate authority (CA).

The **DisableUserPromptForServerValidation** element is optional.

``` syntax
<xs:element name="DisableUserPromptForServerValidation"
    type="boolean"
 />
```

The **DisableUserPromptForServerValidation** element is defined by the [**ServerValidationParameters**](eaptlsconnectionpropertiesv1schema-servervalidationparameters-complextype.md) complex type.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**ServerValidationParameters**](eaptlsconnectionpropertiesv1schema-servervalidationparameters-complextype.md)
</dt> <dt>

**Possible immediate parent elements in schema instance**
</dt> <dt>

[**ServerValidation (EapType)**](eaptlsconnectionpropertiesv1schema-servervalidation-eaptype-element.md)
</dt> <dt>


</dt> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[eaptlsconnectionpropertiesv1 Schema](eaptlsconnectionpropertiesv1schema-schema.md)
</dt> <dt>

[eaptlsconnectionpropertiesv1 Schema Elements](eaptlsconnectionpropertiesv1schema-elements.md)
</dt> </dl>

 

 





