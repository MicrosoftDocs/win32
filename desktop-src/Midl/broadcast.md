---
title: broadcast attribute
description: The keyword \ broadcast\ specifies that remote procedure calls be sent to all servers on a local network.
ms.assetid: 3951c80f-b7f1-457b-9eee-6e075291b27e
keywords:
- broadcast attribute MIDL
topic_type:
- apiref
api_name:
- broadcast
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# broadcast attribute

The keyword **\[broadcast\]** specifies that remote procedure calls be sent to all servers on a local network.

``` syntax
[
    interface-attribute-list
] 
interface interface-name 
{
    [broadcast [, attribute-list]] returntype function-name(params)
}
```

## Parameters

<dl> <dt>

*interface-attribute-list* 
</dt> <dd>

Specifies a list of zero or more IDL attributes that apply to the interface as a whole. When two or more interface attributes are present, they must be separated by commas.

</dd> <dt>

*interface-name* 
</dt> <dd>

Specifies the name of the interface.

</dd> <dt>

*attribute-list* 
</dt> <dd>

Specifies additional attributes to be applied to the function. Separate multiple attributes with commas.

</dd> <dt>

*returntype* 
</dt> <dd>

Specifies the return type of the function.

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the function to which the **\[broadcast\]** attribute will be applied.

</dd> <dt>

*params* 
</dt> <dd>

Function parameter list.

</dd> </dl>

## Remarks

The **\[broadcast\]** keyword specifies that the routine is always broadcasted to all the servers on the network, rather than being delivered to one particular server.The client receives output from the first reply to return successfully, while subsequent replies are discarded.

An operation with the **\[broadcast\]** attribute is implicitly an [**\[idempotent\]**](idempotent.md) operation. However, the **\[broadcast\]** attribute specifies additional properties that functions with the **\[idempotent\]** attribute don't have. Specifically, functions using the **\[broadcast\]** attribute specify that the routine can be called multiple times as the result of one remote procedure call. At the same time, they can be sent to multiple servers. This is different from the **\[idempotent\]** attribute, which specifies only that a call can be retried if it is not completed.

If a remote procedure broadcasts its call to all hosts on a local network, it must use either the [**ncadg\_ip\_udp**](ncadg-ip-udp.md) or the [**ncadg\_ipx**](ncadg-ipx.md) protocol sequence. Note that the size of a **\[broadcast\]** packet is determined by the datagram service in use.

## See also

<dl> <dt>

[**idempotent**](idempotent.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**maybe**](maybe.md)
</dt> <dt>

[**ncadg\_ip\_udp**](ncadg-ip-udp.md)
</dt> <dt>

[**ncadg\_ipx**](ncadg-ipx.md)
</dt> </dl>

 

 




