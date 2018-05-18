---
title: Extended Operations
description: The ldap\_extended\_operation function allows a client to send an extended request (free for all) to an LDAP 3 server. The feature is open and the client request can be for any operation, requiring single or multiple responses.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '25c846b6-0745-4294-8aa4-6383ff1b2205'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-lightweight-directory-services'
ms.tgt_platform: multiple
keywords: ["Extended Operations LDAP"]
---

# Extended Operations

The [**ldap\_extended\_operation**](ldap-extended-operation.md) function allows a client to send an extended request (free for all) to an LDAP 3 server. The feature is open and the client request can be for any operation, requiring single or multiple responses.

Due to the open nature of the request, the client must call [**ldap\_close\_extended\_op**](ldap-close-extended-op.md) to terminate the request.

 

 




