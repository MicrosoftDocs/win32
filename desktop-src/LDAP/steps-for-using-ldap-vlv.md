---
title: Steps for Using LDAP VLV
description: The following list shows that steps to take when adding a VLV search to your application. These steps are demonstrated in Example Code for Using LDAP VLV.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '7ffa843e-d483-47de-ba24-2478e1528dbb'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-lightweight-directory-services'
ms.tgt_platform: multiple
keywords: ["Steps for Using LDAP VLV"]
---

# Steps for Using LDAP VLV

The following list shows that steps to take when adding a VLV search to your application. These steps are demonstrated in [Example Code for Using LDAP VLV](example-code-for-using-ldap-vlv.md).

1.  Bind to the server that you want to perform the search on using [**ldap\_bind**](ldap-bind.md) or [**ldap\_bind\_s**](ldap-bind-s.md).
2.  Set the members for [**LDAPVLVInfo**](ldapvlvinfo.md) and create the control using [**ldap\_create\_vlv\_control**](ldap-create-vlv-control.md).
3.  Create a sort control using [**ldap\_create\_sort\_control**](ldap-create-sort-control.md) and add it to an array with the VLV control.
4.  Perform a search on the server using [**ldap\_search\_ext\_s**](ldap-search-ext-s.md) or [**ldap\_search\_ext**](ldap-search-ext.md).
5.  Parse the results from the server using [**ldap\_parse\_result**](ldap-parse-result.md), then parse the vlv results received from the response control (LDAP\_CONTROL\_VLVRESPONSE) using [**ldap\_parse\_vlv\_control**](ldap-parse-vlv-control.md).
6.  Free the control using [**ldap\_control\_free**](ldap-control-free.md).

 

 




