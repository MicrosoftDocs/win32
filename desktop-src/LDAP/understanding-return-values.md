---
title: Understanding Return Values
description: Most LDAP functions return a numeric Return Value that indicates whether the function call succeeds or what type of error was encountered. However, this information is sometimes not enough to understand the actual problem.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: a364bea4-280b-49af-813d-47614133338f
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- Understanding Return Values LDAP
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Understanding Return Values

Most LDAP functions return a numeric [Return Value](return-values.md) that indicates whether the function call succeeds or what type of error was encountered. However, this information is sometimes not enough to understand the actual problem.

Requesting the server error code can often help identify the source of the problem. The [**ldap\_get\_option**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_get_option) function is used with LDAP version 3 to retrieve the server error string.


```C++
// ld is the LDAP connection.
PCHAR pServerError;        // Use PWCHAR if Unicode.

ULONG ulRtn = ldap_get_option(ld,LDAP_OPT_SERVER_ERROR,(void*)&amp;pServerError);
if (ulRtn == LDAP_SUCCESS)
{
    // Handle the error string.

    ldap_memfree(pErrorString);
}
```



The following code example can be used to identify the error code that the server embeds at the start of the server error string.


```C++
// ld is the LDAP connection.
ULONG ulServerError;

ULONG ulRtn = ldap_get_option(ld,LDAP_OPT_SERVER_EXT_ERROR,(void*)&amp;ulServerError);
if (ulRtn == LDAP_SUCCESS)
{
    // Handle the error code.
}
```



 

 




