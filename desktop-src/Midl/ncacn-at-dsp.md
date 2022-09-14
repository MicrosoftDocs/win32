---
title: ncacn_at_dsp attribute
description: The ncacn\_at\_dsp keyword identifies AppleTalk DSP as the protocol family for the endpoint. This protocol family is obsolete and should not be used in new applications.
ms.assetid: 3165e4f6-8869-4eff-af65-53e85f78a949
keywords:
- ncacn_at_dsp attribute MIDL
topic_type:
- apiref
api_name:
- ncacn_at_dsp
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ncacn\_at\_dsp attribute

The **ncacn\_at\_dsp** keyword identifies AppleTalk DSP as the protocol family for the endpoint. This protocol family is obsolete and should not be used in new applications.

``` syntax
endpoint("ncacn_at_dsp:[port-name]")
```

## Parameters

<dl> <dt>

*port-name* 
</dt> <dd>

Specifies a character string up to 22 bytes long.

</dd> </dl>

## Remarks

The syntax of the AppleTalk DSP port string, like all port strings, is defined by the transport implementation and is independent of the IDL specification. The MIDL compiler performs limited syntax checking but does not guarantee that the endpoint specification is correct. Some classes of errors may be reported at run time rather than at compile time.

## Examples

``` syntax
[
    uuid(12345678-4000-2006-0000-20000000001a), 
    version(1.1), 
    endpoint("ncacn_at_dsp:[my_services_endpoint]") 
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

[**string binding**](/windows/desktop/Rpc/string-binding)
</dt> </dl>

 

 