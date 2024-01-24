---
description: Specifies events associated with the analysis steps of an IInkAnalyzer object.
ms.assetid: 8cb75f99-aa39-44d1-a055-dc1fb3f6b292
title: '_IAnalysisEvents interface'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- _IAnalysisEvents
api_type: 
- COM
api_location: 
---

# \_IAnalysisEvents interface

Specifies events associated with the analysis steps of an [**IInkAnalyzer**](iinkanalyzer.md) object.

-   [Events](/windows)

### Events

The **\_IAnalysisEvents** interface has these events.



| Event                                                               | Description                                                                                                                                                                                    |
|:--------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Activity**](-ianalysisevents-activity.md)                       | Occurs during calls to the [**IInkAnalyzer::Analyze Method**](iinkanalyzer-analyze.md) or [**IInkAnalyzer::BackgroundAnalyze Method**](iinkanalyzer-backgroundanalyze.md) method.<br/> |
| [**IntermediateResults**](-ianalysisevents-intermediateresults.md) | Occurs when the current intermediate analysis stage is finished.<br/>                                                                                                                    |
| [**ReadyToReconcile**](-ianalysisevents-readytoreconcile.md)       | Occurs when the [**IInkAnalyzer**](iinkanalyzer.md) is ready to reconcile its background analysis results with its current state.<br/>                                                  |
| [**Results**](-ianalysisevents-results.md)                         | Occurs when the final analysis stage is finished.<br/>                                                                                                                                   |
| [**UpdateStrokesCache**](-ianalysisevents-updatestrokescache.md)   | Occurs before the [**IInkAnalyzer**](iinkanalyzer.md) accesses stroke data.<br/>                                                                                                        |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                     |



## See also

<dl> <dt>

[**\_IAnalysisProxyEvents**](-ianalysisproxyevents.md)
</dt> <dt>

[**IInkAnalyzer**](iinkanalyzer.md)
</dt> <dt>

[**IInkAnalyzer::Analyze Method**](iinkanalyzer-analyze.md)
</dt> <dt>

[**IInkAnalyzer::BackgroundAnalyze Method**](iinkanalyzer-backgroundanalyze.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

