---
description: Occurs when the final analysis stage is finished.
ms.assetid: 97318c2d-980e-436c-b97d-e064bace5bf0
title: '_IAnalysisEvents::Results event (IACom.h)'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- _IAnalysisEvents.Results
api_type: 
- COM
api_location: 
- IACom.dll
---

# \_IAnalysisEvents::Results event

Occurs when the final analysis stage is finished.

## Syntax


```C++
HRESULT Results(
  [in] IInkAnalyzer    *pInkAnalyzer,
  [in] IAnalysisStatus *pAnalysisStatus
);
```



## Parameters

<dl> <dt>

*pInkAnalyzer* \[in\]
</dt> <dd>

The [**IInkAnalyzer**](iinkanalyzer.md) that produces the analysis results.

</dd> <dt>

*pAnalysisStatus* \[in\]
</dt> <dd>

The [**IAnalysisStatus**](ianalysisstatus.md) object that represents the status of the analysis.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

The [**IInkAnalyzer**](iinkanalyzer.md) raises this event after it has reconciled the results for the final analysis stage.

If your application calls [**IInkAnalyzer::BackgroundAnalyze Method**](iinkanalyzer-backgroundanalyze.md), this event signals when analysis results are ready.

If your application maintains its own data structure, which is synchronized with that of the [**IInkAnalyzer**](iinkanalyzer.md), this event indicates that the **IInkAnalyzer** has finished making changes to its internal data for this analysis stage.

Lock your data structure when the [**IInkAnalyzer**](iinkanalyzer.md) raises the [**\_IAnalysisProxyEvents::InkAnalyzerStateChanging**](-ianalysisproxyevents-inkanalyzerstatechanging.md) event. Changes to your data structure during this phase of analysis can cause errors in ink analysis and synchronization. Unlock your data structure when the **IInkAnalyzer** raises the [**\_IAnalysisEvents::IntermediateResults**](-ianalysisevents-intermediateresults.md) or **\_IAnalysisEvents::Results** event.

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

[**IAnalysisStatus**](ianalysisstatus.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




