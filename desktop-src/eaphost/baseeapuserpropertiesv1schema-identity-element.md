---
title: Identity Element
description: Learn about the EAPHost Identity element. This element captures the identity used for authentication.
ms.assetid: 464979f0-6a2b-43e7-a207-2fbd1e2e5f51
keywords:
- Identity element EAPHost
topic_type:
- apiref
api_name:
- Identity
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# Identity Element

The **Identity** element captures the identity used for authentication.

``` syntax
<xs:element name="Identity"
    type="string"
 />
```

## Remarks

The **Identity** element is abstract; each method must define and use a derived element in the instance documents.

## Requirements



| Role | Minimum supported OS version |
|------|------------------------------|
| Client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[baseeapuserpropertiesv1 Schema](baseeapuserpropertiesv1schema-schema.md)
</dt> </dl>

 

 





