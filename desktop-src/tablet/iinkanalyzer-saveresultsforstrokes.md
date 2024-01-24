---
description: Saves analysis results for the specified strokes associated with an IInkAnalyzer.
ms.assetid: 6ff29b95-6c76-4e3d-b4c0-5e7cb6a9ddf9
title: IInkAnalyzer::SaveResultsForStrokes method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.SaveResultsForStrokes
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::SaveResultsForStrokes method

Saves analysis results for the specified strokes associated with an [**IInkAnalyzer**](iinkanalyzer.md).

## Syntax


```C++
HRESULT SaveResultsForStrokes(
  [in]          ULONG ulStrokeIdsCount,
  [in]          LONG  *plStrokeIds,
  [in, out]     ULONG *pulSerializedDataSize,
  [out, retval] BYTE  **ppbSerializedData
);
```



## Parameters

<dl> <dt>

*ulStrokeIdsCount* \[in\]
</dt> <dd>

The number of stroke identifiers in **plStrokeIds**.

</dd> <dt>

*plStrokeIds* \[in\]
</dt> <dd>

The array of stroke identifiers.

</dd> <dt>

*pulSerializedDataSize* \[in, out\]
</dt> <dd>

The number of bytes in *ppbSerializedData*.

</dd> <dt>

*ppbSerializedData* \[out, retval\]
</dt> <dd>

Pointer to the serialized analysis data.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree) on \**ppbSerializedData* when you no longer need the information.

 

This method saves the current analysis results for the specified strokes. This method saves the ink leaf [**IContextNode**](icontextnode.md) objects containing the strokes and all of the ancestors of those context nodes. This method does not save any stroke data or analysis hint nodes. It is the responsibility of your application to synchronize any analysis results and corresponding stroke data, if it persists.

This method returns an error code when an [**IContextNode**](icontextnode.md) object to save is partially populated (see [**IContextNode::GetPartiallyPopulated**](icontextnode-getpartiallypopulated.md)).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IInkAnalyzer**](iinkanalyzer.md)
</dt> <dt>

[**IInkAnalyzer::LoadResults Method**](iinkanalyzer-loadresults.md)
</dt> <dt>

[**IInkAnalyzer::SaveResults Method**](iinkanalyzer-saveresults.md)
</dt> <dt>

[**IInkAnalyzer::SaveResultsForNodes Method**](iinkanalyzer-saveresultsfornodes.md)
</dt> <dt>

[**IContextNode**](icontextnode.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

