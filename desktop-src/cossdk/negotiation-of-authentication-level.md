---
description: Negotiation of Authentication Level
ms.assetid: 31353d02-bfe2-48ac-81a1-0e38895a8a75
title: Negotiation of Authentication Level
ms.topic: article
ms.date: 05/31/2018
---

# Negotiation of Authentication Level

Both client and server must participate in authentication, and each party indicates that it wants to perform a certain level of authentication. At the beginning of a call, the authentication level is negotiated between the two parties, an appropriate service is chosen, and the call is authenticated and proceeds (with possible encryption, depending on the authentication level chosen). The authentication level negotiated between client and server is determined as Maximum(*Client preference*, *Server preference*). The effect of this means that the server can always dictate a minimum level of authentication that it is comfortable with; that is, authentication can be administratively dictated from the server.

The client specifies that it wants to perform authentication at a certain level as with any COM application. The client authentication level can be indicated as follows:

-   Per client machine, with the machine-wide COM authentication level set by using either [DCOMCNFG](/windows/desktop/com/setting-machine-wide-security-using-dcomcnfg) or the Component Services administrative tool.
-   Per client application administratively, using [DCOMCNFG](/windows/desktop/com/setting-processwide-security-using-dcomcnfg) or using the Component Services administrative tool if the client should be a COM+ application.
-   Per client process programmatically, with [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity).
-   At any point programmatically, using [**CoSetProxyBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-cosetproxyblanket).

The COM+ server application specifies an authentication level administratively by using the Component Services administrative tool (or through an administrative script).

Negotiating authentication for a call proceeds in the following sequence:

1.  Authentication level is chosen as MAX(*client*, *server*).
2.  Negotiation of authentication protocol.
3.  Server authenticates client identity.
4.  Optionally, client authenticates server identity, depending on the authentication protocol.
5.  Method calls are communicated with the chosen level of authentication.

## Related topics

<dl> <dt>

[Client Authentication](client-authentication.md)
</dt> </dl>

 

 
