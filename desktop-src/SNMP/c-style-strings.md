---
title: C-Style Strings
description: A WinSNMP application can use NULL-terminated C-style strings to convert entity and object identifier (OID) objects to and from their string representations.
ms.assetid: 'df04071c-df46-410b-ad92-6adecbfcd454'
---

# C-Style Strings

A WinSNMP application can use **NULL**-terminated C-style strings to convert entity and object identifier (OID) objects to and from their string representations.

The WinSNMP functions that manipulate C-style strings include [**SnmpStrToEntity**](snmpstrtoentity.md), [**SnmpEntityToStr**](snmpentitytostr.md), [**SnmpStrToOid**](snmpstrtooid.md), and [**SnmpOidToStr**](snmpoidtostr.md). Because [**SnmpEntityToStr**](snmpentitytostr.md) and [**SnmpOidToStr**](snmpoidtostr.md) return a pointer to a C-style string variable, the WinSNMP application must pass an appropriate value in the *size* parameter when it makes calls to these functions. For more information, see the reference pages for these functions.

> [!Note]  
> The *context* parameter of the [**SnmpStrToContext**](snmpstrtocontext.md) and [**SnmpContextToStr**](snmpcontexttostr.md) functions must be an octet string structure, that is, an [**smiOCTETS**](smioctets-str.md) structure. The *context* parameter cannot be a C-style string. The string contained in an **smiOCTETS** structure does not require a **NULL**-terminating byte.

 

 

 




