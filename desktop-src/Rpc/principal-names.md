---
title: Principal Names
description: For a client to create a mutually authenticated session with a server program, it must provide the server's expected principal name.
ms.assetid: 4d9977f8-0efb-4559-977e-3eba4e277bc0
ms.topic: article
ms.date: 05/31/2018
---

# Principal Names

For a client to create a mutually authenticated session with a server program, it must provide the server's expected principal name. Some protocols, such as Kerberos, require a correct server principal name for any authenticated session. A principal is an entity that the security system recognizes. This includes human users as well as system services. All principal names take similar format for a given security support provider (SSP). An SSP is a software module that performs security validation. For more information, see [SSPI Architectural Overview](sspi-architectural-overview.md). To maintain uniformity, a security provider usually gives system services similar names as users. Under some security providers, system services may not have a principal name.

The server registers its principal name for the security provider using the [**RpcServerRegisterAuthInfo**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterauthinfo) function. Only one server principal name can be used for each security provider. If more than one name is registered, one name is randomly chosen and used. The SSP dictates the format of the principal name. For example, the Kerberos/Negotiate SSPs for a system service look approximately like the following: machine\_name$@childdomain.parentdomain1.parentdomain2.COM.

The recommended procedure for generating principal names is to use documented APIs (such as the **DsMakeSpn** function), rather than piecing together the principal name from strings. Using documented APIs increases portability between different deployment environments and eliminates the possibility for errors.

Specifying an incorrect principal name may prevent the client and server from establishing an authenticated session. The SCHANNEL SSP takes principal names in either of two forms:

-   The first SCHANNEL principal name form is the [*msstd*](m-glos.md) form. Names in msstd form generally follow the pattern msstd:servername@serverdomain.com. This is referred to as an email name property. If the certificate contains an email name property, and it contains the at sign (@), the principal name is msstd:email name. Otherwise it must contain the common name property. Internal backslashes are doubled, just as in string bindings.
-   The second SCHANNEL principal name form is the [*fullsic*](f-glos.md) form. This is a series of RFC1779-compliant names bounded by angle brackets and separated by backslashes. It typically follows the pattern fullsic:\\<\\Authority\\SubAuthority\\.....\\Person> or fullsic:\\<\\Authority\\SubAuthority\\.....\\ServerProgram>.

If the name does not match the certificate, ERROR\_ACCESS\_DENIED is returned. If the name format is invalid, SCHANNEL SSP returns the code ERROR\_INVALID\_PARAMETER.

To query for the server's principal name, applications can call [**RpcMgmtInqServerPrincName**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtinqserverprincname). This allocates a null-terminated string to hold the principal name. Before it terminates, your application must invoke [**RpcStringFree**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcstringfree) to release the memory this string occupies.

Querying for the server name in this manner is not secure and should be avoided. For server authentication, the client program should know which server it is connecting to and should create the server principal name from scratch.

 

 




