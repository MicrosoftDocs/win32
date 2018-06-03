---
title: Steps for Using LDAP VLV
description: The following list shows that steps to take when adding a VLV search to your application. These steps are demonstrated in Example Code for Using LDAP VLV.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 7ffa843e-d483-47de-ba24-2478e1528dbb
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- Steps for Using LDAP VLV
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Steps for Using LDAP VLV

The following list shows that steps to take when adding a VLV search to your application. These steps are demonstrated in [Example Code for Using LDAP VLV](example-code-for-using-ldap-vlv.md).

1.  Bind to the server that you want to perform the search on using [**ldap\_bind**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_bind) or [**ldap\_bind\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_bind_s).
2.  Set the members for [**LDAPVLVInfo**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-ldapvlvinfo) and create the control using [**ldap\_create\_vlv\_control**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_create_vlv_controla).
3.  Create a sort control using [**ldap\_create\_sort\_control**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_create_sort_control) and add it to an array with the VLV control.
4.  Perform a search on the server using [**ldap\_search\_ext\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_search_ext_s) or [**ldap\_search\_ext**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_search_ext).
5.  Parse the results from the server using [**ldap\_parse\_result**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_parse_result), then parse the vlv results received from the response control (LDAP\_CONTROL\_VLVRESPONSE) using [**ldap\_parse\_vlv\_control**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_parse_vlv_controla).
6.  Free the control using [**ldap\_control\_free**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_control_free).

 

 




