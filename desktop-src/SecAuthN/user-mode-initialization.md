---
Description: 'Distributed (client/server) applications use security packages to obtain authenticated connections and to exchange messages.'
ms.assetid: '8f28177f-335a-4fa2-bf66-2ec1698bebec'
title: User Mode Initialization
---

# User Mode Initialization

Distributed (client/server) applications use [*security packages*](security.s_gly#-security-security-package-gly) to obtain authenticated connections and to exchange messages. The application calls security support provider interface (SSPI) functions which are mapped to [functions implemented by SSP/APs](authentication-functions.md#functions-implemented-by-sspaps), and [functions implemented by User-mode SSP/APs](authentication-functions.md#functions-implemented-by-user-mode-sspaps). This mapping is performed by the security provider DLL (Secur32.dll or Security.dll), which can be loaded into the client and server processes dynamically. The DLL can also be statically linked using Secur32.lib. Both the DLL and LIB ship with the Microsoft Windows Software Development Kit (SDK).

Loading the security package into the client or server's process is handled by the system, if the SSP/AP DLL that contains the security package is properly registered.

The server begins the process of obtaining a secure connection with a client by monitoring a port, waiting for a client to send a message. The client begins the process of obtaining a secure connection to the server by calling the SSPI function [**InitializeSecurityContext (General)**](initializesecuritycontext--general-.md). This function is mapped to the custom security package's [**SpInitLsaModeContext**](spinitlsamodecontext.md) function. **SpInitLsaModeContext** returns a token to the client, who forwards it to the server.

Upon receiving the token from the client, the server calls the SSPI function [**AcceptSecurityContext (General)**](acceptsecuritycontext--general-.md), which is dispatched to the security package's [**SpAcceptLsaModeContext**](spacceptlsamodecontext.md) function. If the **SpAcceptLsaModeContext** function succeeds and no more processing is required to establish the security context, the function should return STATUS\_SUCCESS to the caller. If additional processing is required, the function should return SEC\_I\_CONTINUE\_NEEDED, and return a token to the server. The server forwards the token to the client, who calls [**InitializeSecurityContext (General)**](initializesecuritycontext--general-.md) again.

This calling cycle may be repeated as often as necessary until an authenticated connection is established or fails. During this process, if the [**SpAcceptLsaModeContext**](spacceptlsamodecontext.md) or [**SpInitLsaModeContext**](spinitlsamodecontext.md) function succeeds and no more processing is required to establish the [*security context*](security.s_gly#-security-security-context-gly), the function should return STATUS\_SUCCESS to the caller. If additional processing is required, the function should return SEC\_I\_CONTINUE\_NEEDED, and return a token to the caller, who is responsible for forwarding it.

The protocol implemented by the security package determines the number of times this cycle is repeated. For example, in security packages that supports three-leg mutual authentication, the calling sequence is as follows:

1.  Client obtains a token by calling [**InitializeSecurityContext (General)**](initializesecuritycontext--general-.md), and sends it to the server. The server calls [**AcceptSecurityContext (General)**](acceptsecuritycontext--general-.md) the first time, and gets back a reply token which it sends to the client.
2.  The client uses the token received from the server in a second call to [**InitializeSecurityContext (General)**](initializesecuritycontext--general-.md), and gets back a final token. The client sends this token to the server.
3.  The server receives the token generated in leg 2 which it uses in the final call to [**AcceptSecurityContext (General)**](acceptsecuritycontext--general-.md).

When the [**SpAcceptLsaModeContext**](spacceptlsamodecontext.md) and [**SpInitLsaModeContext**](spinitlsamodecontext.md) functions succeed and no more processing is required to establish the security context, the functions should return STATUS\_SUCCESS to the caller. Additionally, if the custom security package supports the [functions implemented by user-mode SSP/APs](authentication-functions.md#functions-implemented-by-user-mode-sspaps), **SpAcceptLsaModeContext** and **SpInitLsaModeContext** must return **TRUE** by way of the *MappedContext* parameter. The *MappedContext* value is not passed back to the application; it is intercepted by the LSA.

When *MappedContext* is **true**, the LSA calls the SSP/AP DLL's [**SpUsermodeInitialize**](spusermodeinitialize.md) function. This function provides tables of pointers to the user-mode functions implemented by each security package. Each package's [**SpInstanceInit**](spinstanceinit.md) function is called, using the function tables returned by **SpUsermodeInitialize**. **SpInstanceInit** receives a table of pointers to [LSA functions called by user-mode SSP/APs](authentication-functions.md#lsa-functions-called-by-user-mode-sspaps).

 

 



