---
title: Binding Time-out Constants (Rpcdce.h)
description: The RPC library uses the binding time-out constants to specify the relative amount of time that should be spent to establish a binding to the server before giving up.
ms.assetid: bf5f3f08-ab29-4732-9ce3-d6d7ad699369
topic_type:
- apiref
api_name:
- RPC_C_BINDING_INFINITE_TIMEOUT
- RPC_C_BINDING_MIN_TIMEOUT
- RPC_C_BINDING_DEFAULT_TIMEOUT
- RPC_C_BINDING_MAX_TIMEOUT
api_location:
- Rpcdce.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Binding Time-out Constants

The RPC library uses the binding time-out constants to specify the relative amount of time that should be spent to establish a binding to the server before giving up. The timeout can be enabled with a call to the [**RpcMgmtSetComTimeout**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtsetcomtimeout) function. The following list contains the valid time-out values.



| Constant/value                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                              |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RPC_C_BINDING_INFINITE_TIMEOUT"></span><span id="rpc_c_binding_infinite_timeout"></span><dl> <dt>**RPC\_C\_BINDING\_INFINITE\_TIMEOUT**</dt> <dt> 10 </dt> </dl> | Keeps trying to establish communications forever.<br/>                                                                                                                                                             |
| <span id="RPC_C_BINDING_MIN_TIMEOUT"></span><span id="rpc_c_binding_min_timeout"></span><dl> <dt>**RPC\_C\_BINDING\_MIN\_TIMEOUT**</dt> <dt>0</dt> </dl>                   | Tries the minimum amount of time for the network protocol being used. This value favors response time over correctness in determining whether the server is running.<br/>                                          |
| <span id="RPC_C_BINDING_DEFAULT_TIMEOUT"></span><span id="rpc_c_binding_default_timeout"></span><dl> <dt>**RPC\_C\_BINDING\_DEFAULT\_TIMEOUT**</dt> <dt>5</dt> </dl>       | Tries an average amount of time for the network protocol being used. This value gives correctness in determining whether a server is running and gives response time equal weight. This is the default value.<br/> |
| <span id="RPC_C_BINDING_MAX_TIMEOUT"></span><span id="rpc_c_binding_max_timeout"></span><dl> <dt>**RPC\_C\_BINDING\_MAX\_TIMEOUT**</dt> <dt>9</dt> </dl>                   | Tries the longest amount of time for the network protocol being used. This value favors correctness in determining whether a server is running over response time.<br/>                                            |



## Remarks

The values in the preceding table are not in seconds. These values represent a relative amount of time on a scale of zero to 10. For more information on avoiding communication delays, refer to Preventing Client-side Hangs.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Rpcdce.h</dt> </dl> |



 

 





