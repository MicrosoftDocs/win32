---
description: Retrieves the error code for the background ink analysis operation if an error occurred.
ms.assetid: 0255751e-9b2a-46f1-aa45-6509f9d1c658
title: IAnalysisWarning::GetBackgroundError method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisWarning.GetBackgroundError
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisWarning::GetBackgroundError method

Retrieves the error code for the background ink analysis operation if an error occurred.

## Syntax


```C++
HRESULT GetBackgroundError();
```



## Parameters

This method has no parameters.

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

If an error occurs within a background analysis operation, the [**IInkAnalyzer**](iinkanalyzer.md) cannot return the error code because it is occurring in a different thread. Instead, the [**\_IAnalysisEvents::Results**](-ianalysisevents-results.md) event handler receives an [**IAnalysisStatus**](ianalysisstatus.md) that contains an [**IAnalysisWarning**](ianalysiswarning.md) with an [**AnalysisWarningCode**](/windows/desktop/tablet/analysiswarningcode) of **AnalysisWarningCode\_BackgroundException**. This **IAnalysisWarning** contains the error code for the background analysis operation. In general, your **\_IAnalysisEvents::Results** event handler will return this error code so that it can be handled elsewhere in your application.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IAnalysisWarning**](ianalysiswarning.md)
</dt> <dt>

[**IAnalysisStatus**](ianalysisstatus.md)
</dt> <dt>

[**IInkAnalyzer::BackgroundAnalyze Method**](iinkanalyzer-backgroundanalyze.md)
</dt> <dt>

[**\_IAnalysisEvents::Results**](-ianalysisevents-results.md)
</dt> <dt>

[**AnalysisWarningCode**](/windows/desktop/tablet/analysiswarningcode)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

