---
description: Specifies whether the automatic configuration service for wired networks will attempt port authentication using 802.1X.
ms.assetid: ab6cfc59-9cfd-45d3-ad27-306ad4f6d4e1
title: OneXEnabled (security) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- OneXEnabled
api_type: 
- Schema
api_location: 
---

# OneXEnabled (security) Element

The **OneXEnabled** (security) element specifies whether the automatic configuration service for wired networks will attempt port authentication using 802.1X. When **OneXEnabled** is FALSE, the automatic configuration service never uses 802.1X for port authentication. When **OneXEnabled** is TRUE, then the automatic configuration service attempts port authentication using 802.1X.

This element is optional. The default value is TRUE. When **OneXEnabled** is not specified in a profile, then 802.1X may be used for port authentication.

``` syntax
<xs:element name="OneXEnabled"
    type="boolean"
 />
```

The **OneXEnabled** element is defined by the [**security**](lan-profileschema-security-msm-element.md) element.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**security**](lan-profileschema-security-msm-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**security (MSM)**](lan-profileschema-security-msm-element.md)
</dt> </dl>

 

 




