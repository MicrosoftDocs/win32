---
title: ConfigBlob (EapHostConfig) Element
description: Is used when the method configuration is in binary BLOB form instead of text string form.
ms.assetid: 2820e0b8-2cd1-40e8-ac0c-a62e73ac3847
keywords:
- ConfigBlob element EAPHost
topic_type:
- apiref
api_name:
- ConfigBlob
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# ConfigBlob (EapHostConfig) Element

The **ConfigBlob (EapHostConfig)** element is used when the method configuration is in binary BLOB form instead of text string form.

``` syntax
<xs:element name="ConfigBlob"
    type="hexBinary"
 />
```

The **ConfigBlob** element is defined by the [**EapHostConfig**](eaphostconfigschema-eaphostconfig-element.md) element.

## Remarks

The [**Config**](eaphostconfigschema-config-eaphostconfig-element.md) and **ConfigBlob** elements cannot both be used simultaneously.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**EapHostConfig**](eaphostconfigschema-eaphostconfig-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**EapHostConfig**](eaphostconfigschema-eaphostconfig-element.md)
</dt> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[eaphostconfig Schema](eaphostconfigschema-schema.md)
</dt> </dl>

 

 





