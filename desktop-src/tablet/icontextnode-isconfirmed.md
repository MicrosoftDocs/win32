---
description: Retrieves a value that indicates whether the ConfirmationType passed in to this method has been set on this IContextNode.
ms.assetid: 4a96bc46-b627-4784-ad1d-1079f49592e5
title: IContextNode::IsConfirmed method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.IsConfirmed
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::IsConfirmed method

Retrieves a value that indicates whether the ConfirmationType passed in to this method has been set on this IContextNode.

## Syntax


```C++
HRESULT IsConfirmed(
  [in]  ConfirmationType confirmedType,
  [out] VARIANT_BOOL     *pfTypeConfirmed
);
```



## Parameters

<dl> <dt>

*confirmedType* \[in\]
</dt> <dd>

The confirmation type being tested for.

</dd> <dt>

*pfTypeConfirmed* \[out\]
</dt> <dd>

**VARIANT\_TRUE** if the type passed in confirmedType has been set on this [**IContextNode**](icontextnode.md) object; otherwise, **VARIANT\_FALSE**.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

This value is set by the [**IContextNode::Confirm**](icontextnode-confirm.md) method.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IContextNode**](icontextnode.md)
</dt> <dt>

[**IContextNode::Confirm**](icontextnode-confirm.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




