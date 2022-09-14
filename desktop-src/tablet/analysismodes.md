---
description: Specifies how the IInkAnalyzer performs ink analysis.
ms.assetid: bc526445-0c9c-4c53-8b02-32cf758266e6
title: AnalysisModes enumeration (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AnalysisModes
api_type: 
- HeaderDef
api_location: 
- IACom.h
---

# AnalysisModes enumeration

Specifies how the [**IInkAnalyzer**](iinkanalyzer.md) performs ink analysis.

## Syntax


```C++
typedef enum AnalysisModes { 
  AnalysisModes_None                     = 0x0000,
  AnalysisModes_AutomaticReconciliation  = 0x0002,
  AnalysisModes_StrokeCacheAutoCleanup   = 0x0004,
  AnalysisModes_PersonalizationEnabled   = 0x0008,
  AnalysisModes_Default                  = 0x000d
} AnalysisModes;
```



## Constants

<dl> <dt>

<span id="AnalysisModes_None"></span><span id="analysismodes_none"></span><span id="ANALYSISMODES_NONE"></span>**AnalysisModes\_None**
</dt> <dd>

No modes are specified.

</dd> <dt>

<span id="AnalysisModes_AutomaticReconciliation"></span><span id="analysismodes_automaticreconciliation"></span><span id="ANALYSISMODES_AUTOMATICRECONCILIATION"></span>**AnalysisModes\_AutomaticReconciliation**
</dt> <dd>

Whether the [**IInkAnalyzer**](iinkanalyzer.md) automatically starts the reconciliation operation as soon as the intermediate or final results are ready.

If this mode is enabled, the [**\_IAnalysisEvents::ReadyToReconcile**](-ianalysisevents-readytoreconcile.md) event is not raised. If this mode is disabled, the **\_IAnalysisEvents::ReadyToReconcile** event is raised.

</dd> <dt>

<span id="AnalysisModes_StrokeCacheAutoCleanup"></span><span id="analysismodes_strokecacheautocleanup"></span><span id="ANALYSISMODES_STROKECACHEAUTOCLEANUP"></span>**AnalysisModes\_StrokeCacheAutoCleanup**
</dt> <dd>

Whether the [**IInkAnalyzer**](iinkanalyzer.md) automatically clears unneeded strokes from the stroke cache before performing analysis.

If this mode is enabled, the [**IInkAnalyzer**](iinkanalyzer.md) clears the stroke data before performing analysis. Your code must also then handle the [**\_IAnalysisEvents::UpdateStrokesCache**](-ianalysisevents-updatestrokescache.md) event. If the **\_IAnalysisEvents::UpdateStrokesCache** event is not handled, an exception is raised. This check is done both at the Analyze (or BackgroundAnalyze) and Reconciliation phases.

If this mode is disabled, the [**IInkAnalyzer**](iinkanalyzer.md) does not clear the stroke data. To clear the stroke data, call [**IInkAnalyzer::ClearStrokeData Method**](iinkanalyzer-clearstrokedata.md). If this mode is disabled, the [**\_IAnalysisEvents::UpdateStrokesCache**](-ianalysisevents-updatestrokescache.md) event is raised so the **IInkAnalyzer** can retrieve the latest stroke data for any strokes that have had their cache cleared. If the stroke cache is cleared, but the **\_IAnalysisEvents::UpdateStrokesCache** event is not handled, an exception is raised.

</dd> <dt>

<span id="AnalysisModes_PersonalizationEnabled"></span><span id="analysismodes_personalizationenabled"></span><span id="ANALYSISMODES_PERSONALIZATIONENABLED"></span>**AnalysisModes\_PersonalizationEnabled**
</dt> <dd>

Personalization of handwriting recognition is enabled.

</dd> <dt>

<span id="AnalysisModes_Default"></span><span id="analysismodes_default"></span><span id="ANALYSISMODES_DEFAULT"></span>**AnalysisModes\_Default**
</dt> <dd>

All modes are enabled.

</dd> </dl>

## Remarks

This enumeration allows a bitwise combination of its member values.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |



## See also

<dl> <dt>

[**IInkAnalyzer::GetAnalysisModes Method**](iinkanalyzer-getanalysismodes.md)
</dt> <dt>

[**IInkAnalyzer::SetAnalysisModes Method**](iinkanalyzer-setanalysismodes.md)
</dt> <dt>

[**\_IAnalysisEvents::IntermediateResults**](-ianalysisevents-intermediateresults.md)
</dt> <dt>

[**\_IAnalysisEvents::ReadyToReconcile**](-ianalysisevents-readytoreconcile.md)
</dt> <dt>

[**\_IAnalysisEvents::UpdateStrokesCache**](-ianalysisevents-updatestrokescache.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




