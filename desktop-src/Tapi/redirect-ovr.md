---
description: Session redirection allows an application to deflect an offered session to another address without answering the call.
ms.assetid: b52cd5c2-fdd6-4240-b07b-b22733a89d27
title: Redirect
ms.topic: article
ms.date: 05/31/2018
---

# Redirect

Session redirection allows an application to deflect an offered session to another address without answering the call. The application can do redirection on a call-by-call basis. For example, an application might allow a user to specify different redirections based on caller ID information. After a call has been successfully redirected, the state typically transitions to idle and associated resources must be released.

Redirect differs from [forward](forward-ovr.md) in that once forwarding has been set up, the operation is performed by TAPI, the service provider, or the switch without further involvement of the application. Redirect differs from [transfer](transfer-ovr.md) in that redirect does not require answering the call first.

Not all service providers support use of this operation.

**TAPI 2.x:** See [**lineRedirect**](/windows/win32/api/tapi/nf-tapi-lineredirect).

 

 
