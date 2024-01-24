---
title: EapType element (v1 schema connection property)
description: Learn about the EapType element. This element captures method-specific configuration inside the Eap element. | EapType element (v1 schema connection property)
ms.assetid: f953e150-64cf-41b2-937f-410799be4602
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

# EapType Element (v1 schema connection property)

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
|------|------------------------------|
| Client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[baseeapconnectionpropertiesv1 Schema](baseeapconnectionpropertiesv1schema-schema.md)
</dt> </dl>

 

 





