---
title: Authentication Service Constants (RpcDce.h)
description: Defines authentication services by identifying the security package that provides the service, such as NTLMSSP, Kerberos, or Schannel.
ms.assetid: c16a8e52-a7f9-40d9-99ef-10b382b5cb3c
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
- RPC_C_AUTHN_KERNEL
- RPC_C_AUTHN_DIGEST
- RPC_C_AUTHN_NEGO_EXTENDER
- RPC_C_AUTHN_PKU2U
- RPC_C_AUTHN_MQ
- RPC_C_AUTHN_DEFAULT
api_location:
- RpcDce.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Authentication Service Constants

Defines authentication services by identifying the security package that provides the service, such as NTLMSSP, Kerberos, or Schannel.



| Constant/value                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                    |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RPC_C_AUTHN_NONE"></span><span id="rpc_c_authn_none"></span><dl> <dt>**RPC\_C\_AUTHN\_NONE**</dt> <dt>0</dt> </dl>                              | No authentication.<br/>                                                                                                                                                                                                                                                  |
| <span id="RPC_C_AUTHN_DCE_PRIVATE"></span><span id="rpc_c_authn_dce_private"></span><dl> <dt>**RPC\_C\_AUTHN\_DCE\_PRIVATE**</dt> <dt>1</dt> </dl>        | DCE private key authentication.<br/>                                                                                                                                                                                                                                     |
| <span id="RPC_C_AUTHN_DCE_PUBLIC"></span><span id="rpc_c_authn_dce_public"></span><dl> <dt>**RPC\_C\_AUTHN\_DCE\_PUBLIC**</dt> <dt>2</dt> </dl>           | DCE public key authentication.<br/>                                                                                                                                                                                                                                      |
| <span id="RPC_C_AUTHN_DEC_PUBLIC"></span><span id="rpc_c_authn_dec_public"></span><dl> <dt>**RPC\_C\_AUTHN\_DEC\_PUBLIC**</dt> <dt>4</dt> </dl>           | DEC public key authentication. Reserved for future use.<br/>                                                                                                                                                                                                             |
| <span id="RPC_C_AUTHN_GSS_NEGOTIATE"></span><span id="rpc_c_authn_gss_negotiate"></span><dl> <dt>**RPC\_C\_AUTHN\_GSS\_NEGOTIATE**</dt> <dt>9</dt> </dl>  | Snego security support provider.<br/>                                                                                                                                                                                                                                    |
| <span id="RPC_C_AUTHN_WINNT"></span><span id="rpc_c_authn_winnt"></span><dl> <dt>**RPC\_C\_AUTHN\_WINNT**</dt> <dt>10</dt> </dl>                          | NTLMSSP<br/>                                                                                                                                                                                                                                                             |
| <span id="RPC_C_AUTHN_GSS_SCHANNEL"></span><span id="rpc_c_authn_gss_schannel"></span><dl> <dt>**RPC\_C\_AUTHN\_GSS\_SCHANNEL**</dt> <dt>14</dt> </dl>    | Schannel security support provider. This authentication service supports SSL 2.0, SSL 3.0, TLS, and PCT.<br/>                                                                                                                                                            |
| <span id="RPC_C_AUTHN_GSS_KERBEROS"></span><span id="rpc_c_authn_gss_kerberos"></span><dl> <dt>**RPC\_C\_AUTHN\_GSS\_KERBEROS**</dt> <dt>16</dt> </dl>    | Kerberos security support provider.<br/>                                                                                                                                                                                                                                 |
| <span id="RPC_C_AUTHN_DPA"></span><span id="rpc_c_authn_dpa"></span><dl> <dt>**RPC\_C\_AUTHN\_DPA**</dt> <dt>17</dt> </dl>                                | DPA security support provider.<br/>                                                                                                                                                                                                                                      |
| <span id="RPC_C_AUTHN_MSN"></span><span id="rpc_c_authn_msn"></span><dl> <dt>**RPC\_C\_AUTHN\_MSN**</dt> <dt>18</dt> </dl>                                | MSN security support provider.<br/>                                                                                                                                                                                                                                      |
| <span id="RPC_C_AUTHN_KERNEL"></span><span id="rpc_c_authn_kernel"></span><dl> <dt>**RPC\_C\_AUTHN\_KERNEL**</dt> <dt>20</dt> </dl>                       | Kernel security support provider.<br/>                                                                                                                                                                                                                                   |
| <span id="RPC_C_AUTHN_DIGEST"></span><span id="rpc_c_authn_digest"></span><dl> <dt>**RPC\_C\_AUTHN\_DIGEST**</dt> <dt>21</dt> </dl>                       | Digest security support provider.<br/>                                                                                                                                                                                                                                   |
| <span id="RPC_C_AUTHN_NEGO_EXTENDER"></span><span id="rpc_c_authn_nego_extender"></span><dl> <dt>**RPC\_C\_AUTHN\_NEGO\_EXTENDER**</dt> <dt>30</dt> </dl> | NEGO extender security support provider.<br/>                                                                                                                                                                                                                            |
| <span id="RPC_C_AUTHN_PKU2U"></span><span id="rpc_c_authn_pku2u"></span><dl> <dt>**RPC\_C\_AUTHN\_PKU2U**</dt> <dt>31</dt> </dl>                          | PKU2U security support provider.<br/>                                                                                                                                                                                                                                    |
| <span id="RPC_C_AUTHN_MQ"></span><span id="rpc_c_authn_mq"></span><dl> <dt>**RPC\_C\_AUTHN\_MQ**</dt> <dt>100</dt> </dl>                                  | MQ security support provider.<br/>                                                                                                                                                                                                                                       |
| <span id="RPC_C_AUTHN_DEFAULT"></span><span id="rpc_c_authn_default"></span><dl> <dt>**RPC\_C\_AUTHN\_DEFAULT**</dt> <dt>0xFFFFFFFFL</dt> </dl>           | The system default authentication service. When this value is specified, COM uses its normal security blanket negotiation algorithm to pick an authentication service. For more information, see [Security Blanket Negotiation](security-blanket-negotiation.md). <br/> |



## Remarks

These constants are used in the [**SOLE\_AUTHENTICATION\_SERVICE**](/windows/win32/api/objidlbase/ns-objidlbase-sole_authentication_service) and the [**SOLE\_AUTHENTICATION\_INFO**](/windows/win32/api/objidlbase/ns-objidlbase-sole_authentication_info) structures. The **SOLE\_AUTHENTICATION\_SERVICE** structure is passed by the server to the [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) function and can be retrieved by the [**CoQueryAuthenticationServices**](/windows/desktop/api/combaseapi/nf-combaseapi-coqueryauthenticationservices) function. A pointer to a **SOLE\_AUTHENTICATION\_INFO** structure is passed by the client to **CoInitializeSecurity**. For more information on the security packages identified by these values, such as NTLMSSP and Kerberos, see [COM and Security Packages](com-and-security-packages.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>RpcDce.h</dt> </dl> |



## See also

<dl> <dt>

[**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity)
</dt> <dt>

[**CoQueryAuthenticationServices**](/windows/desktop/api/combaseapi/nf-combaseapi-coqueryauthenticationservices)
</dt> <dt>

[**IClientSecurity**](/windows/desktop/api/ObjIdl/nn-objidl-iclientsecurity)
</dt> <dt>

[**SOLE\_AUTHENTICATION\_INFO**](/windows/win32/api/objidlbase/ns-objidlbase-sole_authentication_info)
</dt> <dt>

[**SOLE\_AUTHENTICATION\_SERVICE**](/windows/win32/api/objidlbase/ns-objidlbase-sole_authentication_service)
</dt> </dl>

 

