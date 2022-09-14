---
description: Changes the current top alternate to the specified IAnalysisAlternate.
ms.assetid: 0867a662-d172-4ca2-a41f-49c0ea454768
title: IInkAnalyzer::ModifyTopAlternateWithConfirmation method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.ModifyTopAlternateWithConfirmation
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::ModifyTopAlternateWithConfirmation method

Changes the current top alternate to the specified [**IAnalysisAlternate**](ianalysisalternate.md).

## Syntax


```C++
HRESULT ModifyTopAlternateWithConfirmation(
  [in] IAnalysisAlternate *alternate,
  [in] VARIANT_BOOL       fconfirmAutomatically
);
```



## Parameters

<dl> <dt>

*alternate* \[in\]
</dt> <dd>

The analysis alternate to set as the new top alternate.

</dd> <dt>

*fconfirmAutomatically* \[in\]
</dt> <dd>

**VARIANT\_TRUE** to set all of the ink leaf context nodes that correspond to the analysis alternate to a confirmation type of **ConfirmationType\_NodeTypeAndProperties** (see [**IContextNode::IsConfirmed**](icontextnode-isconfirmed.md) and [**ConfirmationType**](confirmationtype.md)); **VARIANT\_FALSE** to set all of the ink leaf context nodes that correspond to the analysis alternate to a confirmation type of **ConfirmationType\_None**.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

To get analysis alternates, use [**IInkAnalyzer::GetAlternates Method**](iinkanalyzer-getalternates.md), [**IInkAnalyzer::GetAlternatesForContextNodes Method**](iinkanalyzer-getalternatesforcontextnodes.md), or [**IInkAnalyzer::GetAlternatesForStrokes Method**](iinkanalyzer-getalternatesforstrokes.md). To get the context node objects associated with an analysis alternate, use [**IAnalysisAlternate::GetAlternateNodes Method**](ianalysisalternate-getalternatenodes.md).

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

[**Ink Analysis ConfirmationType**](confirmationtype.md)
</dt> <dt>

[Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




