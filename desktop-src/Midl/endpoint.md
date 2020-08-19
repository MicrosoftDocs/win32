---
title: endpoint attribute
description: The \ endpoint\ attribute specifies a well-known port or ports (communication endpoints) on which servers of the interface listen for calls.
ms.assetid: b88c5a97-b726-43de-b5b6-649cda60c320
keywords:
- endpoint attribute MIDL
topic_type:
- apiref
api_name:
- endpoint
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# endpoint attribute

The **\[endpoint\]** attribute specifies a well-known port or ports (communication endpoints) on which servers of the interface listen for calls.

``` syntax
endpoint("protocol-sequence:[endpoint-port]" [ , ...] )
```

## Parameters

<dl> <dt>

*protocol-sequence* 
</dt> <dd>

Specifies a character string that represents a valid combination of an RPC protocol (such as "ncacn"), a transport protocol (such as "tcp"), and a network protocol (such as "ip"). For a list of valid protocol sequences, see [Protocol Sequence Constants](/windows/desktop/Rpc/protocol-sequence-constants).

</dd> <dt>

*endpoint-port* 
</dt> <dd>

Specifies a string that represents the endpoint designation for the specified protocol family. The syntax of the port string is specific to each protocol sequence.

</dd> </dl>

## Remarks

The **\[endpoint\]** attribute specifies a transport family such as the TCP/IP connection-oriented protocol, a NetBIOS connection-oriented protocol, or the named-pipe connection-oriented protocol. Use of the **\[endpoint\]** attribute is consistent with other methods for adding an endpoint, and does not provide additional or special services for the endpoint; it simply provides a shortcut for calling the API.

> [!Note]  
> Specifying an endpoint in the .IDL interface definition does not restrict access to the interface to the specified endpoint. Adding an endpoint to the .IDL interface definition allows the interface to be called through any endpoint in that process, and allows the endpoint to be used to call other interfaces in that process.

 

The *protocol-sequence* value determines the valid values for the *endpoint-port*. The MIDL compiler checks only general syntax for the *endpoint-port* entry. Port specification errors are reported by the run-time libraries. For information about the allowed values for each protocol sequence, see the [Protocol Sequence Constants](/windows/desktop/Rpc/protocol-sequence-constants).

The following protocol sequences specified by DCE are not supported by the MIDL compiler provided with Microsoft RPC: **ncacn\_osi\_dna** and **ncadg\_dds**.

Make sure that you correctly quote backslash characters in endpoints. This error commonly occurs when the endpoint is a named pipe.

Endpoint information specified in the IDL file is used by the RPC run-time functions [**RpcServerUseProtseqIf**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcserveruseprotseqif) and [**RpcServerUseAllProtseqsIf**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcserveruseallprotseqsif).

## Examples

``` syntax
endpoint("ncacn_np:[\\pipe\\rainier]") 

endpoint("ncacn_ip_tcp:[1044]", "ncacn_np:[\\pipe\\shasta]")
```

## See also

<dl> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**RpcServerUseAllProtseqsIf**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcserveruseallprotseqsif)
</dt> <dt>

[**RpcServerUseProtseqIf**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcserveruseprotseqif)
</dt> </dl>

 

 