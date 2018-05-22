---
Description: 'Retrieves the IContextLink at the specified index.'
ms.assetid: '46bb71b9-5ef3-4756-97f6-40e0aaa82826'
title: 'IContextLinks::GetContextLink method'
---

# IContextLinks::GetContextLink method

Retrieves the [**IContextLink**](icontextlink.md) at the specified index.

## Syntax


```C++
HRESULT GetContextLink(
  [in]  ULONG        ulIndex,
  [out] IContextLink **ppContextLink
);
```



## Parameters

<dl> <dt>

*ulIndex* \[in\]
</dt> <dd>

The zero-based index of the [**IContextLink**](icontextlink.md) object to get.

</dd> <dt>

*ppContextLink* \[out\]
</dt> <dd>

A pointer to the [**IContextLink**](icontextlink.md) object at the specified index.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> \[!Caution\]  
> To avoid a memory leak, call [**IUnknown::Release**](https://msdn.microsoft.com/library/windows/desktop/ms682317) on \**ppContextLink* when you no longer need to use the context link.

 

## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IContextLinks**](icontextlinks.md)
</dt> <dt>

[**IContextNode**](icontextnode.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




