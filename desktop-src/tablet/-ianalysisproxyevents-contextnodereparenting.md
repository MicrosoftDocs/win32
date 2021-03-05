---
description: Occurs before the IInkAnalyzer moves an IContextNode object by changing its parent node.
ms.assetid: 91261270-aa7c-4f0a-a790-1b2bf322a3ad
title: '_IAnalysisProxyEvents::ContextNodeReparenting event (IACom.h)'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- _IAnalysisProxyEvents.ContextNodeReparenting
api_type: 
- COM
api_location: 
- IACom.dll
---

# \_IAnalysisProxyEvents::ContextNodeReparenting event

Occurs before the [**IInkAnalyzer**](iinkanalyzer.md) moves an [**IContextNode**](icontextnode.md) object by changing its parent node.

## Syntax


```C++
HRESULT ContextNodeReparenting(
  [in] IInkAnalyzer *pInkAnalyzer,
  [in] IContextNode *pNewParentContextNode,
  [in] IContextNode *pContextNodeToBeReparented
);
```



## Parameters

<dl> <dt>

*pInkAnalyzer* \[in\]
</dt> <dd>

The [**IInkAnalyzer**](iinkanalyzer.md) object moving the [**IContextNode**](icontextnode.md) object.

</dd> <dt>

*pNewParentContextNode* \[in\]
</dt> <dd>

The new parent [**IContextNode**](icontextnode.md) object.

</dd> <dt>

*pContextNodeToBeReparented* \[in\]
</dt> <dd>

The [**IContextNode**](icontextnode.md) object to be moved.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

Use this event when your application maintains its own data structure, which is synchronized with that of the [**IInkAnalyzer**](iinkanalyzer.md). This event occurs during the reconcile phase of ink analysis, or in response to a method that moves an [**IContextNode**](icontextnode.md) from one collection of subnodes to another (see [**IContextNode::GetParentNode**](icontextnode-getparentnode.md) and [**IContextNode::GetSubNodes**](icontextnode-getsubnodes.md)).

For more information about synchronizing your application data with the [**IInkAnalyzer**](iinkanalyzer.md), see [Data Proxy with Ink Analysis](data-proxy-with-ink-analysis.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**\_IAnalysisProxyEvents**](-ianalysisproxyevents.md)
</dt> <dt>

[**IInkAnalyzer**](iinkanalyzer.md)
</dt> <dt>

[**IContextNode**](icontextnode.md)
</dt> <dt>

[**IContextNode::GetParentNode**](icontextnode-getparentnode.md)
</dt> <dt>

[**IContextNode::GetSubNodes**](icontextnode-getsubnodes.md)
</dt> <dt>

[**IInkAnalyzer::Analyze Method**](iinkanalyzer-analyze.md)
</dt> <dt>

[**IInkAnalyzer::BackgroundAnalyze Method**](iinkanalyzer-backgroundanalyze.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




