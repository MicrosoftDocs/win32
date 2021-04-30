---
description: Exposes a method to evaluate whether an IContextNode object meets or fails a specified criteria.
ms.assetid: 8b094882-e739-4088-87de-6ef4719b0b5b
title: IMatchesCriteriaCallBack interface (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMatchesCriteriaCallBack
api_type: 
- COM
api_location: 
- IACom.dll
---

# IMatchesCriteriaCallBack interface

Exposes a method to evaluate whether an [**IContextNode**](icontextnode.md) object meets or fails a specified criteria.

## Members

The **IMatchesCriteriaCallBack** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IMatchesCriteriaCallBack** also has these types of members:

-   [Methods](#methods)

### Methods

The **IMatchesCriteriaCallBack** interface has these methods.



| Method                                                                      | Description                                                                                                                                  |
|:----------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------|
| [**EvaluateContextNode**](imatchescriteriacallback-evaluatecontextnode.md) | When overridden in a derived class, evaluates whether a specified [**IContextNode**](icontextnode.md) object meets the criteria.<br/> |



 

## Remarks

To use [**IInkAnalyzer::FindNodesWithCallBack Method**](iinkanalyzer-findnodeswithcallback.md) or [**IInkAnalyzer::FindNodesWithCallBackInSubTree Method**](iinkanalyzer-findnodeswithcallbackinsubtree.md), create a class that implements **IMatchesCriteriaCallBack**. Implement [**IMatchesCriteriaCallBack::EvaluateContextNode**](imatchescriteriacallback-evaluatecontextnode.md) to return **VARIANT\_TRUE** if the [**IContextNode**](icontextnode.md) object matches your criteria, and **VARIANT\_FALSE** otherwise. For some criteria, you may need to provide a means of initializing or maintaining the state of your **IMatchesCriteriaCallBack** object.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IInkAnalyzer::FindNodesWithCallBack Method**](iinkanalyzer-findnodeswithcallback.md)
</dt> <dt>

[**IInkAnalyzer::FindNodesWithCallBackInSubTree Method**](iinkanalyzer-findnodeswithcallbackinsubtree.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

