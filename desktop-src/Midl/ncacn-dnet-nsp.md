---
title: ncacn_dnet_nsp attribute
description: The ncacn\_dnet\_nsp keyword identifies DECnet as the protocol family for the endpoint. This protocol family is obsolete and should not be used in new applications.
ms.assetid: 797251c1-c5d3-416b-8bc7-5b83bb7027e6
keywords:
- ncacn_dnet_nsp attribute MIDL
topic_type:
- apiref
api_name:
- ncacn_dnet_nsp
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ncacn\_dnet\_nsp attribute

The **ncacn\_dnet\_nsp** keyword identifies DECnet as the protocol family for the endpoint. This protocol family is obsolete and should not be used in new applications.

``` syntax
endpoint("ncacn_dnet_nsp:server-name[port-name]")
```

## Parameters

<dl> <dt>

*server-name* 
</dt> <dd>

Specifies the name or internet address for the server, or host, computer. The name is a character string.

</dd> <dt>

*port-name* 
</dt> <dd>

Specifies a DECnet object name or object number. The object name can consist of up to 16 characters. Object numbers can be prefixed by the pound sign (\#).

</dd> </dl>

## Remarks

The syntax of the DECnet transport port string, like all port strings, is defined independently of the IDL specification. The compiler performs some syntax checking but does not guarantee that the endpoint specification is correct. Some errors may be reported at run time rather than at compile time.

> [!Note]  
> This protocol family is not supported in WindowsÂ XP.

 

## Examples

``` syntax
[   
    uuid(12345678-4000-2006-0000-20000000001a), 
    version(1.1), 
    endpoint("ncacn_dnet_nsp:node[RPC0034501]") 
interface iface
{
    // Interface definition statements.
}

[
    uuid(12345678-1234-1234-1234-123456789ABC), 
    version(1.1), 
    endpoint("ncacn_dnet_nsp:node[#41]") 
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

[**string binding**](/windows/desktop/Rpc/string-binding)
</dt> </dl>

 

 