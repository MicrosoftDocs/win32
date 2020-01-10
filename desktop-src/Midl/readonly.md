---
title: readonly attribute
description: The \ readonly\ attribute prohibits assignment to a variable.
ms.assetid: b81064e6-e788-48d1-9958-203f1e3c7e4d
keywords:
- readonly attribute MIDL
topic_type:
- apiref
api_name:
- readonly
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# readonly attribute

The **\[readonly\]** attribute prohibits assignment to a variable.

``` syntax
[readonly [, optional-attributes]] data-type identifier
```

## Parameters

<dl> <dt>

*optional-attributes* 
</dt> <dd>

Zero or more MIDL attributes.

</dd> <dt>

*data-type* 
</dt> <dd>

The type of the data contained by *identifier*.

</dd> <dt>

*identifier* 
</dt> <dd>

A name by which the software can refer to the data storage location.

</dd> </dl>

## Remarks

The **\[readonly\]** attribute prohibits assignment to a variable. **\[readonly\]** is only supported at the parameter level, not at the method level.

### Flags

VARFLAG\_FREADONLY

## Examples

``` syntax
HRESULT Method3([in, readonly] int iMmutable);
```

## See also

<dl> <dt>

[TYPEFLAGS](https://msdn.microsoft.com/library/ms221509(v=VS.71).aspx)
</dt> <dt>

[ODL File Syntax](https://msdn.microsoft.com/library/ms221683(v=VS.71).aspx)
</dt> <dt>

[ODL File Example](https://msdn.microsoft.com/library/ms221308(v=VS.71).aspx)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> </dl>

 

 




