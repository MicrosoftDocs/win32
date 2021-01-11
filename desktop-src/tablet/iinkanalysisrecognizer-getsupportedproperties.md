---
description: Retrieves the globally unique identifiers (GUIDs) for the properties that this IInkAnalysisRecognizer can generate for analysis results.
ms.assetid: 3a36bc6c-5067-4291-9119-bc6836d32c21
title: IInkAnalysisRecognizer::GetSupportedProperties method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalysisRecognizer.GetSupportedProperties
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalysisRecognizer::GetSupportedProperties method

Retrieves the globally unique identifiers (GUIDs) for the properties that this [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) can generate for analysis results.

## Syntax


```C++
HRESULT GetSupportedProperties(
  [in, out] ULONG *pulPropertiesCount,
  [out]     GUID  **ppProperties
);
```



## Parameters

<dl> <dt>

*pulPropertiesCount* \[in, out\]
</dt> <dd>

The number of GUIDs in *ppProperties*.

</dd> <dt>

*ppProperties* \[out\]
</dt> <dd>

A pointer to the GUIDs of properties that this [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) can generate for analysis results.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, use [**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree) to release the memory from \**ppProperties* when you no longer need the information.

 

A recognizer can support line metrics, line numbers, confidence levels, and so on. For a complete list of the properties that a recognizer can support, see [RecognitionProperty Constants](recognitionproperty-constants.md).

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

[RecognitionProperty Constants](recognitionproperty-constants.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

