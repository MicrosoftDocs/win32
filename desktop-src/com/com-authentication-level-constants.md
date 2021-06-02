---
title: Authentication Level Constants (Rpcdce.h)
description: These values specify an authentication level, which indicates the amount of authentication provided to help protect the integrity of the data. Each level includes the protection provided by the previous levels.
ms.assetid: 06c409e4-3772-45cf-8c31-c64f99aca244
topic_type:
- apiref
api_name:
- RPC_C_AUTHN_LEVEL_DEFAULT
- RPC_C_AUTHN_LEVEL_NONE
- RPC_C_AUTHN_LEVEL_CONNECT
- RPC_C_AUTHN_LEVEL_CALL
- RPC_C_AUTHN_LEVEL_PKT
- RPC_C_AUTHN_LEVEL_PKT_INTEGRITY
- RPC_C_AUTHN_LEVEL_PKT_PRIVACY
api_location:
- rpcdce.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Authentication Level Constants

These values specify an authentication level, which indicates the amount of authentication provided to help protect the integrity of the data. Each level includes the protection provided by the previous levels.



| Constant/value                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                    |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RPC_C_AUTHN_LEVEL_DEFAULT"></span><span id="rpc_c_authn_level_default"></span><dl> <dt>**RPC\_C\_AUTHN\_LEVEL\_DEFAULT**</dt> <dt>0</dt> </dl>                    | Tells DCOM to choose the authentication level using its normal security blanket negotiation algorithm. For more information, see [Security Blanket Negotiation](security-blanket-negotiation.md). <br/> |
| <span id="RPC_C_AUTHN_LEVEL_NONE"></span><span id="rpc_c_authn_level_none"></span><dl> <dt>**RPC\_C\_AUTHN\_LEVEL\_NONE**</dt> <dt>1</dt> </dl>                             | Performs no authentication.<br/>                                                                                                                                                                         |
| <span id="RPC_C_AUTHN_LEVEL_CONNECT"></span><span id="rpc_c_authn_level_connect"></span><dl> <dt>**RPC\_C\_AUTHN\_LEVEL\_CONNECT**</dt> <dt>2</dt> </dl>                    | Authenticates the credentials of the client only when the client establishes a relationship with the server. Datagram transports always use RPC\_AUTHN\_LEVEL\_PKT instead. <br/>                        |
| <span id="RPC_C_AUTHN_LEVEL_CALL"></span><span id="rpc_c_authn_level_call"></span><dl> <dt>**RPC\_C\_AUTHN\_LEVEL\_CALL**</dt> <dt>3</dt> </dl>                             | Authenticates only at the beginning of each remote procedure call when the server receives the request. Datagram transports use RPC\_C\_AUTHN\_LEVEL\_PKT instead.<br/>                                  |
| <span id="RPC_C_AUTHN_LEVEL_PKT"></span><span id="rpc_c_authn_level_pkt"></span><dl> <dt>**RPC\_C\_AUTHN\_LEVEL\_PKT**</dt> <dt>4</dt> </dl>                                | Authenticates that all data received is from the expected client.<br/>                                                                                                                                   |
| <span id="RPC_C_AUTHN_LEVEL_PKT_INTEGRITY"></span><span id="rpc_c_authn_level_pkt_integrity"></span><dl> <dt>**RPC\_C\_AUTHN\_LEVEL\_PKT\_INTEGRITY**</dt> <dt>5</dt> </dl> | Authenticates and verifies that none of the data transferred between client and server has been modified.<br/>                                                                                           |
| <span id="RPC_C_AUTHN_LEVEL_PKT_PRIVACY"></span><span id="rpc_c_authn_level_pkt_privacy"></span><dl> <dt>**RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY**</dt> <dt>6</dt> </dl>       | Authenticates all previous levels and encrypts the argument value of each remote procedure call.<br/>                                                                                                    |



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Rpcdce.h</dt> </dl> |



 

 





