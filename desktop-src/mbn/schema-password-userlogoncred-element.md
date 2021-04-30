---
description: Specifies the password used to authenticate a user.
ms.assetid: 9c02413b-a4c7-4c1f-a150-e27cc125faf6
title: Password (UserLogonCred) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Password
api_type: 
- Schema
---

# Password (UserLogonCred) Element

The [**Password (UserLogonCred)**](schema-ignorepassword-userlogoncred-element.md) element specifies the password used to authenticate a user.

The element is a string of up to 255 characters.

This element is optional.

``` syntax
<xs:element name="Password"
    type="string"
 />
```

The **Password** element is defined by the [**UserLogonCred**](schema-userlogoncred-contexttype-element.md) element.

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

 

 




