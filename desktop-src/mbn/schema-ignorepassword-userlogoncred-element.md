---
description: Specifies how to handle passwords when upgrading profiles.
ms.assetid: 74d7ceb1-d778-4a12-907b-0528d9ff45be
title: IgnorePassword (UserLogonCred) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IgnorePassword
api_type: 
- Schema
---

# IgnorePassword (UserLogonCred) Element

The **IgnorePassword (UserLogonCred)** element specifies how to handle passwords when upgrading profiles.

If set to **TRUE** and a profile with the same name exists at the time of the update operation, then the password from that profile will be taken and stored in new profile.

This element is optional.

``` syntax
<xs:element name="IgnorePassword"
    type="boolean"
 />
```

The **IgnorePassword** element is defined by the [**UserLogonCred**](schema-userlogoncred-contexttype-element.md) element.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported server<br/> | None supported<br/>                         |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**UserLogonCred**](schema-userlogoncred-contexttype-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**UserLogonCred (contextType)**](schema-userlogoncred-contexttype-element.md)
</dt> </dl>

 

 




