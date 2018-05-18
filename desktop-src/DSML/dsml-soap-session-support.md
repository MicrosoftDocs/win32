---
title: DSML SOAP Session Support
description: DSML SOAP Session Support
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'ee619eb4-3266-4b1a-bc93-ef80d4a37d2a'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["DSML SOAP Session Support DSML"]
---

# DSML SOAP Session Support

The [SOAP specification](http://go.microsoft.com/fwlink/p/?linkid=84162) recommends using SOAP headers for building new protocols on top of SOAP messages.

Some LDAP controls, such as PageSize, require stateful support. A state must be maintained from one request to another request. In a typical scenario, a client makes a request; the server then returns the response with a cookie. The client is required to return the same cookie in the next request within the same connection. The cookie usually has an expiration time attached to it, and the server can refuse the client request if the cookie has expired.

A DSML SOAP session will be implemented as XML data in the SOAP header. The DSML SOAP session namespace is as follows:

`xmlns="urn:schema-microsoft-com:activedirectory:dsmlv2"`

The following table lists the SOAP header elements for building session support in DSML V2.



| Element          | Description                                                                                                                                                                                                                                       |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BeginSession** | Request to the server to start the session.                                                                                                                                                                                                       |
| **Session**      | Server response, which includes a session ID unique only to this connection. The client also uses the **Session** element to continue sending subsequent requests through a session that was previously opened with the **BeginSession** element. |
| **EndSession**   | The client uses this header to terminate the session.                                                                                                                                                                                             |



 

> [!Note]  
> For any given SOAP header, the operation can appear only once. For example, you cannot combine **BeginSession** with **EndSession**; you must issue **BeginSession** and **EndSession** separately.

 

 

 




