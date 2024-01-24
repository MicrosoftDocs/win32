---
description: Saves analysis results for a specific context node collection associated with an IInkAnalyzer.
ms.assetid: 671bdb11-6e30-4254-b320-208face1f593
title: IInkAnalyzer::SaveResultsForNodes method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.SaveResultsForNodes
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::SaveResultsForNodes method

Saves analysis results for a specific context node collection associated with an [**IInkAnalyzer**](iinkanalyzer.md).

## Syntax


```C++
HRESULT SaveResultsForNodes(
  [in]      IContextNodes *pContextNodes,
  [in, out] ULONG         *pulSerializedDataSize,
  [out]     BYTE          **ppbSerializedData
);
```



## Parameters

<dl> <dt>

*pContextNodes* \[in\]
</dt> <dd>

The [**IContextNode**](icontextnode.md) collection for which to save analysis results.

</dd> <dt>

*pulSerializedDataSize* \[in, out\]
</dt> <dd>

The number of bytes in *ppbSerializedData*.

</dd> <dt>

*ppbSerializedData* \[out\]
</dt> <dd>

Pointer to the serialized analysis data.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree) on \**ppbSerializedData* when you no longer need the information.

 

This method saves the current analysis results for the [**IContextNode**](icontextnode.md) objects in *pContextNodes* and all of their ancestor and descendant context nodes. This method does not save any stroke data. It is the responsibility of your application to synchronize any analysis results and corresponding stroke data, if it persists.

If the [**IContextNode**](icontextnode.md) object to be saved is only partially populated, this method returns an error code (see [**IContextNode::GetPartiallyPopulated**](icontextnode-getpartiallypopulated.md)).

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

[**IInkAnalyzer::SaveResultsForStrokes Method**](iinkanalyzer-saveresultsforstrokes.md)
</dt> <dt>

[**IContextNode**](icontextnode.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

