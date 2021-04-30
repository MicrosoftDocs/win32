---
description: Clears stroke packet data from the IInkAnalyzer.
ms.assetid: c87a1e73-5e3f-4d27-93e9-e30d9ec5d9e3
title: IInkAnalyzer::ClearStrokeData method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.ClearStrokeData
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::ClearStrokeData method

Clears stroke packet data from the [**IInkAnalyzer**](iinkanalyzer.md).

## Syntax


```C++
HRESULT ClearStrokeData(
  [in] LONG lStrokeId
);
```



## Parameters

<dl> <dt>

*lStrokeId* \[in\]
</dt> <dd>

The identifier of the stroke for which the packet data is cleared.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

Use this method when packet data for a stroke changes, such as when a stroke is moved or otherwise transformed. The [**IInkAnalyzer**](iinkanalyzer.md) raises the [**\_IAnalysisEvents::UpdateStrokesCache**](-ianalysisevents-updatestrokescache.md) event when it needs stroke packet data from a stroke for which the packet data has been cleared.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IInkAnalyzer**](iinkanalyzer.md)
</dt> <dt>

[**IInkAnalyzer::UpdateStrokesData Method**](iinkanalyzer-updatestrokesdata.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




