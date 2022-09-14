---
title: strict_context_handle attribute
description: The \ strict\_context\_handle\ ACF attribute sets restrictions on context handles.
ms.assetid: c34f9018-d519-4a75-ad6f-70d386a20817
keywords:
- strict_context_handle attribute MIDL
topic_type:
- apiref
api_name:
- strict_context_handle
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# strict\_context\_handle attribute

The **\[strict\_context\_handle\]** ACF attribute sets restrictions on context handles.

``` syntax
[ 
    strict_context_handle 
    [, interface-attribute-list] 
] 
interface interface-name
{
    interface-definition-statements
}
```

## Parameters

<dl> <dt>

*interface-attribute-list* 
</dt> <dd>

Other ACF attributes that apply to the interface as a whole. Valid attributes include [**auto\_handle**](auto-handle.md), [**implicit\_handle**](implicit-handle.md), [**explicit\_handle**](explicit-handle.md), and [**optimize**](optimize.md), [**code**](code.md), or [**nocode**](nocode.md). Separate multiple attributes with commas.

</dd> <dt>

*interface-name* 
</dt> <dd>

The name of the interface.

</dd> <dt>

*interface-definition-statements* 
</dt> <dd>

One or more MIDL statements that define the elements of the [**interface**](interface.md).

</dd> </dl>

## Remarks

Normally, when a call to an interface method generates a context handle, that handle becomes freely available to any other interface. When you use the **\[strict\_context\_handle\]** attribute you guarantee that the methods in that interface will only accept context handles that were created by a method from the same interface. Interfaces compiled without **\[strict\_context\_handle\]** cannot accept context handles created on interfaces compiled with **\[strict\_context\_handle\]**.

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> <dt>

[**code**](code.md)
</dt> <dt>

[Context Handles](/windows/desktop/Rpc/context-handles)
</dt> <dt>

[**context\_handle\_serialize**](context-handle-serialize.md)
</dt> <dt>

[**context\_handle\_noserialize**](context-handle-noserialize.md)
</dt> <dt>

[**explicit\_handle**](explicit-handle.md)
</dt> <dt>

[**implicit\_handle**](implicit-handle.md)
</dt> <dt>

[**nocode**](nocode.md)
</dt> <dt>

[**optimize**](optimize.md)
</dt> <dt>

[type\_strict\_context\_handle](type-strict-context-handle.md)
</dt> </dl>

 

 