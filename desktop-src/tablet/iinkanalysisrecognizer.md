---
description: Provides access to handwriting recognizers for use with ink analysis.
ms.assetid: de536cca-889e-413e-a6f7-c2229a77c801
title: IInkAnalysisRecognizer interface (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalysisRecognizer
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalysisRecognizer interface

Provides access to handwriting recognizers for use with ink analysis.

## Members

The **IInkAnalysisRecognizer** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IInkAnalysisRecognizer** also has these types of members:

-   [Methods](#methods)

### Methods

The **IInkAnalysisRecognizer** interface has these methods.



| Method                                                                          | Description                                                                                                                    |
|:--------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| [**GetCapabilities**](iinkanalysisrecognizer-getcapabilities.md)               | Retrieves the capabilities of the recognizer.<br/>                                                                       |
| [**GetGuid**](iinkanalysisrecognizer-getguid.md)                               | Retrieves the globally unique identifier (GUID) of the recognizer.<br/>                                                  |
| [**GetLanguages**](iinkanalysisrecognizer-getlanguages.md)                     | Retrieves the identifiers for the locales that this **IInkAnalysisRecognizer** supports.<br/>                            |
| [**GetName**](iinkanalysisrecognizer-getname.md)                               | Retrieves the name of the recognizer.<br/>                                                                               |
| [**GetSupportedProperties**](iinkanalysisrecognizer-getsupportedproperties.md) | Retrieves the globally unique identifiers (GUIDs) for the properties that this **IInkAnalysisRecognizer** supports.<br/> |
| [**GetVendor**](iinkanalysisrecognizer-getvendor.md)                           | Retrieves the vendor name of the **IInkAnalysisRecognizer**.<br/>                                                        |



 

## Remarks

A recognizer has specific attributes and properties that allow it to perform recognition. The properties of a recognizer must be determined before recognition can occur. The types of properties that a recognizer supports determine the types of recognition that it can perform. For instance, if a recognizer does not support cursive handwriting, it returns inaccurate results when a user writes in cursive.

A recognizer also has built-in functionality that automatically manages many aspects of handwriting. For instance, it determines the metrics for the lines on which strokes are drawn. You can return the line number of a stroke, but you never need to specify how those line metrics are determined because of the built-in functionality of the recognizer.

The [**IInkAnalyzer**](iinkanalyzer.md) maintains a list of available recognizers. To access this list, use the [**IInkAnalyzer::GetInkAnalysisRecognizersByPriority Method**](iinkanalyzer-getinkanalysisrecognizersbypriority.md) method.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IInkAnalysisRecognizers**](iinkanalysisrecognizers.md)
</dt> <dt>

[**IInkAnalyzer**](iinkanalyzer.md)
</dt> <dt>

[**IInkAnalyzer::CreateCustomRecognizer Method**](iinkanalyzer-createcustomrecognizer.md)
</dt> <dt>

[Context Node Types](context-node-types.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

