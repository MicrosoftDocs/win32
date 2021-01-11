---
description: Retrieves the name of the recognizer.
ms.assetid: bd97fead-1e80-49dc-ada0-38eb5dc015ae
title: IInkAnalysisRecognizer::GetName method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalysisRecognizer.GetName
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalysisRecognizer::GetName method

Retrieves the name of the recognizer.

## Syntax


```C++
HRESULT GetName(
  [out] BSTR *pbstrName
);
```



## Parameters

<dl> <dt>

*pbstrName* \[out\]
</dt> <dd>

The name of the recognizer.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) on \**pbstrName* when you no longer need to use the string.

 

The name is localized for the region-neutral language that the recognizer supports.

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

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

