---
Description: Checks whether a pointer is NULL. If the pointer is NULL, the function or method in which the macro appears returns the specified value.
ms.assetid: eca73fbf-5fd8-4b76-af06-ca0c22510b55
title: CheckPointer macro
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CheckPointer macro

Checks whether a pointer is **NULL**. If the pointer is **NULL**, the function or method in which the macro appears returns the specified value.

## Syntax


```C++
HRESULT CheckPointer(
    p,
    ret
);
```



## Parameters

<dl> <dt>

*p* 
</dt> <dd>

Pointer to check.

</dd> <dt>

*ret* 
</dt> <dd>

Value that the function or method returns if *p* is **NULL**.

</dd> </dl>

## Return value

The surrounding function returns *ret* if *p* is **NULL**. Otherwise, the macro does not cause the surrounding function to return.

## Examples


```
HRESULT MyFunction(VOID *pSomeParameter)
{
    // Return E_INVALIDARG if pSomeParameter is NULL.
    CheckPointer(pSomeParameter, E_INVALIDARG)

    // Rest of the function (not shown).
}
```



## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl> |



## See also

<dl> <dt>

[Pointer Validation Macros](pointer-validation-macros.md)
</dt> </dl>

 

 




