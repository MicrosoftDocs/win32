---
title: requestedit attribute
description: The \ requestedit\ attribute indicates that the property supports the OnRequestEdit notification.
ms.assetid: 63f38d83-596b-4031-bb6a-972374cd0c60
keywords: ["requestedit attribute MIDL"]
topic_type:
- apiref
api_name:
- requestedit
api_type:
- NA
---

# requestedit attribute

The **\[requestedit\]** attribute indicates that the property supports the **OnRequestEdit** notification.

``` syntax
[requestedit [,optional-attributes]] return-type function-name(params)
```

## Parameters

<dl> <dt>

*optional-attributes* 
</dt> <dd>

Zero or more MIDL attributes.

</dd> <dt>

*return-type* 
</dt> <dd>

Specifies the return type of the function.

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the function in the IDL file.

</dd> <dt>

*params* 
</dt> <dd>

Zero or more function parameters.

</dd> </dl>

## Remarks

Supporting **OnRequestEdit** notification means that, before a change is made, the object will send the client a request for permission to change a property. An object can support data binding but not have this attribute.

### Flags

FUNCFLAG\_FREQUESTEDIT, VARFLAG\_FREQUESTEDIT

## Examples

``` syntax
properties:
    [propget, helpstring("A useful comment"), bindable, defaultbind,
     displaybind, requestedit] long Func1(void);
```

## See also

<dl> <dt>

[TYPEFLAGS](bf34cc90-f772-4562-9d18-7cf35aeed41e)
</dt> <dt>

[ODL File Syntax](df7aa86f-1453-4409-939e-788d469d611e)
</dt> <dt>

[ODL File Example](86d64a4f-08eb-422a-bb1d-dfa868094645)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> </dl>

 

 




