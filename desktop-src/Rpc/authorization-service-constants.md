---
title: Authorization-Service Constants
description: The authorization service constants represent the authorization services passed to various run-time functions.
ms.assetid: b773bb51-7af0-4eb3-9438-fe3ef9a350db
topic_type:
- apiref
api_name:
- RPC_C_AUTHZ_NONE
- RPC_C_AUTHZ_NAME
- RPC_C_AUTHZ_DCE
- RPC_C_AUTHZ_DEFAULT
api_location:
- Rpcdce.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Authorization-Service Constants

The authorization service constants represent the authorization services passed to various run-time functions.

The following constants are valid values for the *AuthzSvc* parameter. Most applications find RPC\_C\_AUTHZ\_NON sufficient.



| Constant/value                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                  |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RPC_C_AUTHZ_NONE"></span><span id="rpc_c_authz_none"></span><dl> <dt>**RPC\_C\_AUTHZ\_NONE**</dt> <dt>0</dt> </dl>                   | Server performs no authorization.<br/>                                                                                                                                                                                                                                                                 |
| <span id="RPC_C_AUTHZ_NAME"></span><span id="rpc_c_authz_name"></span><dl> <dt>**RPC\_C\_AUTHZ\_NAME**</dt> <dt>1</dt> </dl>                   | Server performs authorization based on the client's principal name.<br/>                                                                                                                                                                                                                               |
| <span id="RPC_C_AUTHZ_DCE"></span><span id="rpc_c_authz_dce"></span><dl> <dt>**RPC\_C\_AUTHZ\_DCE**</dt> <dt>2</dt> </dl>                      | Server performs authorization checking using the client's DCE privilege attribute certificate (PAC) information, which is sent to the server with each remote procedure call made using the binding handle. Generally, access is checked against DCE access control lists ([ACLs](https://msdn.microsoft.com/library/windows/desktop/aa374931)).<br/> |
| <span id="RPC_C_AUTHZ_DEFAULT"></span><span id="rpc_c_authz_default"></span><dl> <dt>**RPC\_C\_AUTHZ\_DEFAULT**</dt> <dt>0xffffffff</dt> </dl> | Server uses the default authorization service for the current SSP.<br/>                                                                                                                                                                                                                                |



## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Rpcdce.h</dt> </dl> |



## See also

<dl> <dt>

[**RpcBindingInqAuthInfo**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindinginqauthinfo?branch=master)
</dt> <dt>

[**RpcBindingSetAuthInfo**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindingsetauthinfo?branch=master)
</dt> <dt>

[**RpcBindingInqAuthClient**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindinginqauthclient?branch=master)
</dt> <dt>

[**RpcBindingInqAuthClientEx**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindinginqauthclientex?branch=master)
</dt> <dt>

[**RpcBindingSetAuthInfoEx**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindingsetauthinfoexa?branch=master)
</dt> <dt>

[**RpcBindingInqAuthInfoEx**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindinginqauthinfoexa?branch=master)
</dt> <dt>

[**RpcMgmtInqDefaultProtectLevel**](/windows/win32/Rpcdce/nf-rpcdce-rpcmgmtinqdefaultprotectlevel?branch=master)
</dt> </dl>

 

 





