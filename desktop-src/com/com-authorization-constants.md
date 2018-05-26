---
title: Authorization Constants
description: Defines what the server authorizes.
ms.assetid: a0bc9337-b7e4-41c5-ae36-4843fa7d98ce
topic_type:
- apiref
api_name:
- RPC_C_AUTHZ_NONE
- RPC_C_AUTHZ_NAME
- RPC_C_AUTHZ_DCE
- RPC_C_AUTHZ_DEFAULT
api_location:
- RpcDce.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Authorization Constants

Defines what the server authorizes.



| Constant/value                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                       |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RPC_C_AUTHZ_NONE"></span><span id="rpc_c_authz_none"></span><dl> <dt>**RPC\_C\_AUTHZ\_NONE**</dt> <dt>0</dt> </dl>                   | The server performs no authorization. Currently, RPC\_C\_AUTHN\_WINNT, RPC\_C\_AUTHN\_GSS\_SCHANNEL, and RPC\_C\_AUTHN\_GSS\_KERBEROS all use only RPC\_C\_AUTHZ\_NONE.<br/>                                                                                                                |
| <span id="RPC_C_AUTHZ_NAME"></span><span id="rpc_c_authz_name"></span><dl> <dt>**RPC\_C\_AUTHZ\_NAME**</dt> <dt>1</dt> </dl>                   | The server performs authorization based on the client's principal name. <br/>                                                                                                                                                                                                               |
| <span id="RPC_C_AUTHZ_DCE"></span><span id="rpc_c_authz_dce"></span><dl> <dt>**RPC\_C\_AUTHZ\_DCE**</dt> <dt>2</dt> </dl>                      | The server performs authorization checking using the client's DCE privilege attribute certificate (PAC) information, which is sent to the server with each remote procedure call made using the binding handle. Generally, access is checked against DCE access control lists (ACLs). <br/> |
| <span id="RPC_C_AUTHZ_DEFAULT"></span><span id="rpc_c_authz_default"></span><dl> <dt>**RPC\_C\_AUTHZ\_DEFAULT**</dt> <dt>0xffffffff</dt> </dl> | DCOM can choose the authorization level using its normal security blanket negotiation algorithm. For more information, see [Security Blanket Negotiation](security-blanket-negotiation.md).<br/>                                                                                           |



## Remarks

These constants are used by methods of the [**IClientSecurity**](/windows/win32/ObjIdl/nn-objidl-iclientsecurity?branch=master) interface. They are used in the [**SOLE\_AUTHENTICATION\_SERVICE**](/windows/win32/objidlbase/ns-objidl-tagsole_authentication_service?branch=master) structure, which is retrieved by the [**CoQueryAuthenticationServices**](/windows/win32/combaseapi/nf-combaseapi-coqueryauthenticationservices?branch=master) function. They are also used in the [**SOLE\_AUTHENTICATION\_INFO**](/windows/win32/objidlbase/ns-objidl-tagsole_authentication_info?branch=master) structure, which in turn is a member of the [**SOLE\_AUTHENTICATION\_LIST**](/windows/win32/objidlbase/ns-objidl-tagsole_authentication_list?branch=master) structure. This structure, which is a list of authentication services, the authorization services they perform, and the authentication information for each service, is passed to the [**CoInitializeSecurity**](/windows/win32/combaseapi/nf-combaseapi-coinitializesecurity?branch=master) function and the [**IClientSecurity::SetBlanket**](/windows/win32/objidlbase/nf-objidl-iclientsecurity-setblanket?branch=master) method.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>RpcDce.h</dt> </dl> |



## See also

<dl> <dt>

[**CoInitializeSecurity**](/windows/win32/combaseapi/nf-combaseapi-coinitializesecurity?branch=master)
</dt> <dt>

[**CoQueryAuthenticationServices**](/windows/win32/combaseapi/nf-combaseapi-coqueryauthenticationservices?branch=master)
</dt> <dt>

[**IClientSecurity**](/windows/win32/ObjIdl/nn-objidl-iclientsecurity?branch=master)
</dt> <dt>

[**SOLE\_AUTHENTICATION\_INFO**](/windows/win32/objidlbase/ns-objidl-tagsole_authentication_info?branch=master)
</dt> <dt>

[**SOLE\_AUTHENTICATION\_SERVICE**](/windows/win32/objidlbase/ns-objidl-tagsole_authentication_service?branch=master)
</dt> </dl>

 

 





