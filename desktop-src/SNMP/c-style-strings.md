---
title: C-Style Strings
description: A WinSNMP application can use NULL-terminated C-style strings to convert entity and object identifier (OID) objects to and from their string representations.
ms.assetid: df04071c-df46-410b-ad92-6adecbfcd454
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# C-Style Strings

A WinSNMP application can use **NULL**-terminated C-style strings to convert entity and object identifier (OID) objects to and from their string representations.

The WinSNMP functions that manipulate C-style strings include [**SnmpStrToEntity**](/windows/win32/Winsnmp/nf-winsnmp-snmpstrtoentity?branch=master), [**SnmpEntityToStr**](/windows/win32/Winsnmp/nf-winsnmp-snmpentitytostr?branch=master), [**SnmpStrToOid**](/windows/win32/Winsnmp/nf-winsnmp-snmpstrtooid?branch=master), and [**SnmpOidToStr**](/windows/win32/Winsnmp/nf-winsnmp-snmpoidtostr?branch=master). Because [**SnmpEntityToStr**](/windows/win32/Winsnmp/nf-winsnmp-snmpentitytostr?branch=master) and [**SnmpOidToStr**](/windows/win32/Winsnmp/nf-winsnmp-snmpoidtostr?branch=master) return a pointer to a C-style string variable, the WinSNMP application must pass an appropriate value in the *size* parameter when it makes calls to these functions. For more information, see the reference pages for these functions.

> [!Note]  
> The *context* parameter of the [**SnmpStrToContext**](/windows/win32/Winsnmp/nf-winsnmp-snmpstrtocontext?branch=master) and [**SnmpContextToStr**](/windows/win32/Winsnmp/nf-winsnmp-snmpcontexttostr?branch=master) functions must be an octet string structure, that is, an [**smiOCTETS**](/windows/win32/Winsnmp/ns-winsnmp-smioctets?branch=master) structure. The *context* parameter cannot be a C-style string. The string contained in an **smiOCTETS** structure does not require a **NULL**-terminating byte.

 

 

 




