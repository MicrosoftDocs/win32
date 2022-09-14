---
description: Represents the possible handwriting recognition word matches for IContextNode objects.
ms.assetid: a497c140-6166-4309-af0f-851af09015c6
title: IAnalysisAlternate interface (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisAlternate
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisAlternate interface

Represents the possible handwriting recognition word matches for [**IContextNode**](icontextnode.md) objects.

## Members

The **IAnalysisAlternate** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IAnalysisAlternate** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAnalysisAlternate** interface has these methods.



| Method                                                                          | Description                                                                                                                                                          |
|:--------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetAlternateNodes**](ianalysisalternate-getalternatenodes.md)               | Retrieves the [**IContextNode**](icontextnode.md) objects that are associated with this alternate.<br/>                                                       |
| [**GetRecognitionConfidence**](ianalysisalternate-getrecognitionconfidence.md) | Retrieves a value that indicates the level of confidence that the [**IInkAnalyzer**](iinkanalyzer.md) has in the accuracy of the **IAnalysisAlternate**.<br/> |
| [**GetRecognizedString**](ianalysisalternate-getrecognizedstring.md)           | Retrieves the recognized string value of the **IAnalysisAlternate** object.<br/>                                                                               |
| [**GetStrokeIds**](ianalysisalternate-getstrokeids.md)                         | Retrieves the stroke identifiers that are associated with this **IAnalysisAlternate**.<br/>                                                                    |



 

## Remarks

There are many variations in users' handwriting. For that reason, handwriting recognizers can sometimes convert handwriting into text that is different from what the user intended. When an [**IInkAnalyzer**](iinkanalyzer.md) performs analysis on a collection of strokes, the **IInkAnalyzer** finds the most likely set of words that the handwriting represents. In addition, the **IInkAnalyzer** also finds sets of alternative recognition matches, which are stored in an [**IAnalysisAlternates**](ianalysisalternates.md) collection. In order for a user to take advantage of recognition alternates, you must create a user interface that allows the user to select the correct **IAnalysisAlternate**.

**IAnalysisAlternate** objects are generally obtained through [**IInkAnalyzer::GetAlternates Method**](iinkanalyzer-getalternates.md). The first **IAnalysisAlternate** object in the collection is what the [**IInkAnalyzer**](iinkanalyzer.md) considers to be the most likely alternate.

This interface is equivalent to [System.Windows.Ink.AnalysisCore.AnalysisAlternateBase](/previous-versions/ms610092(v=vs.100)) in the .NET Framework.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IAnalysisAlternates**](ianalysisalternates.md)
</dt> <dt>

[**IInkAnalyzer::GetAlternatesForContextNodes Method**](iinkanalyzer-getalternatesforcontextnodes.md)
</dt> <dt>

[**IInkAnalyzer::GetAlternatesForStrokes Method**](iinkanalyzer-getalternatesforstrokes.md)
</dt> <dt>

[**IInkAnalyzer::GetAlternates Method**](iinkanalyzer-getalternates.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

