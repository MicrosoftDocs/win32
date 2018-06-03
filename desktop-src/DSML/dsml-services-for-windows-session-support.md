---
title: DSML Services for Windows Session Support
description: DSML Services for Windows Session Support
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: c9920590-bcba-463f-a62d-a08d4dc355e8
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- DSML Services for Windows Session Support DSML
- Windows session support
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DSML Services for Windows Session Support

DSML V2 was designed to be used with a request/response protocol such as HTTP. For a given request document, a DSML V2 server/gateway is expected to produce a corresponding response document. No state is carried between one request to another request, so each request is completely independent of the other.

One of the benefits of this approach is to free the server from maintaining states, which promotes scalability. This design is also aligned with one of the goals of DSML V2: transport independence. Because most transport protocols include session support, DSML V2 can still be implemented on top of these protocols and take advantage of their session support.

However, the design also introduces several challenges for LDAP operations that require session support. DSML Services for Windows implements session support in the SOAP transport layer.

For more information on session support, see the following topics:

-   [DSML SOAP Session Support](dsml-soap-session-support.md)
-   [Session Support Example](session-support-example.md)
-   [Session Characteristics](session-characteristics.md)
-   [LDAP Controls and Session Support](ldap-controls-and-session-support.md)

 

 




