---
title: Eap Element (connection properties)
description: Learn about the Eap element. This element captures the method type selected and method-specific configuration. | Eap Element (connection properties)
ms.assetid: 4e9f3869-257e-4b03-93f6-2eec94eaacee
keywords:
- Eap element EAPHost
topic_type:
- apiref
api_name:
- Eap
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# Eap Element (connection properties)

The **Eap** element captures the method type selected and method-specific configuration.

``` syntax
<xs:element name="Eap
          
        "
    type="BaseEapParameters"
 />
```

## Remarks

The method can define the constituent elements inside the **Eap** element. The method also performs schema validation on the elements in **Eap**.

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

 

 





