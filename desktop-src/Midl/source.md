---
title: source attribute
description: The \ source\ attribute indicates that a member of a coclass, property, or method is a source of events. For a member of a coclass, this attribute means that the member is called rather than implemented.
ms.assetid: fbd5411a-e614-4643-810a-f3765e7ec16d
keywords:
- source attribute MIDL
topic_type:
- apiref
api_name:
- source
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# source attribute

The **\[source\]** attribute indicates that a member of a [**coclass**](coclass.md), property, or method is a source of events. For a member of a **coclass**, this attribute means that the member is called rather than implemented.

``` syntax
[
    coclass-attributes
]
coclass coclass-name
{
    [source [, optional-attributes] ] statement-type statement-name; 
  [, ...]
}

[source] object-type function-name(optional-parameter-list);
```

## Parameters

<dl> <dt>

*coclass-attributes* 
</dt> <dd>

Zero or more attributes that will be applied to the [**coclass**](coclass.md).

</dd> <dt>

*coclass-name* 
</dt> <dd>

The name identifier of the [**coclass**](coclass.md).

</dd> <dt>

*optional-attributes* 
</dt> <dd>

Zero or more MIDL attributes.

</dd> <dt>

*statement-type* 
</dt> <dd>

Can be [**interface**](interface.md) or [**dispinterface**](dispinterface.md).

</dd> <dt>

*statement-name* 
</dt> <dd>

The name of the [**interface**](interface.md) or [**dispinterface**](dispinterface.md).

</dd> <dt>

*object-type* 
</dt> <dd>

The type of the object that the method returns. This object is a source of events.

</dd> <dt>

*function-name* 
</dt> <dd>

The name of a method in an [**interface**](interface.md) or [**dispinterface**](dispinterface.md).

</dd> <dt>

*optional-parameter-list* 
</dt> <dd>

Zero or more method parameters.

</dd> </dl>

## Remarks

On a property or method, the **\[source\]** attribute indicates that the member returns an object or VARIANT that is a source of events. The object implements **IConnectionPointContainer**.

### Flags

IMPLTYPEFLAG\_FSOURCE, VARFLAG\_SOURCE, FUNCFLAG\_SOURCE

## Examples

``` syntax
[default, source] dispinterface DIMyFaceAdviseSink;
[source]interface IMyFaceAdviseSink;
```

## See also

<dl> <dt>

[**coclass**](coclass.md)
</dt> <dt>

[**dispinterface**](dispinterface.md)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[**interface**](interface.md)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[TYPEFLAGS](/windows/win32/api/oaidl/ne-oaidl-typeflags)
</dt> </dl>

 

 