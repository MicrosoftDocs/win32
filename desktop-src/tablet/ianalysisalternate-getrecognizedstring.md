---
description: Gets the recognized string value of the IAnalysisAlternate object.
ms.assetid: cdf41824-77a4-4c71-8712-f380a6cbf4c5
title: IAnalysisAlternate::GetRecognizedString method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisAlternate.GetRecognizedString
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisAlternate::GetRecognizedString method

Gets the recognized string value of the [**IAnalysisAlternate**](ianalysisalternate.md) object.

## Syntax


```C++
HRESULT GetRecognizedString(
  [out] BSTR *pbstrRecognizedString
);
```



## Parameters

<dl> <dt>

*pbstrRecognizedString* \[out\]
</dt> <dd>

A pointer to the **BSTR** that is set to the recognized string value.

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

[**IAnalysisAlternate**](ianalysisalternate.md)
</dt> <dt>

[**IInkAnalyzer::GetRecognizedString Method**](iinkanalyzer-getrecognizedstring.md)
</dt> </dl>

 

 




