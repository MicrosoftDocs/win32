---
title: Session Support Example
description: The following code example shows how a DSML Services for Windows session is initiated, maintained, and terminated. For brevity, the actual DSML payload in the SOAP body is eliminated from the example.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: f90fbab0-fb6e-4de2-8a12-128fdacd59dc
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Code Example DSML , Session Support
- Session Support Example DSML
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Session Support Example

The following code example shows how a DSML Services for Windows session is initiated, maintained, and terminated. For brevity, the actual DSML payload in the SOAP body is eliminated from the example.

## Begin the session

To begin the session, the client indicates its intention by sending a **BeginSession** element in the SOAP header. The **mustUnderstand** attribute of the SOAP header must be set to 1. If a server does not support **BeginSession**, per the SOAP specification, it must return a SOAP fault before processing the SOAP body. If the server can establish the session, any DSML operations including the **batchRequest** envelope can run inside the session. If the server cannot establish a session, a SOAP fault will be returned and no DSML operation will be attempted.

Be aware that you can send an empty DSML payload, such as **batchRequest/**, with this request, but not an empty SOAP body without a DSML payload, such as **SOAP-ENV:Body/**. The following code example shows a valid envelope sending an empty payload:


```soap
<SOAP-ENV:Envelope
 xmlns:SOAP-ENV=http://schemas.xmlsoap.org/soap/envelope/>
    <SOAP-ENV:Header>
        <ad:BeginSession
         xmlns:ad="urn:schema-microsoft-com:activedirectory:dsmlv2"
         SOAP-ENV:mustUnderstand="1"/>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <batchRequest/> 
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```



## The server response

Under normal circumstances, the DSML V2 server/gateway will respond with the **Session** element and its associated **SessionID**. When a **SessionID** is established by the server, it remains constant throughout that particular session.

The server must respond by returning a SOAP fault if:

-   One or more **errorResponse** conditions occur.
-   The server declines to give a new session to a client.

The following code example shows how the server responds with the **sessionID**:


```soap
<SOAP-ENV:Envelope
 xmlns:SOAP-ENV=http://schemas.xmlsoap.org/soap/envelope/>
    <SOAP-ENV:Header>
        <ad:Session
         xmlns:ad="urn:schema-microsoft-com:activedirectory:dsmlv2"
         ad:SessionID="1534"/>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <entity type="hellip"/> <!<entity type="mdash"/>DSML Payload Here --> 
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

```



For each subsequent request, the client can send the **sessionID** obtained from the server. The client must still set the **mustUnderstand** SOAP attribute to 1, as shown in the following code example:


```soap
<SOAP-ENV:Envelope
 xmlns:SOAP-ENV=http://schemas.xmlsoap.org/soap/envelope/>
    <SOAP-ENV:Header>
        <ad:Session
         xmlns:ad="urn:schema-microsoft-com:activedirectory:dsmlv2"
         ad:SessionID="1534" 
         SOAP-ENV:mustUnderstand="1"/>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <entity type="hellip"/> <!<entity type="mdash"/>DSML Payload Here --> 
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```



The server then processes the request that is running on the specified session. The server can, at any time, refuse to run the requested session. If the server refuses to run a session, it must send the SOAP fault response before processing any DSML operations.

If the server can run a requested session after processing the DSML operation, the server should send the same data as described earlier for the first server response.

## End a session

To terminate the session, the client sends the **EndSession** request as shown in the following code example. This request instructs the server to terminate the session after processing the DSML operations. If there are any DSML operations to be processed, they must be running in the context of session to be terminated.


```soap
<SOAP-ENV:Envelope
 xmlns:SOAP-ENV=http://schemas.xmlsoap.org/soap/envelope/>
    <SOAP-ENV:Header>
        <ad:EndSession
         xmlns:ad="urn:schema-microsoft-com:activedirectory:dsmlv2"
         ad:SessionID="1534"
         SOAP-ENV:mustUnderstand="1"/>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <entity type="hellip"/> <!<entity type="mdash"/>DSML Payload Here --> 
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```



The server acknowledges the **EndSession** request by returning the **SessionID** of the session that was terminated. If there is a DSML payload, the server will process the operations based on the **SessionID** before terminating it.

Rarely, the server can refuse to close the session. If the server cannot close the connection, for example, because of an invalid **SessionID**, it should respond as a SOAP fault. The server can also time-out and close idle sessions.

It is recommended that clients using a DSML V2 session do so conservatively. If the client no longer requires the session, it should terminate the session as soon as possible. However, the session should not be created and terminated repeatedly over a short period of time, because the resource cost of creating and maintaining sessions on the server side can be great.

Clients must also be prepared to start over from the beginning and resend the session request, by issuing **BeginSession**, if the server rejects the requested session.

 

 




