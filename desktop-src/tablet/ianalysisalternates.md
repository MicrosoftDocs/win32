---
description: Contains a collection of objects that implement the IAnalysisAlternate interface and that are the result of ink analysis.
ms.assetid: 53802a62-4425-40fd-bf48-0da55ea8ffbe
title: IAnalysisAlternates interface (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisAlternates
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisAlternates interface

Contains a collection of objects that implement the [**IAnalysisAlternate**](ianalysisalternate.md) interface and that are the result of ink analysis.

## Members

The **IAnalysisAlternates** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IAnalysisAlternates** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAnalysisAlternates** interface has these methods.



| Method                                                                   | Description                                                                                                                                      |
|:-------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetAnalysisAlternate**](ianalysisalternates-getanalysisalternate.md) | Retrieves the [**IAnalysisAlternate**](ianalysisalternate.md) object at the specified index within the collection.<br/>                   |
| [**GetCount**](ianalysisalternates-getcount.md)                         | Retrieves the number of [**IAnalysisAlternate**](ianalysisalternate.md) objects contained in the **IAnalysisAlternates** collection.<br/> |



 

## Remarks

This interface is equivalent to the [**System.Windows.Ink.AnalysisCore.AnalysisAlternateBaseCollection**](/previous-versions/ms610094(v=vs.100)) class in the .NET Framework.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IAnalysisAlternate**](ianalysisalternate.md)
</dt> <dt>

[**IInkAnalyzer::GetAlternates Method**](iinkanalyzer-getalternates.md)
</dt> <dt>

[**IInkAnalyzer::GetAlternatesForContextNodes Method**](iinkanalyzer-getalternatesforcontextnodes.md)
</dt> <dt>

[**IInkAnalyzer::GetAlternatesForStrokes Method**](iinkanalyzer-getalternatesforstrokes.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

