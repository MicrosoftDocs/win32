---
description: Microsoft Digest performs an initial authentication when the server receives the first challenge response from a client.
ms.assetid: c65bb134-d480-4a71-872c-30e2884237a6
title: Microsoft Digest Authentication
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft Digest Authentication

Microsoft Digest performs an initial authentication when the server receives the first challenge response from a client. The server verifies that the client has not been authenticated and then performs the initial authentication by accessing the services of a domain controller. For a detailed description of this procedure, see [Initial Authentication Using Microsoft Digest](initial-authentication-using-microsoft-digest.md).

When the initial authentication is successful the server receives a Digest [*session key*](../secgloss/s-gly.md). The server caches this key and uses it to authenticate subsequent requests for resources from the client. This authentication is local, that is, it does not require access to a domain controller. For a detailed description of this procedure see [Authenticating Subsequent Requests Using Microsoft Digest](authenticating-subsequent-requests-using-microsoft-digest.md).

When using HTTP, there is no connection maintained between client and server. To reduce domain controller traffic and improve performance, Microsoft Digest caches information received after successful authentication. For information about this process, see [Maintaining the Security Context Between Connections](maintaining-the-security-context-between-connections.md).

 

 
