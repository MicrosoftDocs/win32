---
title: Config (EapHostConfig) Element
description: Is used when the method configuration is in XML text form instead of a binary BLOB.
ms.assetid: f47bec23-745f-47db-84db-2556beb6a9e9
keywords:
- Config element EAPHost
topic_type:
- apiref
api_name:
- Config
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# Config (EapHostConfig) Element

The **Config (EapHostConfig)** element is used when the method configuration is in XML text form instead of a binary BLOB.

``` syntax
<xs:element name="Config"
    type="BaseEapMethodConfig"
 />
```

The **Config** element is defined by the [**EapHostConfig**](eaphostconfigschema-eaphostconfig-element.md) element.

## Remarks

The **Config** and [**ConfigBlob**](eaphostconfigschema-configblob-eaphostconfig-element.md) elements cannot both be used simultaneously.

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

 

 





