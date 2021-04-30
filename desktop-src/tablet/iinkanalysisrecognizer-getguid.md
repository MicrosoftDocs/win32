---
description: Retrieves the globally unique identifier (GUID) of the recognizer.
ms.assetid: 9b98993b-eaf3-4207-9d56-33efeceb75cf
title: IInkAnalysisRecognizer::GetGuid method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalysisRecognizer.GetGuid
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalysisRecognizer::GetGuid method

Retrieves the globally unique identifier (GUID) of the recognizer.

## Syntax


```C++
HRESULT GetGuid(
  [out] GUID *pId
);
```



## Parameters

<dl> <dt>

*pId* \[out\]
</dt> <dd>

The GUID that identifies this [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md).

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
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




