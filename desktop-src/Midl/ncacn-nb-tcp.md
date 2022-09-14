---
title: ncacn_nb_tcp attribute
description: The ncacn\_nb\_tcp keyword is used to identify TCP over NetBIOS as the protocol family for the endpoint. This protocol family is obsolete and should not be used in new applications.
ms.assetid: 3633842c-d1f5-46d9-866e-e54f31415ea5
keywords:
- ncacn_nb_tcp attribute MIDL
topic_type:
- apiref
api_name:
- ncacn_nb_tcp
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ncacn\_nb\_tcp attribute

The **ncacn\_nb\_tcp** keyword is used to identify TCP over NetBIOS as the protocol family for the endpoint. This protocol family is obsolete and should not be used in new applications.

``` syntax
endpoint("ncacn_nb_tcp:[port-name]")
```

## Parameters

<dl> <dt>

*port-name* 
</dt> <dd>

Specifies an optional 8-bit value ranging from 1 to 254. Values of less than 0x20 are reserved. If the *port-name* value is not specified, the endpoint-mapping service selects the port value.

</dd> </dl>

## Remarks

The syntax of the NetBIOS port string, like all port strings, is defined by the transport implementation and is independent of the IDL specification. The MIDL compiler performs limited syntax checking but does not guarantee that the endpoint specification is correct. Some classes of errors may be reported at run time rather than at compile time.

> [!Note]  
> This protocol family is not supported in WindowsÂ XP.

 

## Examples

``` syntax
[
    uuid(12345678-4000-2006-0000-20000000001a), 
    version(1.1), 
    endpoint("ncacn_nb_tcp:[100]") 
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

[**ncacn\_ip\_tcp**](ncacn-ip-tcp.md)
</dt> <dt>

[**ncacn\_nb\_nb**](ncacn-nb-nb.md)
</dt> <dt>

[**ncacn\_np**](ncacn-np.md)
</dt> <dt>

[**ncacn\_spx**](ncacn-spx.md)
</dt> <dt>

[**ncalrpc**](ncalrpc.md)
</dt> <dt>

[**string binding**](/windows/desktop/Rpc/string-binding)
</dt> </dl>

 

 