---
title: Closing a Connection
description: When an LDAP client has finished communicating with a server, and all necessary memory cleanup is complete, call ldap\_unbind or ldap\_unbind\_s to unbind from the directory, close the connection, and release the session handle.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '692c0a08-5313-40a1-bbc6-5b9063e7d336'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-lightweight-directory-services'
ms.tgt_platform: multiple
keywords: ["Closing a Connection LDAP"]
---

# Closing a Connection

When an LDAP client has finished communicating with a server, and all necessary memory cleanup is complete, call [**ldap\_unbind**](ldap-unbind.md) or [**ldap\_unbind\_s**](ldap-unbind-s.md) to unbind from the directory, close the connection, and release the session handle. Call this function when you have finished with a connection, even if you have not explicitly called a bind function to open the connection.

Both [**ldap\_unbind**](ldap-unbind.md) and [**ldap\_unbind\_s**](ldap-unbind-s.md) work synchronously. There is no server response to an unbind operation. Ensure that you do not inadvertently call either unbind function more than one time on a session handle; doing so can free resources that you did not intend to release.

 

 




