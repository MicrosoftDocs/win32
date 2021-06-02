---
description: Specifies whether the user credentials are cached for subsequent connections.
ms.assetid: 65ed03f1-f61e-46f8-a666-91b393618de3
title: cacheUserData (OneX) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- cacheUserData
api_type: 
- Schema
api_location: 
---

# cacheUserData (OneX) Element

The cacheUserData (OneX) element specifies whether the user credentials are cached for subsequent connections. When cacheUserData is TRUE, the credentials are cached. When cacheUserData is FALSE, the credentials are not cached and the user may be prompted for credentials on subsequent connection attempts.

This element is optional. When cacheUserData is not specified in a profile, the user credentials are cached.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

``` syntax
<xs:element name="cacheUserData"
    type="boolean"
 />
```

The **cacheUserData** element is defined by the [**OneX**](onexschema-onex-element.md) element.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**OneX**](onexschema-onex-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**OneX**](onexschema-onex-element.md)
</dt> </dl>

 

 




