---
description: Occurs before the IInkAnalyzer accesses stroke data.
ms.assetid: fed46476-4531-4516-9375-d7b654efb3be
title: '_IAnalysisEvents::UpdateStrokesCache event (IACom.h)'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- _IAnalysisEvents.UpdateStrokesCache
api_type: 
- COM
api_location: 
- IACom.dll
---

# \_IAnalysisEvents::UpdateStrokesCache event

Occurs before the [**IInkAnalyzer**](iinkanalyzer.md) accesses stroke data.

## Syntax


```C++
HRESULT UpdateStrokesCache(
  [in] ULONG ulStrokeIdsCount,
  [in] LONG  *plStrokeIds
);
```



## Parameters

<dl> <dt>

*ulStrokeIdsCount* \[in\]
</dt> <dd>

The number of stroke identifiers in *plStrokeIds*.

</dd> <dt>

*plStrokeIds* \[in\]
</dt> <dd>

The identifiers of the strokes whose packet data has been cleared.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

The [**IInkAnalyzer**](iinkanalyzer.md) raises this event during ink analysis when it accesses one or more strokes for which the packet data has been cleared. To update the stroke packet data, use the [**IInkAnalyzer::UpdateStrokesData Method**](iinkanalyzer-updatestrokesdata.md) method.

The [**IInkAnalyzer**](iinkanalyzer.md) does not raise this event when accessing a partially populated ink leaf node when the location of the node has not been set by the **IInkAnalyzer**.

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

[**\_IAnalysisEvents**](-ianalysisevents.md)
</dt> <dt>

[**\_IAnalysisProxyEvents**](-ianalysisproxyevents.md)
</dt> <dt>

[**IInkAnalyzer**](iinkanalyzer.md)
</dt> <dt>

[**IInkAnalyzer::Analyze Method**](iinkanalyzer-analyze.md)
</dt> <dt>

[**IInkAnalyzer::BackgroundAnalyze Method**](iinkanalyzer-backgroundanalyze.md)
</dt> <dt>

[**IInkAnalyzer::UpdateStrokesData Method**](iinkanalyzer-updatestrokesdata.md)
</dt> <dt>

[**IContextNode::CreatePartiallyPopulatedSubNode**](icontextnode-createpartiallypopulatedsubnode.md)
</dt> <dt>

[**IContextNode::GetPartiallyPopulated**](icontextnode-getpartiallypopulated.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




