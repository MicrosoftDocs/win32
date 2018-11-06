---
title: Which Security Provider to Use
description: All other things being equal, use RPC\_C\_AUTHN\_GSS\_KERBEROS or RPC\_C\_AUTHN\_GSS\_NEGOTIATE.
ms.assetid: 921975ae-17e7-433a-bbc5-e6b95989d31a
ms.topic: article
ms.date: 05/31/2018
---

# Which Security Provider to Use

All other things being equal, use RPC\_C\_AUTHN\_GSS\_KERBEROS or RPC\_C\_AUTHN\_GSS\_NEGOTIATE. Each provides the most scalable and secure service. If you use RPC\_C\_AUTHN\_GSS\_NEGOTIATE on the server, this allows down-level clients, such as NTLM clients, to connect to your server. If that is undesirable, either limit the choice to RPC\_C\_AUTHN\_GSS\_KERBEROS only, or call [**RpcBindingInqAuthClientEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindinginqauthclientex) to determine which security provider the client is using, and deny access to clients using NTLM. The preferred method of establishing which security provider the client is using is the [**RpcServerInqCallAttributes**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcserverinqcallattributesa) function.

 

 




