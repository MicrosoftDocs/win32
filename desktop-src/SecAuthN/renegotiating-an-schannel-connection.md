---
Description: To change a connections attributes, such as the cipher suite or client authentication, you can request a &\#0034;redo&\#0034; or renegotiation of the connection.
ms.assetid: 681b607d-66d8-4012-9a84-d202c9778a26
title: Renegotiating an Schannel Connection
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Renegotiating an Schannel Connection

To change a connection's attributes, such as the cipher suite or client authentication, you can request a "redo" or renegotiation of the connection.

If the attributes you want to change are controlled by credentials, you must obtain new credentials before you renegotiate the connection. For more information, see [Obtaining Schannel Credentials](obtaining-schannel-credentials.md).

To request a redo from a client application, call the [**InitializeSecurityContext (Schannel)**](/windows/win32/Sspi/?branch=master) function. Server applications call the [**AcceptSecurityContext (Schannel)**](/windows/win32/Sspi/?branch=master) function. Set the parameters as follows:

-   Specify the existing [*security context*](security.s_gly#-security-security-context-gly) in the *phContext* parameter.
-   (Clients only) Specify the same server name (in the *pszTargetName* parameter) as specified when establishing the context.
-   Specify new credentials, using the *phCredential* parameter, if applicable.
-   If you want to change context attributes unrelated to the credentials, specify these attributes using the *fContextReq* parameter.

After calling the appropriate function, your application should send the results to the client and continue processing incoming messages using the [**DecryptMessage (Schannel)**](/windows/win32/Sspi/?branch=master) function.

The [**DecryptMessage (Schannel)**](/windows/win32/Sspi/?branch=master) function will return SEC\_I\_RENEGOTIATE when Schannel is ready for your application to proceed. When you receive the SEC\_I\_RENEGOTIATE return code, your application must call [**AcceptSecurityContext (Schannel)**](/windows/win32/Sspi/?branch=master) (servers) or [**InitializeSecurityContext (Schannel)**](/windows/win32/Sspi/?branch=master) (clients), passing in empty input buffers. After this call returns a value, proceed as though your application were creating a new connection.

 

 



