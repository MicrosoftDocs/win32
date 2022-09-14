---
description: Retrieves the type of relationship this IContextLink represents.
ms.assetid: 03c13eba-1493-4fb7-b684-f15147e5a0eb
title: IContextLink::GetContextLinkDirection method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextLink.GetContextLinkDirection
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextLink::GetContextLinkDirection method

Retrieves the type of relationship this [**IContextLink**](icontextlink.md) represents.

## Syntax


```C++
HRESULT GetContextLinkDirection(
  [out] ContextLinkDirection *pContextLinkDirection
);
```



## Parameters

<dl> <dt>

*pContextLinkDirection* \[out\]
</dt> <dd>

The direction this [**IContextLink**](icontextlink.md) represents.

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

[**IContextLink**](icontextlink.md)
</dt> <dt>

[**ContextLinkDirection**](contextlinkdirection.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




