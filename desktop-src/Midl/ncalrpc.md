---
title: ncalrpc attribute
description: The ncalrpc keyword identifies local interprocess communication as the protocol family for the endpoint. This keyword is one of the valid protocol family names that must be used with the \ endpoint\ attribute.
ms.assetid: 0009f794-5c14-4484-9023-cb20c7030dc5
keywords:
- ncalrpc attribute MIDL
topic_type:
- apiref
api_name:
- ncalrpc
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ncalrpc attribute

The **ncalrpc** keyword identifies local interprocess communication as the protocol family for the endpoint. This keyword is one of the valid protocol family names that must be used with the **\[**[**endpoint**](endpoint.md)**\]** attribute.

``` syntax
endpoint("ncalrpc:[port-name]")
```

## Parameters

<dl> <dt>

*port-name* 
</dt> <dd>

A character string that specifies the communication port (an application, a service, or an instance of a service) that a client uses to make interprocess calls to a server. The string can contain up to 53 characters and should not contain any backslash (\\) characters. The computer name must not be used with the **ncalrpc** keyword.

</dd> </dl>

## Remarks

The syntax of the local interprocess-communication port string, like all port strings, is defined by the transport implementation and is independent of the IDL specification. The MIDL compiler performs limited syntax checking but does not guarantee that the endpoint specification is correct. Some classes of errors may be reported at run time rather than at compile time.

## Examples

``` syntax
[
    uuid(12345678-4000-2006-0000-20000000001a), 
    version(1.1), 
    endpoint("ncalrpc:[myapplicationname]") 
] 
interface iface
{
    // Interface definition statements.
}
```

## See also

<dl> <dt>

[**endpoint**](endpoint.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**ncacn\_at\_dsp**](ncacn-at-dsp.md)
</dt> <dt>

[**ncacn\_dnet\_nsp**](ncacn-dnet-nsp.md)
</dt> <dt>

[**ncacn\_ip\_tcp**](ncacn-ip-tcp.md)
</dt> <dt>

[**ncacn\_nb\_ipx**](ncacn-nb-ipx.md)
</dt> <dt>

[**ncacn\_spx**](ncacn-spx.md)
</dt> <dt>

[**ncacn\_nb\_nb**](ncacn-nb-nb.md)
</dt> <dt>

[**ncacn\_nb\_tcp**](ncacn-nb-tcp.md)
</dt> <dt>

[**ncacn\_np**](ncacn-np.md)
</dt> <dt>

[**ncacn\_vns\_spp**](ncacn-vns-spp.md)
</dt> <dt>

[**ncadg\_ip\_udp**](ncadg-ip-udp.md)
</dt> <dt>

[**ncadg\_ipx**](ncadg-ipx.md)
</dt> <dt>

[String Binding](/windows/desktop/Rpc/string-binding)
</dt> </dl>

 

 