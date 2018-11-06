---
title: C-Style Strings
description: A WinSNMP application can use NULL-terminated C-style strings to convert entity and object identifier (OID) objects to and from their string representations.
ms.assetid: df04071c-df46-410b-ad92-6adecbfcd454
ms.topic: article
ms.date: 05/31/2018
---

# C-Style Strings

A WinSNMP application can use **NULL**-terminated C-style strings to convert entity and object identifier (OID) objects to and from their string representations.

The WinSNMP functions that manipulate C-style strings include [**SnmpStrToEntity**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstrtoentity), [**SnmpEntityToStr**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpentitytostr), [**SnmpStrToOid**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstrtooid), and [**SnmpOidToStr**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpoidtostr). Because [**SnmpEntityToStr**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpentitytostr) and [**SnmpOidToStr**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpoidtostr) return a pointer to a C-style string variable, the WinSNMP application must pass an appropriate value in the *size* parameter when it makes calls to these functions. For more information, see the reference pages for these functions.

> [!Note]  
> The *context* parameter of the [**SnmpStrToContext**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstrtocontext) and [**SnmpContextToStr**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcontexttostr) functions must be an octet string structure, that is, an [**smiOCTETS**](/windows/desktop/api/Winsnmp/ns-winsnmp-smioctets) structure. The *context* parameter cannot be a C-style string. The string contained in an **smiOCTETS** structure does not require a **NULL**-terminating byte.

 

 

 




