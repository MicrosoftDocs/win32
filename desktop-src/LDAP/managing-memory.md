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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Managing Memory

Client-side memory management depends on the specific LDAP functions. In general, you must release the memory associated with data returned to the client either as an *out* parameter or as a function return value. However, some functions, such as [**ldap\_err2string**](/windows/previous-versions/Winldap/nf-winldap-ldap_err2string?branch=master), return a pointer to a static buffer, and in that case you should not free the memory associated with the returned data.

The LDAP API supports the following memory management functions. For more information about managing memory for a particular function, see the reference page for that function.

The [**ldap\_memfree**](/windows/previous-versions/Winldap/nf-winldap-ldap_memfree?branch=master) function frees memory that was allocated from the LDAP heap. Call this function to free strings, such as the DN returned by [**ldap\_get\_dn**](/windows/previous-versions/Winldap/nf-winldap-ldap_get_dn?branch=master) and the *ErrorMessage* and *MatchedDNs* parameters in [**ldap\_parse\_result**](/windows/previous-versions/Winldap/nf-winldap-ldap_parse_result?branch=master).

The [**ldap\_value\_free**](/windows/previous-versions/Winldap/nf-winldap-ldap_value_free?branch=master) function frees the character string returned by [**ldap\_get\_values**](/windows/previous-versions/Winldap/nf-winldap-ldap_get_values?branch=master). Call [**ldap\_value\_free\_len**](/windows/previous-versions/Winldap/nf-winldap-ldap_value_free_len?branch=master) to free the [**berval**](/windows/previous-versions/Winldap/ns-winldap-berval?branch=master) structures returned by [**ldap\_get\_values\_len**](/windows/previous-versions/Winldap/nf-winldap-ldap_get_values_len?branch=master).

Call the [**ldap\_control\_free**](/windows/previous-versions/Winldap/nf-winldap-ldap_control_free?branch=master) function to dispose of a previously allocated [**LDAPControl**](/windows/previous-versions/Winldap/ns-winldap-ldapcontrola?branch=master) structure. Call [**ldap\_controls\_free**](/windows/previous-versions/Winldap/nf-winldap-ldap_controls_free?branch=master) to dispose of a previously allocated array of **LDAPControl** structures.

Call [**ldap\_msgfree**](/windows/previous-versions/Winldap/nf-winldap-ldap_msgfree?branch=master) to dispose of an [**LDAPMessage**](/windows/previous-versions/Winldap/ns-winldap-ldapmsg?branch=master) structure, such as the one the server returns in a call to [**ldap\_first\_reference**](/windows/previous-versions/Winldap/nf-winldap-ldap_first_reference?branch=master).

 

 




