---
description: Retrieves the number of IInkAnalysisRecognizer objects in this collection.
ms.assetid: dfb5c530-b481-4c60-b7fe-87fe162de270
title: IInkAnalysisRecognizers::GetCount method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalysisRecognizers.GetCount
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalysisRecognizers::GetCount method

Retrieves the number of [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) objects in this collection.

## Syntax


```C++
HRESULT GetCount(
  [out, retval] ULONG *pulCount
);
```



## Parameters

<dl> <dt>

*pulCount* \[out, retval\]
</dt> <dd>

The number of [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) objects in this collection.

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

[**InkAnalysisRecognizers**](iinkanalysisrecognizers.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




