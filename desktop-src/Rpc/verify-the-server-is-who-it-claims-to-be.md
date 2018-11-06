---
title: Verify the Server is Who it Claims to Be
description: It is best to use mutual authentication, and thereby verify the identity of the server.
ms.assetid: 6636a865-0e3b-4e52-81bb-0df48285e928
ms.topic: article
ms.date: 05/31/2018
---

# Verify the Server is Who it Claims to Be

It is best to use mutual authentication, and thereby verify the identity of the server. An example of a common mistake that fails to do this is applications that have a local service into which clients call. In some configurations an administrator may decide that the system service is not really useful and may chose to stop it. An inventive attacker on a terminal server computer may launch a process that listens on the same endpoint, and when a client connects to an endpoint, allowing impersonation on the server without mutually authenticating the server, the attacker can impersonate the client and access the client's data, or make network calls on behalf of the client. Most system services run under a well-known account, such as LocalSysyem, LocalService, or NetworkService, which can be verified using mutual authentication.

 

 




