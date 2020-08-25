---
title: PeapExtensionsType complex type (connection properties)
description: Learn about the PeapExtensionsType complex type. This type enables future enhancements to the schema.
ms.assetid: d4f7784d-d426-4da6-bf81-40716f185416
keywords:
- PeapExtensionsType complex type EAPHost
topic_type:
- apiref
api_name:
- PeapExtensionsType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# PeapExtensionsType complex type (connection properties)

The **PeapExtensionsType** complex type enables future enhancements to the schema.

``` syntax
<xs:complexType name="PeapExtensionsType">
    <xs:sequence>
        <xs:any
            processContents="lax"
            minOccurs="0"
            maxOccurs="unbounded"
            namespace="##other"
         />
    </xs:sequence>
</xs:complexType>
```

## Remarks

The **PeapExtensionsType** complex type is optional.

## Requirements



| Role | Minimum supported OS version |
|------|------------------------------|
| Client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[mspeapuserpropertiesv1 Schema](mspeapuserpropertiesv1schema-schema.md)
</dt> </dl>

 

 





