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
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
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

[TYPEFLAGS](https://msdn.microsoft.com/windows/desktop/bf34cc90-f772-4562-9d18-7cf35aeed41e)
</dt> <dt>

[ODL File Syntax](https://msdn.microsoft.com/windows/desktop/df7aa86f-1453-4409-939e-788d469d611e)
</dt> <dt>

[ODL File Example](https://msdn.microsoft.com/windows/desktop/86d64a4f-08eb-422a-bb1d-dfa868094645)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> </dl>

 

 




