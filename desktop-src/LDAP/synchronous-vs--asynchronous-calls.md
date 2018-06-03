---
title: Synchronous and Asynchronous Calls
description: Most of the LDAP function calls have both asynchronous and synchronous versions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 97d7cd88-7fa8-40d6-9ea1-f2e586634a28
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Synchronous and Asynchronous Calls

Most of the LDAP function calls have both asynchronous and synchronous versions. A synchronous function call, identified by an **-s** suffix in the function name, must return before your client can continue executing code. Synchronous functions return LDAP\_SUCCESS if successful, or another LDAP error code if the call failed.

When you make an asynchronous function call, the client can continue with other tasks, including making new requests to the server, or processing the results of a search, while the asynchronous request is in progress. Most asynchronous functions return a message identifier (ID) for each operation.

At any time a client application can check on the status of an asynchronous call by calling [**ldap\_result**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_result) with the message ID. To abandon an asynchronous call in progress, call [**ldap\_abandon**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_abandon).

Because the function returns a message ID, rather than a return code, these asynchronous functions are not thread-safe. To determine whether the call returned an error value, you have to retrieve the return code from the connection block. It is possible for another thread to overwrite the return code before you retrieve it. The extended operation calls provided with LDAP 3 (identified by an \_ext suffix) are thread-safe because they pass the message ID back to the caller as an *out* parameter.

 

 




