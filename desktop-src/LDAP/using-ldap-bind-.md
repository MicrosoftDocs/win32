---
title: Using ldap\_bind
description: Used for asynchronous authentication and binding.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: d47f4ede-938b-4edb-9e73-1508da02a4da
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using ldap\_bind

The [**ldap\_bind**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_bind) function is used for asynchronous authentication and binding. LDAP\_AUTH\_SIMPLE is the only authentication method compatible with this asynchronous binding function. Using another authentication method with **ldap\_bind** will fail and return LDAP\_PARAM\_ERROR. All other authentication methods require synchronous binding as provided by [**ldap\_bind\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_bind_s). Like [**ldap\_simple\_bind\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_simple_bind_s), the LDAP\_AUTH\_SIMPLE method used with the **ldap\_bind** function, requires a name and password transmitted in plaintext.

> \[!Caution\]  
> This function sends the name and password unencrypted, and therefore can be intercepted. Unless a TLS (SSL) encrypted session has been set up, this function should not be used. For information about how to set up an encrypted session, see [Initializing a Session](initializing-a-session.md).

 

 

 




