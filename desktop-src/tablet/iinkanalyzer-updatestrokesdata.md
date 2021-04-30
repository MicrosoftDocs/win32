---
description: Updates the packet data for the specified strokes.
ms.assetid: 7fca4c39-eef2-4019-86a0-27cd0e4e7510
title: IInkAnalyzer::UpdateStrokesData method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.UpdateStrokesData
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::UpdateStrokesData method

Updates the packet data for the specified strokes.

## Syntax


```C++
HRESULT UpdateStrokesData(
  [in] ULONG ulStrokeIdsCount,
  [in] LONG  *plStrokeIds,
  [in] ULONG ulStrokePacketDescriptionCount,
  [in] GUID  *pStrokePacketDescriptionGuids,
  [in] ULONG *pulPacketDataCountPerStroke,
  [in] LONG  *plStrokePacketData
);
```



## Parameters

<dl> <dt>

*ulStrokeIdsCount* \[in\]
</dt> <dd>

The number of strokes to update.

</dd> <dt>

*plStrokeIds* \[in\]
</dt> <dd>

An array containing the stroke identifiers.

</dd> <dt>

*ulStrokePacketDescriptionCount* \[in\]
</dt> <dd>

The number of properties in each packet.

</dd> <dt>

*pStrokePacketDescriptionGuids* \[in\]
</dt> <dd>

An array containing the packet property identifiers.

</dd> <dt>

*pulPacketDataCountPerStroke* \[in\]
</dt> <dd>

An array containing the number of packets in each stroke.

</dd> <dt>

*plStrokePacketData* \[in\]
</dt> <dd>

An array containing the packet data for the strokes.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

the *plStrokePacketData* parameter contains packet data for all of the strokes. The *pStrokePacketDescriptionGuids* parameter contains the globally unique identifiers (GUIDs) that describe the types of packet data included for each point in each stroke. For a complete list of available packet properties, see [PacketPropertyGuids Constants](packetpropertyguids-constants.md).

Only strokes with the same packet descriptions can be updated in a single call to **IInkAnalyzer::UpdateStrokesData Method**.

This method does not update the ink analyzer's dirty region (see [**IInkAnalyzer::GetDirtyRegion Method**](iinkanalyzer-getdirtyregion.md)).

If a specified stroke is not associated with the [**IInkAnalyzer**](iinkanalyzer.md), this method ignores the identifier.

If none of the specified strokes identify a stroke associated with the [**IInkAnalyzer**](iinkanalyzer.md), this method returns without updating the **IInkAnalyzer**.

This method returns an error code when *plStrokeIds* is **NULL**.

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

[**IInkAnalyzer::AddStroke Method**](iinkanalyzer-addstroke.md)
</dt> <dt>

[**IInkAnalyzer::AddStrokeForLanguage Method**](iinkanalyzer-addstrokeforlanguage.md)
</dt> <dt>

[**IInkAnalyzer::AddStrokeToCustomRecognizer Method**](iinkanalyzer-addstroketocustomrecognizer.md)
</dt> <dt>

[**IInkAnalyzer::AddStrokes Method**](iinkanalyzer-addstrokes.md)
</dt> <dt>

[**IInkAnalyzer::AddStrokesForLanguage Method**](iinkanalyzer-addstrokesforlanguage.md)
</dt> <dt>

[**IInkAnalyzer::AddStrokesToCustomRecognizer Method**](iinkanalyzer-addstrokestocustomrecognizer.md)
</dt> <dt>

[**IInkAnalyzer::ClearStrokeData Method**](iinkanalyzer-clearstrokedata.md)
</dt> <dt>

[**\_IAnalysisEvents::UpdateStrokesCache**](-ianalysisevents-updatestrokescache.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




