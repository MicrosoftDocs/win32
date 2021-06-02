---
description: Retrieves the capabilities of the recognizer.
ms.assetid: 9014bd9b-54fb-4735-9eb8-56a6188a5fc0
title: IInkAnalysisRecognizer::GetCapabilities method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalysisRecognizer.GetCapabilities
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalysisRecognizer::GetCapabilities method

Retrieves the capabilities of the recognizer.

## Syntax


```C++
HRESULT GetCapabilities(
  [out] InkAnalysisRecognizerCapabilities *pCapabilities
);
```



## Parameters

<dl> <dt>

*pCapabilities* \[out\]
</dt> <dd>

A bitwise combination of [**RecognizerCapabilities**](recognizercapabilities.md) values.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

This value is constant for each [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md)

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
</dt> <dt>

[**RecognizerCapabilities**](recognizercapabilities.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




