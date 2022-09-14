---
title: Dynamic Authentication Configuration
description: Applications can change authentication configurations on a URL Group or server session at any time.
ms.assetid: 8a5cc119-0427-487d-a155-74c14e2104d4
ms.topic: article
ms.date: 05/31/2018
---

# Dynamic Authentication Configuration

By default, the HTTP Server API does not perform authentication unless the application specifically enables it. Applications can change authentication configurations on a URL Group or server session at any time. Changes to the authentication configuration do not affect requests that are already authenticated or being dispatched to the application

For authentication schemes where multiple rounds of handshake are required, the HTTP Server API drops the authentication handshake if the current scheme is no longer supported due to configuration changes from the application. For example, if the application enables Negotiate and disables NTLM, and the HTTP Server API is in the intermediate authentication handshake for NTLM, the handshake for NTLM is discarded and the request is passed to the application. The application sends a 401 authentication challenge with the new authentication types specified in the WWW-Authenticate header.

 

 




