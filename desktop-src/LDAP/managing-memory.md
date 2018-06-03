---
title: Managing Memory
description: Client-side memory management depends on the specific LDAP functions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 73054cae-cf3e-4860-b903-7df83611e150
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- Managing Memory LDAP
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Managing Memory

Client-side memory management depends on the specific LDAP functions. In general, you must release the memory associated with data returned to the client either as an *out* parameter or as a function return value. However, some functions, such as [**ldap\_err2string**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_err2string), return a pointer to a static buffer, and in that case you should not free the memory associated with the returned data.

The LDAP API supports the following memory management functions. For more information about managing memory for a particular function, see the reference page for that function.

The [**ldap\_memfree**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_memfree) function frees memory that was allocated from the LDAP heap. Call this function to free strings, such as the DN returned by [**ldap\_get\_dn**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_get_dn) and the *ErrorMessage* and *MatchedDNs* parameters in [**ldap\_parse\_result**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_parse_result).

The [**ldap\_value\_free**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_value_free) function frees the character string returned by [**ldap\_get\_values**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_get_values). Call [**ldap\_value\_free\_len**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_value_free_len) to free the [**berval**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-berval) structures returned by [**ldap\_get\_values\_len**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_get_values_len).

Call the [**ldap\_control\_free**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_control_free) function to dispose of a previously allocated [**LDAPControl**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-ldapcontrola) structure. Call [**ldap\_controls\_free**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_controls_free) to dispose of a previously allocated array of **LDAPControl** structures.

Call [**ldap\_msgfree**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_msgfree) to dispose of an [**LDAPMessage**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-ldapmsg) structure, such as the one the server returns in a call to [**ldap\_first\_reference**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_first_reference).

 

 




