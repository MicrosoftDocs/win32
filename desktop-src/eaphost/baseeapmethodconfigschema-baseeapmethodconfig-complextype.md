---
title: BaseEapMethodConfig Complex Type
description: Learn about the BaseEapMethodConfig complex type. This type is a placeholder element for the method configuration.
ms.assetid: 9aafd6ad-2342-4882-99d3-2f2e6c3d67b5
keywords:
- BaseEapMethodConfig complex type EAPHost
topic_type:
- apiref
api_name:
- BaseEapMethodConfig
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# BaseEapMethodConfig Complex Type

The **BaseEapMethodConfig** complex type is a placeholder element for the method configuration.

``` syntax
<xs:complexType name="BaseEapMethodConfig">
    <xs:sequence>
        <xs:any
            processContents="lax"
            minOccurs="0"
            maxOccurs="unbounded"
            namespace="##any"
         />
    </xs:sequence>
</xs:complexType>
```

## Remarks

The EAP method performs schema validation on the contents of the **BaseEapMethodConfig** element.

## Requirements



| Role | Minimum supported OS version |
|------|------------------------------|
| Client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[baseeapmethodconfig Schema](baseeapmethodconfigschema-schema.md)
</dt> </dl>

 

 





