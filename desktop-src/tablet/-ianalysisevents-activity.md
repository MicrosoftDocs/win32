---
description: Occurs when the IInkAnalyzer::Analyze method or IInkAnalyzer::BackgroundAnalyze method is called.
ms.assetid: 339b41c6-f388-4b81-b2bc-3705b39d9cc9
title: '_IAnalysisEvents::Activity event (IACom.h)'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- _IAnalysisEvents.Activity
api_type: 
- COM
api_location: 
- IACom.dll
---

# \_IAnalysisEvents::Activity event

Occurs when the [**IInkAnalyzer::Analyze**](iinkanalyzer-analyze.md) method or [**IInkAnalyzer::BackgroundAnalyze**](iinkanalyzer-backgroundanalyze.md) method is called.

## Syntax


```C++
HRESULT Activity();
```



## Parameters

This event has no parameters.

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

This event indicates that the [**IInkAnalyzer**](iinkanalyzer.md) is performing ink analysis. This event does not indicate the progress of the ink analysis operation.

To do any of the following, implement an **\_IAnalysisEvents::Activity** event handler:

-   Indicate to the user that the ink analyzer is performing ink analysis.
-   Process user input during synchronous analysis.
-   Receive notification of system requests, such as repainting of the application's window, during ink analysis.

The [**IInkAnalyzer**](iinkanalyzer.md) raises this event frequently during the layout analysis phase and the writing and drawing classification phase of ink analysis. The **IInkAnalyzer** raises this event during the handwriting recognition phase before and after accessing an ink recognizer.

The number of activity events an [**IInkAnalyzer**](iinkanalyzer.md) generates is affected by:

-   The ink recognizer that the [**IInkAnalyzer**](iinkanalyzer.md) applies to ink recognition.
-   The number and length of strokes that the [**IInkAnalyzer**](iinkanalyzer.md) is analyzing.
-   The number of strokes that are classified as writing.

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

[**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md)
</dt> <dt>

[**IInkAnalyzer::Analyze Method**](iinkanalyzer-analyze.md)
</dt> <dt>

[**IInkAnalyzer::BackgroundAnalyze Method**](iinkanalyzer-backgroundanalyze.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




