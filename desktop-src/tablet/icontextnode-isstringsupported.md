---
description: Indicates whether recognized string of this IContextNode came from the system dictionary, user dictionary, or word list.
ms.assetid: 9eaee549-ae78-4a67-a39e-2096c7d5d9cd
title: IContextNode::IsStringSupported method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.IsStringSupported
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::IsStringSupported method

Indicates whether recognized string of this [**IContextNode**](icontextnode.md) came from the system dictionary, user dictionary, or word list.

## Syntax


```C++
HRESULT IsStringSupported(
  [out, retval] VARIANT_BOOL *pfIsSupported
);
```



## Parameters

<dl> <dt>

*pfIsSupported* \[out, retval\]
</dt> <dd>

**VARIANT\_TRUE** if the recognized string value of this [**IContextNode**](icontextnode.md) is supported by the [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) with any corresponding hint nodes applied; otherwise, **VARIANT\_FALSE**.

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

[**IContextNode**](icontextnode.md)
</dt> </dl>

 

 




