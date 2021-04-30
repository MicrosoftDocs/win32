---
description: Indicates whether the specified recognized string came from the system dictionary, user dictionary, or word list.
ms.assetid: 1504e633-5917-4ac6-b043-95d4bc75b020
title: IContextNode::IsAlternateStringSupported method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.IsAlternateStringSupported
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::IsAlternateStringSupported method

Indicates whether the specified recognized string came from the system dictionary, user dictionary, or word list. Any restricting data, like wordlists, guides or factoids, in any corresponding hint node will be used to determine if the string is supported.

## Syntax


```C++
HRESULT IsAlternateStringSupported(
  [in]  BSTR         bstrAlternateString,
  [out] VARIANT_BOOL *pfIsSupported
);
```



## Parameters

<dl> <dt>

*bstrAlternateString* \[in\]
</dt> <dd>

Recognized string to verify.

</dd> <dt>

*pfIsSupported* \[out\]
</dt> <dd>

**VARIANT\_TRUE** if the specified string is supported by the [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) with any corresponding hint nodes applied; **VARIANT\_FALSE** if not supported.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

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

 

 




