---
description: Saves all analysis results for an IInkAnalyzer.
ms.assetid: 538eb781-d831-475b-ba09-271d71f6a6bf
title: IInkAnalyzer::SaveResults method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.SaveResults
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::SaveResults method

Saves all analysis results for an [**IInkAnalyzer**](iinkanalyzer.md).

## Syntax


```C++
HRESULT SaveResults(
  [out] ULONG *pulSerializedDataSize,
  [out] BYTE  **ppbSerializedData
);
```



## Parameters

<dl> <dt>

*pulSerializedDataSize* \[out\]
</dt> <dd>

The number of bytes in *ppbSerializedData*.

</dd> <dt>

*ppbSerializedData* \[out\]
</dt> <dd>

An array containing the saved analysis results.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, use [**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree) to release the memory from \**ppbSerializedData* when you no longer need the information.

 

This method saves all the current analysis results, which include current analysis hint and custom recognizer nodes (see [**IContextNode::GetType**](icontextnode-gettype.md)). This method does not save any stroke data. It is the responsibility of your application to synchronize any analysis results and corresponding strokes if it persists data.

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

[**IInkAnalyzer::SaveResultsForNodes Method**](iinkanalyzer-saveresultsfornodes.md)
</dt> <dt>

[**IInkAnalyzer::SaveResultsForStrokes Method**](iinkanalyzer-saveresultsforstrokes.md)
</dt> <dt>

[**IContextNode**](icontextnode.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

