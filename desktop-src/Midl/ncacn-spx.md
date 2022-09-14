---
title: ncacn_spx attribute
description: The ncacn\_spx keyword identifies SPX as the protocol family for the endpoint. This protocol family is obsolete and should not be used in new applications.
ms.assetid: 45e93e25-e84d-4242-80b0-c4b61e80f716
keywords:
- ncacn_spx attribute MIDL
topic_type:
- apiref
api_name:
- ncacn_spx
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ncacn\_spx attribute

The **ncacn\_spx** keyword identifies SPX as the protocol family for the endpoint. This protocol family is obsolete and should not be used in new applications.

``` syntax
endpoint("ncacn_spx:link-address[port-name]")
```

## Parameters

<dl> <dt>

*link-address* 
</dt> <dd>

Specifies the host server. This may be either a character string (the server name), or a 20-digit hexadecimal number that consists of the host server's network address (8 digits) concatenated with the node address (12 digits). See Remarks for instructions on how to obtain the network address and node address. A **NULL** string specifies the local computer.

</dd> <dt>

*port-name* 
</dt> <dd>

Specifies an optional 16-bit number that represents the socket address. Values can range from 1 to 65,535. When no value is specified, the endpoint-mapping service selects a valid *port-name* value.

</dd> </dl>

## Remarks

When you use the **ncacn\_spx** transport, the server name is exactly the same as the 32-bit Windows name. However, since the names are distributed using Novell protocols, they must conform to the Novell naming conventions. If a server name is not a valid Novell name, servers will not be able to create endpoints with the **ncacn\_spx** transport. The following is a partial list of characters prohibited in Novell server names:

" \* + . / : ; < = > ? \[ \] \\ \|

The **ncacn\_spx** transport is not supported by the version of NWLink supplied with MS Client 3.0.

16-bit Windows client applications that use the **ncacn\_spx** transport require that the file Nwipxspx.dll be installed in order to run under the WOW subsystem. Contact Novell to obtain this file.

> [!Note]  
> To obtain the network and node addresses, use Novell's **comcheck** utility, or the Novell-defined API **IPXGetInternetAddress**. On Windows, you can also obtain these addresses with the **ipxroute config** command.

 

The syntax of the SPX transport port string, like all port strings, is defined independently of the IDL specification. The compiler performs some syntax checking but does not guarantee that the endpoint specification is correct. Some errors may be reported at run time rather than at compile time.

## Examples

``` syntax
[
    uuid(12345678-4000-2006-0000-20000000001a), 
    version(1.1), 
    endpoint("ncacn_spx:[1000]") 
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

[**ncacn\_nb\_nb**](ncacn-nb-nb.md)
</dt> <dt>

[**ncacn\_nb\_tcp**](ncacn-nb-tcp.md)
</dt> <dt>

[**ncacn\_np**](ncacn-np.md)
</dt> <dt>

[**ncacn\_vns\_spp**](ncacn-vns-spp.md)
</dt> <dt>

[**ncalrpc**](ncalrpc.md)
</dt> <dt>

[**ncadg\_ipx**](ncadg-ipx.md)
</dt> <dt>

[**ncadg\_ip\_udp**](ncadg-ip-udp.md)
</dt> <dt>

[string binding](/windows/desktop/Rpc/string-binding)
</dt> </dl>

 

 