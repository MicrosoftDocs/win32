---
title: Null Sessions
description: Sometimes a call arriving on the null session can appear like an authenticated call.
ms.assetid: 5d113d20-c7af-4fb3-ba17-d0715671f290
ms.topic: article
ms.date: 05/31/2018
---

# Null Sessions

Sometimes a call arriving on the null session can appear like an authenticated call. Specifically, calling the [**RpcBindingInqAuthClient**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindinginqauthclient) function returns the authentication level and security provider used for the call. This operation does not mean the call was not on a null session. The two issues are orthogonal. On Microsoft Windows 2000, a remote procedure call can attempt to impersonate a caller and check the permissions after impersonation. On Microsoft Windows XP, it is faster to call the [**RpcServerInqCallAttributes**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcserverinqcallattributesa) function and check for the **NullSession** flag.

Another relevant difference exists between Windows 2000 and Windows XP. If only the RPC\_IF\_ALLOW\_SECURE\_ONLY flag is specified, calls on the null session go through in Windows 2000. In Windows XP, with the general tightening of default security settings, when this flag is specified, calls on the null session are rejected with access denied. However, even with the RPC\_IF\_ALLOW\_SECURE\_ONLY flag, RPC does not guarantee the privilege level of the calling user. All RPC checks is that the user has valid credentials. It is possible that the calling user is using the guest account or other low privileged accounts. Make sure the server does not assume high privilege once RPC\_IF\_ALLOW\_SECURE\_ONLY is used.

 

 




