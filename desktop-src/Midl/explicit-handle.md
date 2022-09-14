---
title: explicit_handle attribute
description: The \ explicit\_handle\ ACF attribute specifies that each procedure has, as its first parameter, a primitive handle, such as a handle\_t type.
ms.assetid: c95d005e-dcc7-4d83-885d-91c0773c0ed8
keywords:
- explicit_handle attribute MIDL
topic_type:
- apiref
api_name:
- explicit_handle
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# explicit\_handle attribute

The \[**explicit\_handle**\] ACF attribute specifies that each procedure has, as its first parameter, a primitive handle, such as a [**handle\_t**](handle-t.md) type.

``` syntax
[
    explicit_handle
] 
interface interface-name
{
    ...
}
```

## Parameters

<dl> <dt>

*interface-name* 
</dt> <dd>

Specifies the name of the interface.

</dd> </dl>

## Remarks

When you use the **\[explicit\_handle\]** attribute, each procedure has a primitive handle as its first parameter even if the IDL file does not contain this handle in its parameter list. The prototypes emitted to the header file and stub routines contain the additional parameter, and that parameter is used as the handle for directing the remote call.

The **\[explicit\_handle\]** attribute affects both remote procedures and serialization procedures. For type serialization, the support routines are generated with the initial parameter as an explicit (serialization) handle. If the **\[explicit\_handle\]** attribute is not used, the application can still specify that an operation have an explicit handle (binding or serialization) directing the call. To do this, a prototype with an argument containing a handle type is supplied to the IDL file. Note that in default mode, an argument that does not appear first can also be used as a handle directing the call.

Therefore, while the **\[explicit\_handle\]** attribute is a way of giving the IDL prototype a primitive **\[explicit\_handle\]** attribute, it does not necessarily require a change to the IDL file. In [**/osf**](-osf.md) mode only the first argument can be used as an explicit handle type.

The **\[explicit\_handle\]** attribute can be used as either an interface attribute or an operation attribute. As an interface attribute, it affects all the operations in the interface and all the types that require serialization support. If, however, it is used as an operation attribute, it affects only that particular operation. If a method contains one or more \[in\] context handles, the left most \[in\] context handle is used as the binding handle, and no additional explicit handle is created.

## Examples

``` syntax
/* ACF File */ 
[
    explicit_handle
] 
interface iface
{ 
    // Interface definition statements.
};
```

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> <dt>

[**auto\_handle**](auto-handle.md)
</dt> <dt>

[**implicit\_handle**](implicit-handle.md)
</dt> <dt>

[**/osf**](-osf.md)
</dt> </dl>

 

 




