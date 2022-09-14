---
description: Changes the current top alternate to the specified alternate and clears the confirmation type for all IContextNode objects associated with the alternate.
ms.assetid: a4ff7e82-623f-4501-9641-5235c3083757
title: IInkAnalyzer::ModifyTopAlternate method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.ModifyTopAlternate
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::ModifyTopAlternate method

Changes the current top alternate to the specified alternate and clears the confirmation type for all [**IContextNode**](icontextnode.md) objects associated with the alternate.

## Syntax


```C++
HRESULT ModifyTopAlternate(
  [in] IAnalysisAlternate *pAlternate
);
```



## Parameters

<dl> <dt>

*pAlternate* \[in\]
</dt> <dd>

The [**IAnalysisAlternate**](ianalysisalternate.md) object containing the new top alternate.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

To get analysis alternates, use [**IInkAnalyzer::GetAlternates Method**](iinkanalyzer-getalternates.md), [**IInkAnalyzer::GetAlternatesForContextNodes Method**](iinkanalyzer-getalternatesforcontextnodes.md), or [**IInkAnalyzer::GetAlternatesForStrokes Method**](iinkanalyzer-getalternatesforstrokes.md). To get the [**IContextNode**](icontextnode.md) objects associated with an analysis alternate, use [**IAnalysisAlternate::GetAlternateNodes Method**](ianalysisalternate-getalternatenodes.md).

To change the confirmation type for a context node, use [**IContextNode::Confirm**](icontextnode-confirm.md).

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

[**IContextNode**](icontextnode.md)
</dt> <dt>

[**ConfirmationType**](confirmationtype.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




