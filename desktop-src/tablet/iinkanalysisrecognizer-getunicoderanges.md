---
description: Retrieves an array of character ranges representing the supported Unicode character ranges.
ms.assetid: 334cf545-832a-4e8a-8fe6-76a173676be7
title: IInkAnalysisRecognizer::GetUnicodeRanges method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalysisRecognizer.GetUnicodeRanges
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalysisRecognizer::GetUnicodeRanges method

Retrieves an array of character ranges representing the supported Unicode character ranges.

## Syntax


```C++
HRESULT GetUnicodeRanges(
  [in, out] ULONG  *pulNumberOfRanges,
  [out]     WCHAR  **ppulLowUnicode,
  [out]     USHORT **ppusUnicodeRangeLength
);
```



## Parameters

<dl> <dt>

*pulNumberOfRanges* \[in, out\]
</dt> <dd>

The number of character ranges pointed to by *ppulLowUnicode*.

</dd> <dt>

*ppulLowUnicode* \[out\]
</dt> <dd>

Pointer to an array of character ranges representing the supported Unicode character ranges.

</dd> <dt>

*ppusUnicodeRangeLength* \[out\]
</dt> <dd>

Pointer to an array of values indicating the length of each array point to by *ppulLowUnicode*.

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

[**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md)
</dt> </dl>

 

 




