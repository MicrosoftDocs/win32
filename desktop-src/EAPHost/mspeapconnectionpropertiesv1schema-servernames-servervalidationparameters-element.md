---
title: ServerNames (ServerValidationParameters) Element
description: Represents a list of semicolon delimited server names.
ms.assetid: 2595daa1-9f1b-40cf-9219-0e7295fdd5c3
keywords:
- ServerNames element EAPHost
topic_type:
- apiref
api_name:
- ServerNames
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ServerNames (ServerValidationParameters) Element

The **ServerNames (ServerValidationParameters)** element represents a list of semicolon delimited server names.

``` syntax
<xs:element name="ServerNames"
    type="string"
    minOccurs="0"
 />
```

The **ServerNames** element is defined by the [**ServerValidationParameters**](mspeapconnectionpropertiesv1schema-servervalidationparameters-complextype.md) complex type.

## Remarks

Each server name is delimited by semicolons, and can be represented by regular expressions. The **ServerNames** element is optional.

## Requirements



|                                     |                                                      |
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

 

 





