---
title: Using Controls
description: LDAP 3 operations can be extended through the use of controls. Controls may be sent to a server or returned to the client with any LDAP message. These controls are referred to as server controls.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 2c1f68e6-51b0-4270-b55a-88ba7292bbbc
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using Controls

LDAP 3 operations can be extended through the use of controls. Controls may be sent to a server or returned to the client with any LDAP message. These controls are referred to as server controls.

The LDAP API also supports a client-side extension mechanism through the use of client controls. These controls affect the behavior of the LDAP API only and are never sent to a server. A common data structure, [**LDAPControl**](/windows/previous-versions/Winldap/ns-winldap-ldapcontrola?branch=master), is used to represent both types of controls.

Some LDAP API calls allocate an **LDAPControl** structure or a NULL-terminated array of **LDAPControl** structures. The following routines can be used to dispose of a single control or an array of controls:

-   [**ldap\_control\_free**](/windows/previous-versions/Winldap/nf-winldap-ldap_control_free?branch=master)
-   [**ldap\_controls\_free**](/windows/previous-versions/Winldap/nf-winldap-ldap_controls_free?branch=master)

A set of controls that affect the entire session can be set using the [**ldap\_set\_option**](/windows/previous-versions/Winldap/nf-winldap-ldap_set_option?branch=master) function. A list of controls can also be passed directly to some LDAP API calls such as [**ldap\_search\_ext**](/windows/previous-versions/Winldap/nf-winldap-ldap_search_ext?branch=master), in which case any controls set for the session by means of **ldap\_set\_option** are ignored. Control lists are represented as a NULL-terminated array of pointers to **LDAPControl** structures.

Server controls are defined by LDAP 3 protocol extension documents. Various LDAP version 3 server implementations are likely to support a different set of extended controls, so if a particular control is critical to an operation, the server can be queried to return a list of supported controls, or the server can be instructed to fail gracefully when using a function with a control not supported by that server.

Each extended control has a Criticality flag, represented by the **ldctl\_iscritical** field of the [**LDAPControl**](/windows/previous-versions/Winldap/ns-winldap-ldapcontrola?branch=master) structure. If this flag is set to **TRUE**, then the server will return a [**LDAP\_UNAVAILABLE\_CRIT\_EXTENSION**](return-values.md) error code if the server does not support the request control when attempting an API call that includes the control. Using extended controls on a LDAP version 2 connection will also fail with this return code.

 

 




