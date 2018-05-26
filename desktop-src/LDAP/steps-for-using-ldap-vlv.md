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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Steps for Using LDAP VLV

The following list shows that steps to take when adding a VLV search to your application. These steps are demonstrated in [Example Code for Using LDAP VLV](example-code-for-using-ldap-vlv.md).

1.  Bind to the server that you want to perform the search on using [**ldap\_bind**](/windows/previous-versions/Winldap/nf-winldap-ldap_bind?branch=master) or [**ldap\_bind\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_bind_s?branch=master).
2.  Set the members for [**LDAPVLVInfo**](/windows/previous-versions/Winldap/ns-winldap-ldapvlvinfo?branch=master) and create the control using [**ldap\_create\_vlv\_control**](/windows/previous-versions/Winldap/nf-winldap-ldap_create_vlv_controla?branch=master).
3.  Create a sort control using [**ldap\_create\_sort\_control**](/windows/previous-versions/Winldap/nf-winldap-ldap_create_sort_control?branch=master) and add it to an array with the VLV control.
4.  Perform a search on the server using [**ldap\_search\_ext\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_search_ext_s?branch=master) or [**ldap\_search\_ext**](/windows/previous-versions/Winldap/nf-winldap-ldap_search_ext?branch=master).
5.  Parse the results from the server using [**ldap\_parse\_result**](/windows/previous-versions/Winldap/nf-winldap-ldap_parse_result?branch=master), then parse the vlv results received from the response control (LDAP\_CONTROL\_VLVRESPONSE) using [**ldap\_parse\_vlv\_control**](/windows/previous-versions/Winldap/nf-winldap-ldap_parse_vlv_controla?branch=master).
6.  Free the control using [**ldap\_control\_free**](/windows/previous-versions/Winldap/nf-winldap-ldap_control_free?branch=master).

 

 




