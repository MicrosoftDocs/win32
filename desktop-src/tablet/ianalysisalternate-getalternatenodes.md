---
Description: Gets the IContextNode objects that are associated with this alternate.
ms.assetid: 6dfae9cc-d9d2-44de-b6cf-80bbcd296390
title: IAnalysisAlternateGetAlternateNodes method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IAnalysisAlternate::GetAlternateNodes method

Gets the [**IContextNode**](icontextnode.md) objects that are associated with this alternate.

## Syntax


```C++
HRESULT GetAlternateNodes(
  [out] IContextNodes **ppAlternateNodes
);
```



## Parameters

<dl> <dt>

*ppAlternateNodes* \[out\]
</dt> <dd>

A pointer to the [**IContextNodes**](icontextnodes.md) collection that contains [**IContextNode**](icontextnode.md) objects that are associated with this alternate.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> \[!Caution\]  
> To avoid a memory leak, call [**IUnknown::Release**](https://msdn.microsoft.com/library/windows/desktop/ms682317) on \**ppAlternateNodes* when you no longer need to use the context node collection.

 

This method returns the leaf context nodes that are associated with this alternate. Examples of leaf nodes are InkWord, TextWord, Image, InkDrawing, and InkBullet context nodes. For more information, see [**IContextNode::GetType**](icontextnode-gettype.md) and [Context Node Types](context-node-types.md).

Because they correspond to alternates, these [**IContextNode**](icontextnode.md) objects are not descendants of the [**IInkAnalyzer**](iinkanalyzer.md) object's root **IContextNode** (see [**IInkAnalyzer::GetRootNode Method**](iinkanalyzer-getrootnode.md)) unless they are the top alternate, which is the first element in an [**IAnalysisAlternates**](ianalysisalternates.md) collection.

## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IAnalysisAlternate**](ianalysisalternate.md)
</dt> <dt>

[**IContextNode**](icontextnode.md)
</dt> <dt>

[**IContextNodes**](icontextnodes.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> <dt>

[System.Windows.Ink.AnalysisCore.AnalysisAlternateBase.AlternateNodes](ianalysisalternate-getalternatenodes.md)
</dt> </dl>

 

 




