---
title: Impersonation Level Constants (RpcDce.h)
description: Specifies an impersonation level, which indicates the amount of authority given to the server when it is impersonating the client.
ms.assetid: ea5a3b46-b607-4192-a3cc-b2ec55ca94a6
topic_type:
- apiref
api_name:
- RPC_C_IMP_LEVEL_DEFAULT
- RPC_C_IMP_LEVEL_ANONYMOUS
- RPC_C_IMP_LEVEL_IDENTIFY
- RPC_C_IMP_LEVEL_IMPERSONATE
- RPC_C_IMP_LEVEL_DELEGATE
api_location:
- RpcDce.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Impersonation Level Constants

Specifies an impersonation level, which indicates the amount of authority given to the server when it is impersonating the client.



| Constant/value                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RPC_C_IMP_LEVEL_DEFAULT"></span><span id="rpc_c_imp_level_default"></span><dl> <dt>**RPC\_C\_IMP\_LEVEL\_DEFAULT**</dt> <dt>0</dt> </dl>             | DCOM can choose the impersonation level using its normal security blanket negotiation algorithm. For more information, see [Security Blanket Negotiation](security-blanket-negotiation.md).<br/>                                                                                                                                                                                                                                                                           |
| <span id="RPC_C_IMP_LEVEL_ANONYMOUS"></span><span id="rpc_c_imp_level_anonymous"></span><dl> <dt>**RPC\_C\_IMP\_LEVEL\_ANONYMOUS**</dt> <dt>1</dt> </dl>       | The client is anonymous to the server. The server process can impersonate the client, but the impersonation token will not contain any information and cannot be used.<br/>                                                                                                                                                                                                                                                                                                 |
| <span id="RPC_C_IMP_LEVEL_IDENTIFY"></span><span id="rpc_c_imp_level_identify"></span><dl> <dt>**RPC\_C\_IMP\_LEVEL\_IDENTIFY**</dt> <dt>2</dt> </dl>          | The server can obtain the client's identity. The server can impersonate the client for ACL checking, but it cannot access system objects as the client. <br/>                                                                                                                                                                                                                                                                                                               |
| <span id="RPC_C_IMP_LEVEL_IMPERSONATE"></span><span id="rpc_c_imp_level_impersonate"></span><dl> <dt>**RPC\_C\_IMP\_LEVEL\_IMPERSONATE**</dt> <dt>3</dt> </dl> | The server process can impersonate the client's security context while acting on behalf of the client. This level of impersonation can be used to access local resources such as files. When impersonating at this level, the impersonation token can only be passed across one machine boundary. The [Schannel](schannel.md) authentication service only supports this level of impersonation. <br/>                                                                      |
| <span id="RPC_C_IMP_LEVEL_DELEGATE"></span><span id="rpc_c_imp_level_delegate"></span><dl> <dt>**RPC\_C\_IMP\_LEVEL\_DELEGATE**</dt> <dt>4</dt> </dl>          | The server process can impersonate the client's security context while acting on behalf of the client. The server process can also make outgoing calls to other servers while acting on behalf of the client, using cloaking. The server may use the client's security context on other machines to access local and remote resources as the client. When impersonating at this level, the impersonation token can be passed across any number of computer boundaries.<br/> |



## Remarks

[**GetUserName**](/windows/desktop/api/winbase/nf-winbase-getusernamea) will fail while impersonating at identify level. The workaround is to impersonate, call [**OpenThreadToken**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-openthreadtoken), revert, call [**GetTokenInformation**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-gettokeninformation), and finally, call [**LookupAccountSid**](/windows/desktop/api/winbase/nf-winbase-lookupaccountsida). Using [**CoSetProxyBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-cosetproxyblanket), the client sets the impersonation level

Using [**CoSetProxyBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-cosetproxyblanket), the client sets the impersonation level and proxy identity that will be available when a server calls [**CoImpersonateClient**](/windows/desktop/api/combaseapi/nf-combaseapi-coimpersonateclient). The identity the server will see when impersonating takes place is described in [Cloaking](cloaking.md). Note that when making a call while impersonating, the callee will normally receive the caller's process token, not the caller's impersonation token. To receive the caller's impersonation token, the caller must enable cloaking.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>RpcDce.h</dt> </dl> |



## See also

<dl> <dt>

[Cloaking](cloaking.md)
</dt> </dl>

 

