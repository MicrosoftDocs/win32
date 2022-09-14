---
description: Explains how to establish a security context that protects communications between a client and server.
ms.assetid: eb1eadb2-14b2-4265-994a-dcea4208e650
title: Creating an Schannel Security Context
ms.topic: article
ms.date: 05/31/2018
---

# Creating an Schannel Security Context

To establish a [*security context*](/windows/desktop/SecGloss/s-gly) that will protect communications between a client and server, both must participate in the following information exchange process:

## Client

1.  The client calls the [**InitializeSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-initializesecuritycontexta) function.
2.  Schannel begins creating a security context according to the rules of the selected security protocol. The function's return code indicates whether the client must call the function again. [**InitializeSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-initializesecuritycontexta) may return a token that represents the context.
3.  If a token was returned, the client sends it to the server.
4.  When [**InitializeSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-initializesecuritycontexta) returns SEC\_E\_OK, the client is done. If the function returns SEC\_I\_CONTINUE\_NEEDED, the client must wait for the server to send it a token. When the client has the token from the server, it must call the **InitializeSecurityContext (General)** [*function*](/windows/desktop/SecGloss/c-gly) again. (Return to step 2.)

## Server

1.  The server waits for a client to send a message that contains a security token. The server passes the token received from the client into the [**AcceptSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-acceptsecuritycontext) function.
2.  Schannel builds on the partial security context represented by the token. Schannel returns a token to the server, and a return code indicating whether the server must call the function again.
3.  If a token was returned, the server sends it to the client.
4.  When [**AcceptSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-acceptsecuritycontext) returns SEC\_E\_OK, the server is done. If the function returns SEC\_I\_CONTINUE\_NEEDED, then the server must wait for the client to send it a token. When the server has the token from the client, it must call the **AcceptSecurityContext (General)** function again. (Return to step 2.)

If either function returns a value other than SEC\_E\_OK, SEC\_I\_CONTINUE\_NEEDED, or SEC\_E\_INCOMPLETE\_MESSAGE (see the following paragraph) an error has occurred. The client and server should call the [**DeleteSecurityContext**](/windows/desktop/api/Sspi/nf-sspi-deletesecuritycontext) function to delete the partially established security context.

A special case that can alter client and server processing is when too little or too much information is sent to the client or server from the other party. In the case of too little information, both functions return SEC\_E\_INCOMPLETE\_MESSAGE. For information about recognizing and handling insufficient or excess information, see [Extra buffers Returned by Schannel](extra-buffers-returned-by-schannel.md).

## Related topics

<dl> <dt>

[Performing Authentication Using Schannel](performing-authentication-using-schannel.md)
</dt> <dt>

[Mapping Certificates](mapping-certificates.md)
</dt> <dt>

[Manually Validating Schannel Credentials](manually-validating-schannel-credentials.md)
</dt> </dl>

 

 
