---
title: EapType element (base user properties)
description: Learn about the EapType element. This element captures method-specific configuration inside the Eap element. | EapType element (base user properties)
ms.assetid: 8ce81848-5b36-441f-967d-02c666ba5c6c
keywords:
- EapType element EAPHost
topic_type:
- apiref
api_name:
- EapType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# EapType element (base user properties)

The **EapType** element captures method-specific configuration inside the Eap element.

``` syntax
<xs:element name="EapType"
    type="BaseEapTypeParameters"
 />
```

## Remarks

The **EapType** element is abstract; each method must define and use a derived element in the instance documents.

## Requirements



| Role | Minimum supported OS version |
|-------------------------------------|------------------------------------------------------|
| Client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[baseeapuserpropertiesv1 Schema](baseeapuserpropertiesv1schema-schema.md)
</dt> </dl>

 

 





