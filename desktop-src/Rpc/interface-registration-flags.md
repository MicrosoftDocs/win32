---
title: Interface Registration Flags (Rpcdce.h)
description: The following constants are used in the Flags parameter of the RpcServerRegisterIf2 and RpcServerRegisterIfEx functions.
ms.assetid: 387311c0-13df-4497-a0ac-ce6aec0e726c
topic_type:
- apiref
api_name:
- RPC_IF_ALLOW_CALLBACKS_WITH_NO_AUTH
- RPC_IF_ALLOW_LOCAL_ONLY
- RPC_IF_AUTOLISTEN
- RPC_IF_OLE
- RPC_IF_ALLOW_UNKNOWN_AUTHORITY
- RPC_IF_ALLOW_SECURE_ONLY
- RPC_IF_SEC_NO_CACHE
api_location:
- Rpcdce.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Interface Registration Flags

The following constants are used in the *Flags* parameter of the [**RpcServerRegisterIf2**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif2) and [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex) functions.




| Constant | Description | 
|----------|-------------|
| <span id="0"></span><dl><dt><strong>0</strong></dt></dl> | Standard interface semantics.<br /> | 
| **RPC_IF_ALLOW_CALLBACKS_WITH_NO_AUTH**<br> | When this interface flag is registered, the RPC runtime invokes the registered security callback for all calls, regardless of identity, protocol sequence, or authentication level of the client.<br> **Note:** This flag is available starting with Windows XP with SP2 and Windows Server 2003 with SP1. When this flag is not set, RPC automatically filters all unauthenticated calls before they reach the security callback.<br> | 
| **RPC_IF_ALLOW_LOCAL_ONLY**<br> | When this interface flag is registered, the RPC runtime rejects calls made by remote clients. All local calls using ncadg_* and ncacn_* protocol sequences are also rejected, with the exception of ncacn_np. RPC allows ncacn_NP calls only if the call does not come from SRV. Calls from ncalrpc are always processed.<br> **Note:** This flag is available starting with Windows XP with SP2 and Windows Server 2003 with SP1.<br> | 
| <span id="RPC_IF_AUTOLISTEN"></span><span id="rpc_if_autolisten"></span><dl><dt><strong>RPC_IF_AUTOLISTEN</strong></dt></dl> | This is an <strong>auto-listen</strong> interface. The run time begins listening for calls as soon as the first autolisten interface is registered, and stops listening when the last autolisten interface is unregistered.<br /> | 
| <span id="RPC_IF_OLE"></span><span id="rpc_if_ole"></span><dl><dt><strong>RPC_IF_OLE</strong></dt></dl> | Reserved for OLE. Do not use this flag.<br /> | 
| <span id="RPC_IF_ALLOW_UNKNOWN_AUTHORITY"></span><span id="rpc_if_allow_unknown_authority"></span><dl><dt><strong>RPC_IF_ALLOW_UNKNOWN_AUTHORITY</strong></dt></dl> | Currently not implemented.<br /> | 
| <span id="RPC_IF_ALLOW_SECURE_ONLY"></span><span id="rpc_if_allow_secure_only"></span><dl><dt><strong>RPC_IF_ALLOW_SECURE_ONLY</strong></dt></dl> | Limits connections to clients that use an authorization level higher than RPC_C_AUTHN_LEVEL_NONE. Specifying this flag allows clients to come through on the <strong>NULL</strong> session. On Windows XP and Windows Server 2003, such clients are not allowed. Clients that fail the RPC_IF_ALLOW_SECURE_ONLY test receive an RPC_S_ACCESS_DENIED error. Using the RPC_IF_ALLOW_SECURE_ONLY flag does not imply or guarantee a high level of privilege on the part of the calling user. RPC only checks that the user has valid credentials; the calling user may be using the guest account or other low privileged accounts. Do not assume high privilege when RPC_IF_ALLOW_SECURE_ONLY is used.<br /><strong>Windows NT 4.0 and Windows Me/98/95:  </strong><br /> | 
| **RPC_IF_SEC_NO_CACHE**<br> | Disables security callback caching, forcing a security callback for each RPC call on a given interface.<br> **Note:** This flag is available starting with Windows XP with SP2 and Windows Server 2003 with SP1.<br> | 




## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Rpcdce.h</dt> </dl> |



 

 





