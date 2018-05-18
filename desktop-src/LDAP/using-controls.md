---
title: Using Controls
description: LDAP 3 operations can be extended through the use of controls. Controls may be sent to a server or returned to the client with any LDAP message. These controls are referred to as server controls.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '2c1f68e6-51b0-4270-b55a-88ba7292bbbc'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-lightweight-directory-services'
ms.tgt_platform: multiple
---

# Using Controls

LDAP 3 operations can be extended through the use of controls. Controls may be sent to a server or returned to the client with any LDAP message. These controls are referred to as server controls.

The LDAP API also supports a client-side extension mechanism through the use of client controls. These controls affect the behavior of the LDAP API only and are never sent to a server. A common data structure, [**LDAPControl**](ldapcontrol.md), is used to represent both types of controls.

Some LDAP API calls allocate an **LDAPControl** structure or a NULL-terminated array of **LDAPControl** structures. The following routines can be used to dispose of a single control or an array of controls:

-   [**ldap\_control\_free**](ldap-control-free.md)
-   [**ldap\_controls\_free**](ldap-controls-free.md)

A set of controls that affect the entire session can be set using the [**ldap\_set\_option**](ldap-set-option.md) function. A list of controls can also be passed directly to some LDAP API calls such as [**ldap\_search\_ext**](ldap-search-ext.md), in which case any controls set for the session by means of **ldap\_set\_option** are ignored. Control lists are represented as a NULL-terminated array of pointers to **LDAPControl** structures.

Server controls are defined by LDAP 3 protocol extension documents. Various LDAP version 3 server implementations are likely to support a different set of extended controls, so if a particular control is critical to an operation, the server can be queried to return a list of supported controls, or the server can be instructed to fail gracefully when using a function with a control not supported by that server.

Each extended control has a Criticality flag, represented by the **ldctl\_iscritical** field of the [**LDAPControl**](ldapcontrol.md) structure. If this flag is set to **TRUE**, then the server will return a [**LDAP\_UNAVAILABLE\_CRIT\_EXTENSION**](return-values.md) error code if the server does not support the request control when attempting an API call that includes the control. Using extended controls on a LDAP version 2 connection will also fail with this return code.

 

 




