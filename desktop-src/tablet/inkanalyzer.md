---
Description: Implements the IInkAnalyzer interface.
ms.assetid: 3a19db78-df14-43c2-9e3e-8cf674aa7b9c
title: InkAnalyzer class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InkAnalyzer
api_type: 
- COM
api_location: 
- IACom.dll
---

# InkAnalyzer class

Implements the [**IInkAnalyzer**](iinkanalyzer.md) interface.

## Remarks

This class implements the [**IInkAnalyzer**](iinkanalyzer.md) COM interface.

[\_IAnalysisEvents](-ianalysisevents.md) is the default source of events and provides standard events for the [**IInkAnalyzer**](iinkanalyzer.md).

[**\_IAnalysisProxyEvents**](-ianalysisproxyevents.md) provides the data proxy events for the [**IInkAnalyzer**](iinkanalyzer.md). For more information, see [Data Proxy with Ink Analysis](data-proxy-with-ink-analysis.md).

## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**AnalysisModes**](analysismodes.md)
</dt> <dt>

[**IAnalysisAlternate**](ianalysisalternate.md)
</dt> <dt>

[**IAnalysisStatus**](ianalysisstatus.md)
</dt> <dt>

[**IContextLink**](icontextlink.md)
</dt> <dt>

[**IContextNode**](icontextnode.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




