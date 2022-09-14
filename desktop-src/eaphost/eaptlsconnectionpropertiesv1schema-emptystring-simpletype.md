---
title: emptyString Simple Type
description: Learn about the emptyString simple type, which is not in use. See requirements and view additional available resources.
ms.assetid: e561b8d5-8683-41a1-bd72-73b1a767b6cf
keywords:
- emptyString simple type EAPHost
topic_type:
- apiref
api_name:
- emptyString
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# emptyString Simple Type

The **emptyString** simple type is not in use.

``` syntax
<xs:simpleType name="emptyString">
    <xs:restriction
        base="string"
    >
        <xs:maxLength
            value="0"
         />
    </xs:restriction>
</xs:simpleType>
```

## Requirements



| Role | Minimum supported OS version |
|-------------------------------------|------------------------------------------------------|
| Client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[eaptlsconnectionpropertiesv1 Schema](eaptlsconnectionpropertiesv1schema-schema.md)
</dt> <dt>

[eaptlsconnectionpropertiesv1 Schema Simple Types](eaptlsconnectionpropertiesv1schema-simple-types.md)
</dt> </dl>

 

 





