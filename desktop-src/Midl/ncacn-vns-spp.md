---
title: ncacn_vns_spp attribute
description: The ncacn\_vns\_spp keyword identifies Banyan Vines SPP as the protocol family for the endpoint. This protocol family is obsolete and should not be used in new applications.
ms.assetid: a2aff0a6-2e7e-43e4-a180-f1ddd0456843
keywords:
- ncacn_vns_spp attribute MIDL
topic_type:
- apiref
api_name:
- ncacn_vns_spp
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ncacn\_vns\_spp attribute

The **ncacn\_vns\_spp** keyword identifies Banyan Vines SPP as the protocol family for the endpoint. This protocol family is obsolete and should not be used in new applications.

``` syntax
endpoint("ncacn_vns_spp:server-name[port-address]")
```

## Parameters

<dl> <dt>

*server-name* 
</dt> <dd>

Specifies the StreetTalk name of the server. The name is of the form item@group@organization. The item can be up to 31 characters long and the group and organization can be up to 15 characters.

</dd> <dt>

*port-name* 
</dt> <dd>

Specifies a Banyan Vines SPP port. The valid range for static endpoints is 250– 511.

</dd> </dl>

## Remarks

In order to use the **ncacn\_vns\_spp** transport protocol in distributed applications running on Windows 2000, the appropriate Banyan Enterprise Client software must be installed. After installation, open **Control Panel**, choose **Configuration and Add**, then select **Service \| Banyan \| RPC services for Banyan**. Support for 16-bit clients requires appropriate Vines software. For more information about Banyan's Enterprise Client product and 16-bit Vines software, contact Banyan.

The syntax of the Banyan Vines SPP transport port string, like all port strings, is defined independently of the IDL specification. The compiler performs some syntax checking but does not guarantee that the endpoint specification is correct. Some errors may be reported at run time rather than at compile time.

> [!Note]  
> This protocol family is not supported in Windows XP.

 

## Examples

``` syntax
[
    uuid(12345678-1234-1234-1234-123456789ABC), 
    version(1.1), 
    endpoint("ncacn_vns_spp:printer@sdkgrp@company[260]")
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

[**ncalrpc**](ncalrpc.md)
</dt> <dt>

[**ncadg\_ipx**](ncadg-ipx.md)
</dt> <dt>

[**ncadg\_ip\_udp**](ncadg-ip-udp.md)
</dt> <dt>

[string binding](/windows/desktop/Rpc/string-binding)
</dt> </dl>

 

 