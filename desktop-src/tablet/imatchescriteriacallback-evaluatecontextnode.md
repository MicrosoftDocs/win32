---
description: When overridden in a derived class, evaluates whether a specified IContextNode object meets the criteria.
ms.assetid: ade8e59c-6aeb-4a87-a95d-229f8f0b2223
title: IMatchesCriteriaCallBack::EvaluateContextNode method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMatchesCriteriaCallBack.EvaluateContextNode
api_type: 
- COM
api_location: 
- IACom.dll
---

# IMatchesCriteriaCallBack::EvaluateContextNode method

When overridden in a derived class, evaluates whether a specified [**IContextNode**](icontextnode.md) object meets the criteria.

## Syntax


```C++
HRESULT EvaluateContextNode(
  [in]  IContextNode *pContextNodeToEvaluate,
  [out] VARIANT_BOOL *pbResult
);
```



## Parameters

<dl> <dt>

*pContextNodeToEvaluate* \[in\]
</dt> <dd>

The [**IContextNode**](icontextnode.md) object to evaluate.

</dd> <dt>

*pbResult* \[out\]
</dt> <dd>

**VARIANT\_TRUE** if *pContextNodeToEvaluate* matches the criteria; otherwise, **VARIANT\_FALSE**.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

To use [**IInkAnalyzer::FindNodesWithCallBack Method**](iinkanalyzer-findnodeswithcallback.md) or [**IInkAnalyzer::FindNodesWithCallBackInSubTree Method**](iinkanalyzer-findnodeswithcallbackinsubtree.md), create a class that implements [**IMatchesCriteriaCallBack**](imatchescriteriacallback.md). Implement **IMatchesCriteriaCallBack::EvaluateContextNode** to return **VARIANT\_TRUE** if the [**IContextNode**](icontextnode.md) object matches your criteria, and **VARIANT\_FALSE** otherwise. For some criteria, you may need to provide a means of initializing or maintaining the state of your **IMatchesCriteriaCallBack** object.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IMatchesCriteriaCallBack**](imatchescriteriacallback.md)
</dt> <dt>

[**IInkAnalyzer::FindNodesWithCallBack Method**](iinkanalyzer-findnodeswithcallback.md)
</dt> <dt>

[**IInkAnalyzer::FindNodesWithCallBackInSubTree Method**](iinkanalyzer-findnodeswithcallbackinsubtree.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




