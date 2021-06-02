---
description: Gets the number of IContextLink objects in this collection.
ms.assetid: c3becacd-2df0-401c-88c8-5fad3e9f8c02
title: IContextLinks::GetCount method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextLinks.GetCount
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextLinks::GetCount method

Gets the number of [**IContextLink**](icontextlink.md) objects in this collection.

## Syntax


```C++
HRESULT GetCount(
  [out, retval] ULONG *pulCount
);
```



## Parameters

<dl> <dt>

*pulCount* \[out, retval\]
</dt> <dd>

The number of [**IContextLink**](icontextlink.md) objects that are contained in this collection.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IContextLinks**](icontextlinks.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




