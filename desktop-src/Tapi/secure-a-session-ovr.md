---
description: If an application does not want any interference by outside events for a session from TAPI or the service provider, it should secure the call.
ms.assetid: 0a3be209-e3ff-4177-abb2-ad0facbdf569
title: Secure a Session
ms.topic: article
ms.date: 05/31/2018
---

# Secure a Session

If an application does not want any interference by outside events for a session from TAPI or the service provider, it should secure the call. For example, in an analog environment call-waiting tones can destroy a fax or modem session on the original call.

An application can secure a call at the time the call is made or after the call already exists.

Not all service providers support use of this operation.

**TAPI 2.x:** See [**lineSecureCall**](/windows/win32/api/tapi/nf-tapi-linesecurecall).

**TAPI 3.x:** See [**ITAddress::Forward**](/windows/desktop/api/tapi3if/nf-tapi3if-itaddress-forward).

 

 
