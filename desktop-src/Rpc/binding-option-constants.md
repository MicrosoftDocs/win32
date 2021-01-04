---
title: Binding Option Constants (Rpcdce.h)
description: Applications set the binding option constants to control how the RPC run-time library processes remote procedure calls. The following table lists each binding property, and the relevant constant values for the binding properties.
ms.assetid: ff88e05d-b9f3-42ef-a44f-fee9261832c8
topic_type:
- apiref
api_name:
- RPC_C_OPT_BINDING_NONCAUSAL
- RPC_C_OPT_MAX_OPTIONS
- RPC_C_DONT_FAIL
- RPC_C_OPT_SESSION_ID
- RPC_C_OPT_COOKIE_AUTH
- RPC_C_OPT_RESOURCE_TYPE_UUID
- RPC_C_OPT_DONT_LINGER
- RPC_C_OPT_UNIQUE_BINDING
api_location:
- Rpcdce.h
- Rpcdcep.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Binding Option Constants

Applications set the binding option constants to control how the RPC run-time library processes remote procedure calls. The following table lists each binding property, and the relevant constant values for the binding properties.

> [!Note]  
> All message queue options (MQ) in the following table are valid for Windows 2000 only. Windows XP and later versions do not support message queuing. Developers are discouraged from using message queuing.

 



| Constant/value                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                           |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RPC_C_OPT_BINDING_NONCAUSAL"></span><span id="rpc_c_opt_binding_noncausal"></span><dl> <dt>**RPC\_C\_OPT\_BINDING\_NONCAUSAL**</dt> <dt>9</dt> </dl>     | Default. If **FALSE**, causal call ordering. RPC calls are executed in strict order of submission. See Remarks.<br/> If **TRUE**, noncausal call ordering. RPC calls are executed independently. See Remarks.<br/>                                                                        |
| <span id="RPC_C_OPT_MAX_OPTIONS"></span><span id="rpc_c_opt_max_options"></span><dl> <dt>**RPC\_C\_OPT\_MAX\_OPTIONS**</dt> <dt>17</dt> </dl>                      | Not needed for application programs. Used internally by Microsoft.<br/>                                                                                                                                                                                                                         |
| <span id="RPC_C_DONT_FAIL"></span><span id="rpc_c_dont_fail"></span><dl> <dt>**RPC\_C\_DONT\_FAIL**</dt> <dt>4</dt> </dl>                                          | Not needed for application programs. Used internally by Microsoft.<br/>                                                                                                                                                                                                                         |
| <span id="RPC_C_OPT_SESSION_ID"></span><span id="rpc_c_opt_session_id"></span><dl> <dt>**RPC\_C\_OPT\_SESSION\_ID**</dt> <dt>6</dt> </dl>                          | If **TRUE**, a session ID is generated for each connection.<br/>                                                                                                                                                                                                                                |
| <span id="RPC_C_OPT_COOKIE_AUTH"></span><span id="rpc_c_opt_cookie_auth"></span><dl> <dt>**RPC\_C\_OPT\_COOKIE\_AUTH**</dt> <dt>7</dt> </dl>                       | If **TRUE**, client-side cookie-based authentication is used for connections. A pointer to the [**RPC\_C\_OPT\_COOKIE\_AUTH\_DESCRIPTOR**](/windows/desktop/api/Rpcdcep/ns-rpcdcep-rpc_c_opt_cookie_auth_descriptor) structure is passed as the *OptionValue* parameter in [**RpcBindingSetOption**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetoption).<br/> |
| <span id="RPC_C_OPT_RESOURCE_TYPE_UUID"></span><span id="rpc_c_opt_resource_type_uuid"></span><dl> <dt>**RPC\_C\_OPT\_RESOURCE\_TYPE\_UUID**</dt> <dt>8</dt> </dl> | Not needed for application programs. Used internally by Microsoft.<br/>                                                                                                                                                                                                                         |
| <span id="RPC_C_OPT_DONT_LINGER"></span><span id="rpc_c_opt_dont_linger"></span><dl> <dt>**RPC\_C\_OPT\_DONT\_LINGER**</dt> <dt>13</dt> </dl>                      | If **TRUE**, force shutdown of the association after the last binding handle/context handle on it is freed.<br/>                                                                                                                                                                                |
| <span id="RPC_C_OPT_UNIQUE_BINDING"></span><span id="rpc_c_opt_unique_binding"></span><dl> <dt>**RPC\_C\_OPT\_UNIQUE\_BINDING**</dt> <dt>11</dt> </dl>             | When set to **true**, RPC does not reuse existing connections. A unique binding handle is opened for each connection and state is maintained for each unique binding handle.<br/>                                                                                                               |



## Remarks

By default, the RPC run-time library executes the calls on a given binding handle from each thread of an application in strict order of submission. This does not guarantee that calls from different threads on the same binding handle are serialized. Multithreaded applications must serialize their RPC calls. If this behavior is too restrictive, you can enable noncausal ordering. When you do, the RPC run-time library executes calls independently. It imposes no ordering on their submission.

One example of an application that might find noncausal ordering useful is a multithreaded program whose threads make calls on the same binding handle. Similarly, a program that uses multiple asynchronous calls on a binding handle will find noncausal ordering a convenient option. Another example might be an Internet proxy program that uses a single thread to handle requests for several clients. In each of these cases, it would be extremely restrictive to try to serialize the remote procedure calls.

The **RPC\_C\_OPT\_DONT\_LINGER** option can be set only on binding handles that use the **ncalrpc** or **ncacn\_\*** protocol sequences. It cannot be used on **ncadg\_\*** protocol sequences. The [**RpcBindingSetOption**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetoption) function with this option must be called on a binding handle on which at least one RPC call has been made. If no RPC call have been made on the binding handle, **RPC\_S\_WRONG\_KIND\_OF\_BINDING** is returned from the **RpcBindingSetOption** function call. The option takes effect for the entire association, regardless of how many binding handles are attached to the association. Since it is checked before the association is destroyed, it can be set at any time before the binding handle is closed.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                 |
| Header<br/>                   | <dl> <dt>Rpcdce.h; </dt> <dt>Rpcdcep.h</dt> </dl> |



## See also

<dl> <dt>

[**RpcBindingSetOption**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetoption)
</dt> <dt>

[**RpcBindingInqOption**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindinginqoption)
</dt> <dt>

[Managing Network Connection Sets (Associations)](managing-network-connection-sets-associations-.md)
</dt> </dl>

 

 





