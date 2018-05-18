---
title: LDAP\_SERVER\_FAST\_BIND\_OID
description: Used internally by the LDAP\_OPT\_FAST\_CONCURRENT\_BIND session option to put an LDAP connection into fast bind mode.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '8b69d0b4-77cb-442d-9865-fcea41e8ff9d'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-lightweight-directory-services'
ms.tgt_platform: multiple
keywords: ["LDAP_SERVER_FAST_BIND_OID LDAP"]
---

# LDAP\_SERVER\_FAST\_BIND\_OID

The LDAP\_SERVER\_FAST\_BIND\_OID is used internally by the **LDAP\_OPT\_FAST\_CONCURRENT\_BIND** session option to put an LDAP connection into fast bind mode. For more information, see [**Session Options**](session-options.md).

The LDAP\_SERVER\_FAST\_BIND\_OID, defined as "1.2.840.113556.1.4.1781", identifies an LDAP extended request that puts an LDAP connection into fast bind mode. This mode is intended for use by server applications that use LDAP as to authenticate clients. During a normal bind the LDAP server checks the credentials and then determines all the groups that the client is a member of to perform further authorization. Fast bind mode is a way of skipping the group evaluation step if LDAP is only used to verify a client's credentials. Only simple binds are accepted on a connection in this mode. Because no group evaluation is done the connection is always handled as if no bind had occurred for the purposes of all other LDAP operations.

This OID is used internally by the LDAP client API. To place an Active Directory server in fast bind mode, the **LDAP\_OPT\_FAST\_CONCURRENT\_BIND** session option should be used. For more information about using this session option, see [Using LDAP for Password Authentication](using-ldap-for-password-authentication.md).

 

 




