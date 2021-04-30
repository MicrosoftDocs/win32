---
description: Retrieves analysis alternates for the nodes in a specified IContextNodes collection.
ms.assetid: 7d047808-4360-442d-8fd9-4ee4aeeed2c9
title: IInkAnalyzer::GetAlternatesForContextNodes method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.GetAlternatesForContextNodes
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::GetAlternatesForContextNodes method

Retrieves analysis alternates for the nodes in a specified [**IContextNodes**](icontextnodes.md) collection.

## Syntax


```C++
HRESULT GetAlternatesForContextNodes(
  [in]  IContextNodes      *pContextNodes,
  [in]  ULONG              ulMaximumAlternates,
  [out] AnalysisAlternates **ppAlternates
);
```



## Parameters

<dl> <dt>

*pContextNodes* \[in\]
</dt> <dd>

The [**IContextNodes**](icontextnodes.md) collection for which the analysis alternatives are returned.

</dd> <dt>

*ulMaximumAlternates* \[in\]
</dt> <dd>

The maximum number of alternatives to return.

</dd> <dt>

*ppAlternates* \[out\]
</dt> <dd>

The [**IAnalysisAlternates**](ianalysisalternates.md) object containing the analysis alternatives.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on *ppAlternates* when you no longer need to use the object.

 

The top [**IAnalysisAlternate**](ianalysisalternate.md) is returned as the first alternate of the collection.

The [**IContextNode**](icontextnode.md) objects in *pContextNodes* do not have to represent adjacent areas of the document.

For each analysis hint in nodes, the [**IInkAnalyzer**](iinkanalyzer.md) returns only the top alternate.

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

[**IAnalysisAlternate**](ianalysisalternate.md)
</dt> <dt>

[**IAnalysisAlternates**](ianalysisalternates.md)
</dt> <dt>

[**IInkAnalyzer::GetAlternates Method**](iinkanalyzer-getalternates.md)
</dt> <dt>

[**IInkAnalyzer::GetAlternatesForStrokes Method**](iinkanalyzer-getalternatesforstrokes.md)
</dt> <dt>

[**IInkAnalyzer::ModifyTopAlternate Method**](iinkanalyzer-modifytopalternate.md)
</dt> <dt>

[**IInkAnalyzer::ModifyTopAlternateWithConfirmation Method**](iinkanalyzer-modifytopalternatewithconfirmation.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

