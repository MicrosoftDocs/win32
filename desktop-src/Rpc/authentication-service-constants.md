---
title: Authentication-Service Constants (Rpcdce.h)
description: The authentication service constants represent the authentication services passed to various run-time functions.
ms.assetid: ac95276f-230d-4993-92fe-1739d022c8b3
topic_type:
- apiref
api_name:
- RPC_C_AUTHN_NONE
- RPC_C_AUTHN_DCE_PRIVATE
- RPC_C_AUTHN_DCE_PUBLIC
- RPC_C_AUTHN_DEC_PUBLIC
- RPC_C_AUTHN_GSS_NEGOTIATE
- RPC_C_AUTHN_WINNT
- RPC_C_AUTHN_GSS_SCHANNEL
- RPC_C_AUTHN_GSS_KERBEROS
- RPC_C_AUTHN_DPA
- RPC_C_AUTHN_MSN
- RPC_C_AUTHN_DIGEST
- RPC_C_AUTHN_NEGO_EXTENDER
- RPC_C_AUTHN_MQ
- RPC_C_AUTHN_DEFAULT
api_location:
- Rpcdce.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Authentication-Service Constants

The authentication service constants represent the authentication services passed to various run-time functions.

The following constants are valid values for the *AuthnSvc* parameter.



| Constant/value                                                                                                                                                                                                                                               | Description                                                                                                                                                                          |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RPC_C_AUTHN_NONE"></span><span id="rpc_c_authn_none"></span><dl> <dt>**RPC\_C\_AUTHN\_NONE**</dt> <dt>0</dt> </dl>                              | No authentication.<br/>                                                                                                                                                        |
| <span id="RPC_C_AUTHN_DCE_PRIVATE"></span><span id="rpc_c_authn_dce_private"></span><dl> <dt>**RPC\_C\_AUTHN\_DCE\_PRIVATE**</dt> <dt>1</dt> </dl>        | Use Distributed Computing Environment (DCE) private key authentication.<br/>                                                                                                   |
| <span id="RPC_C_AUTHN_DCE_PUBLIC"></span><span id="rpc_c_authn_dce_public"></span><dl> <dt>**RPC\_C\_AUTHN\_DCE\_PUBLIC**</dt> <dt>2</dt> </dl>           | DCE public key authentication (reserved for future use).<br/>                                                                                                                  |
| <span id="RPC_C_AUTHN_DEC_PUBLIC"></span><span id="rpc_c_authn_dec_public"></span><dl> <dt>**RPC\_C\_AUTHN\_DEC\_PUBLIC**</dt> <dt>4</dt> </dl>           | DEC public key authentication (reserved for future use).<br/>                                                                                                                  |
| <span id="RPC_C_AUTHN_GSS_NEGOTIATE"></span><span id="rpc_c_authn_gss_negotiate"></span><dl> <dt>**RPC\_C\_AUTHN\_GSS\_NEGOTIATE**</dt> <dt>9</dt> </dl>  | Use the [Microsoft Negotiate SSP](/windows/desktop/SecAuthN/microsoft-negotiate). This SSP negotiates between the use of the NTLM and Kerberos protocol Security Support Providers (SSP).<br/>  |
| <span id="RPC_C_AUTHN_WINNT"></span><span id="rpc_c_authn_winnt"></span><dl> <dt>**RPC\_C\_AUTHN\_WINNT**</dt> <dt>10</dt> </dl>                          | Use the [Microsoft NT LAN Manager (NTLM) SSP](/windows/desktop/SecAuthN/microsoft-ntlm).<br/>                                                                                                   |
| <span id="RPC_C_AUTHN_GSS_SCHANNEL"></span><span id="rpc_c_authn_gss_schannel"></span><dl> <dt>**RPC\_C\_AUTHN\_GSS\_SCHANNEL**</dt> <dt>14</dt> </dl>    | Use the [Schannel SSP](/windows/desktop/SecAuthN/secure-channel). This SSP supports Secure Socket Layer (SSL), private communication technology (PCT), and transport level security (TLS).<br/> |
| <span id="RPC_C_AUTHN_GSS_KERBEROS"></span><span id="rpc_c_authn_gss_kerberos"></span><dl> <dt>**RPC\_C\_AUTHN\_GSS\_KERBEROS**</dt> <dt>16</dt> </dl>    | Use the [Microsoft Kerberos SSP](/windows/desktop/SecAuthN/microsoft-kerberos).<br/>                                                                                                            |
| <span id="RPC_C_AUTHN_DPA"></span><span id="rpc_c_authn_dpa"></span><dl> <dt>**RPC\_C\_AUTHN\_DPA**</dt> <dt>17</dt> </dl>                                | Use Distributed Password Authentication (DPA).<br/>                                                                                                                            |
| <span id="RPC_C_AUTHN_MSN"></span><span id="rpc_c_authn_msn"></span><dl> <dt>**RPC\_C\_AUTHN\_MSN**</dt> <dt>18</dt> </dl>                                | Authentication protocol SSP used for the Microsoft Network (MSN).<br/>                                                                                                         |
| <span id="RPC_C_AUTHN_DIGEST"></span><span id="rpc_c_authn_digest"></span><dl> <dt>**RPC\_C\_AUTHN\_DIGEST**</dt> <dt>21</dt> </dl>                       | Windows XP or later: Use the [Microsoft Digest SSP](/windows/desktop/SecAuthN/microsoft-digest-ssp)<br/>                                                                                        |
| <span id="RPC_C_AUTHN_NEGO_EXTENDER"></span><span id="rpc_c_authn_nego_extender"></span><dl> <dt>**RPC\_C\_AUTHN\_NEGO\_EXTENDER**</dt> <dt>30</dt> </dl> | Windows 7 or later: Reserved. Do not use<br/>                                                                                                                                  |
| <span id="RPC_C_AUTHN_MQ"></span><span id="rpc_c_authn_mq"></span><dl> <dt>**RPC\_C\_AUTHN\_MQ**</dt> <dt>100</dt> </dl>                                  | This SSP provides an SSPI-compatible wrapper for the Microsoft Message Queue (MSMQ) transport-level protocol.<br/>                                                             |
| <span id="RPC_C_AUTHN_DEFAULT"></span><span id="rpc_c_authn_default"></span><dl> <dt>**RPC\_C\_AUTHN\_DEFAULT**</dt> <dt>0xffffffff</dt> </dl>            | Use the default authentication service.<br/>                                                                                                                                   |



## Remarks

Specify RPC\_C\_AUTHN\_NONE to turn off authentication for remote procedure calls made over a binding handle. When you specify RPC\_C\_AUTHN\_DEFAULT, the RPC run-time library uses the RPC\_C\_AUTHN\_WINNT authentication service for remote procedure calls made using the binding handle.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Rpcdce.h</dt> </dl> |



## See also

<dl> <dt>

[**RpcBindingInqAuthInfo**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindinginqauthinfo)
</dt> <dt>

[**RpcBindingSetAuthInfo**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetauthinfo)
</dt> <dt>

[**RpcBindingInqAuthClient**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindinginqauthclient)
</dt> <dt>

[**RpcBindingInqAuthClientEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindinginqauthclientex)
</dt> <dt>

[**RpcBindingSetAuthInfoEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetauthinfoexa)
</dt> <dt>

[**RpcBindingInqAuthInfoEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindinginqauthinfoexa)
</dt> </dl>

 

