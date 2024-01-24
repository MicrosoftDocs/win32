---
title: DisableUserPromptForServerValidation element (PEAP)
description: Learn about the DisableUserPromptForServerValidation (ServerValidationParameters) element. It indicates whether the user should be asked for server validation. | DisableUserPromptForServerValidation element (PEAP)
ms.assetid: ddb09888-731b-4c67-939e-9f0e6769408b
keywords:
- DisableUserPromptForServerValidation element EAPHost
topic_type:
- apiref
api_name:
- DisableUserPromptForServerValidation
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# DisableUserPromptForServerValidation (ServerValidationParameters) element (PEAP)

The **DisableUserPromptForServerValidation (ServerValidationParameters)** element indicates whether the user should be asked for server validation.

If **DisableUserPromptForServerValidation** is TRUE, then EAP-TLS performs the server validation without user input; if the validation fails, EAP-TLS fails the authentication. If **DisableUserPromptForServerValidation** is FALSE, the user is prompted for a validated server certificate or name, or root certificate authority (CA).

The **DisableUserPromptForServerValidation** element is optional.

``` syntax
<xs:element name="DisableUserPromptForServerValidation"
    type="boolean"
 />
```

The **DisableUserPromptForServerValidation** element is defined by the [**ServerValidationParameters**](mspeapconnectionpropertiesv1schema-servervalidationparameters-complextype.md) complex type.

## Requirements



| Role | Minimum supported OS version |
|------|------------------------------|
| Client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



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

 

 





