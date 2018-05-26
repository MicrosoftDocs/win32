---
title: Object(DN-Binary) syntax
description: An octet string that contains a binary value and a distinguished name (DN).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 1d7efc17-a99a-41bf-9812-9e8a2b2b6644
ms.prod: windows-server-dev
ms.technology: active-directory-schema
ms.tgt_platform: multiple
keywords:
- Object(DN-Binary) syntax AD Schema
topic_type:
- apiref
api_name:
- Object(DN-Binary)
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Object(DN-Binary) syntax

An octet string that contains a binary value and a distinguished name (DN).



|              |                                                                                    |
|--------------|------------------------------------------------------------------------------------|
| Name         | Object(DN-Binary)                                                                  |
| Syntax ID    | 2.5.5.7                                                                            |
| OM ID        | 127                                                                                |
| MAPI Type    | TSTRING                                                                            |
| ADS Type     | ADSTYPE\_DN\_WITH\_BINARY                                                          |
| Variant Type | VT\_DISPATCH                                                                       |
| SDS Type     | A COM object that can be cast to an [**IADsDNWithBinary**](https://msdn.microsoft.com/library/aa705996). |



## Remarks

A value with this syntax has the following format:

``` syntax
B:<char count>:<binary value>:<object DN>
```

where "&lt;char count&gt;" is the number of hexadecimal digits in "&lt;binary value&gt;", "&lt;binary value&gt;" is the hexadecimal representation of the binary value, and "&lt;object DN&gt;" is a distinguished name. Active Directory automatically updates the DN if the object that it refers to is moved or renamed. For more information and a code example that uses this syntax, see [Enabling Rename-safe Binding with the otherWellKnownObjects Property](https://msdn.microsoft.com/library/ms676295).

## See also

<dl> <dt>

[**IADsDNWithBinary**](https://msdn.microsoft.com/library/aa705996)
</dt> </dl>

 

 




