---
title: Using ldap\_simple\_bind\_s
description: Queries the LDAP server to authenticate the distinguished name and password provided in its parameters.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '89abdef3-4d5a-49dc-bb83-9130e5b632cb'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-lightweight-directory-services'
ms.tgt_platform: multiple
---

# Using ldap\_simple\_bind\_s

The [**ldap\_simple\_bind\_s**](ldap-simple-bind-s.md) function queries the LDAP server to authenticate the distinguished name and password provided in its parameters. If the server successfully authenticates the name and password, a binding is completed and the function returns LDAP\_SUCCESS. This enables later function calls from this client to read or write directory data, depending on their level of permissions as set by the server.

> \[!Caution\]  
> This function sends the name and password without encrypting them, and therefore someone eavesdropping on the network could read the password. Unless a TLS (SSL) encrypted session has been set up, this function should not be used. For information about how to set up an encrypted session, see [Initializing a Session](initializing-a-session.md).

 

 

 




