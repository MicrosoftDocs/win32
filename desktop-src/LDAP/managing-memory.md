---
title: Managing Memory
description: Client-side memory management depends on the specific LDAP functions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '73054cae-cf3e-4860-b903-7df83611e150'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-lightweight-directory-services'
ms.tgt_platform: multiple
keywords: ["Managing Memory LDAP"]
---

# Managing Memory

Client-side memory management depends on the specific LDAP functions. In general, you must release the memory associated with data returned to the client either as an *out* parameter or as a function return value. However, some functions, such as [**ldap\_err2string**](ldap-err2string.md), return a pointer to a static buffer, and in that case you should not free the memory associated with the returned data.

The LDAP API supports the following memory management functions. For more information about managing memory for a particular function, see the reference page for that function.

The [**ldap\_memfree**](ldap-memfree.md) function frees memory that was allocated from the LDAP heap. Call this function to free strings, such as the DN returned by [**ldap\_get\_dn**](ldap-get-dn.md) and the *ErrorMessage* and *MatchedDNs* parameters in [**ldap\_parse\_result**](ldap-parse-result.md).

The [**ldap\_value\_free**](ldap-value-free.md) function frees the character string returned by [**ldap\_get\_values**](ldap-get-values.md). Call [**ldap\_value\_free\_len**](ldap-value-free-len.md) to free the [**berval**](berval.md) structures returned by [**ldap\_get\_values\_len**](ldap-get-values-len.md).

Call the [**ldap\_control\_free**](ldap-control-free.md) function to dispose of a previously allocated [**LDAPControl**](ldapcontrol.md) structure. Call [**ldap\_controls\_free**](ldap-controls-free.md) to dispose of a previously allocated array of **LDAPControl** structures.

Call [**ldap\_msgfree**](ldap-msgfree.md) to dispose of an [**LDAPMessage**](ldapmessage.md) structure, such as the one the server returns in a call to [**ldap\_first\_reference**](ldap-first-reference.md).

 

 




