---
description: This section contains information about the interfaces and classes used in ink analysis. The ink analysis classes and interfaces are not Automation-compliant.
ms.assetid: 712908e1-2d1d-4e42-8c80-71354b03d318
title: Ink Analysis Classes and Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Ink Analysis Classes and Interfaces

This section contains information about the interfaces and classes used in ink analysis. The ink analysis classes and interfaces are not Automation-compliant.

## Classes



| Class                                    | Description                                                                     |
|------------------------------------------|---------------------------------------------------------------------------------|
| [**AnalysisRegion**](analysisregion.md) | Implements the [**IAnalysisRegion**](ianalysisregion.md) interface.<br/> |
| [**InkAnalyzer**](inkanalyzer.md)       | Implements the [**IInkAnalyzer**](iinkanalyzer.md) interface.<br/>       |



 

## Interfaces



| Interface                                                    | Description                                                                                                                                                                                                      |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IAnalysisAlternate**](ianalysisalternate.md)             | Represents the possible handwriting recognition word matches for [**IContextNode**](icontextnode.md) objects.<br/>                                                                                        |
| [**IAnalysisAlternates**](ianalysisalternates.md)           | Contains a collection of objects that implement the [**IAnalysisAlternate**](ianalysisalternate.md) interface and that are the result of ink analysis.<br/>                                               |
| [**IAnalysisRegion**](ianalysisregion.md)                   | Exposes methods and properties for a region that represents an area of a document.<br/>                                                                                                                    |
| [**IAnalysisStatus**](ianalysisstatus.md)                   | Represents the status of the ink analysis operation by describing whether the analysis was completed successfully and whether any warnings occurred.<br/>                                                  |
| [**IAnalysisWarning**](ianalysiswarning.md)                 | Represents a warning or error that occurs during an ink analysis operation.<br/>                                                                                                                           |
| [**IAnalysisWarnings**](ianalysiswarnings.md)               | Contains a collection of objects that implement the [**IAnalysisWarning**](ianalysiswarning.md) interface and that are the result of an ink analysis operation.<br/>                                      |
| [**IContextLink**](icontextlink.md)                         | Represents a relationship between two [**IContextNode**](icontextnode.md) objects.<br/>                                                                                                                   |
| [**IContextLinks**](icontextlinks.md)                       | Contains a collection of objects that implement the [**IContextLink**](icontextlink.md) interface.<br/>                                                                                                   |
| [**IContextNode**](icontextnode.md)                         | Represents a node in a tree of objects that are created as part of ink analysis.<br/>                                                                                                                      |
| [**IContextNodes**](icontextnodes.md)                       | Contains a collection of objects that implement the [**IContextNode**](icontextnode.md) interface and that are the result of an ink analysis operation.<br/>                                              |
| [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md)     | Provides access to handwriting recognizers for use with ink analysis.<br/>                                                                                                                                 |
| [**IInkAnalysisRecognizers**](iinkanalysisrecognizers.md)   | Contains a collection of objects that implement the [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) interface and that represent the ability to recognize handwriting, objects, or gestures.<br/> |
| [**IInkAnalyzer**](iinkanalyzer.md)                         | Provides access to layout analysis, writing and drawing classification, and handwriting recognition.<br/>                                                                                                  |
| [**IMatchesCriteriaCallBack**](imatchescriteriacallback.md) | Exposes a method to evaluate whether an [**IContextNode**](icontextnode.md) object meets or fails a specified criteria.<br/>                                                                              |



 

## Return Values

Methods in the Tablet PC COM Library return values of **HRESULT**. Unless otherwise noted, the meanings of the **HRESULT** values are described in this table.



| HRESULT value                                   | Description                                                                              |
|-------------------------------------------------|------------------------------------------------------------------------------------------|
| S\_OK<br/>                                | Success.<br/>                                                                      |
| E\_POINTER<br/>                           | At least one pointer (for either an input or an output parameter) is invalid.<br/> |
| E\_INVALIDARG<br/>                        | Member attempted to pass in an invalid argument.<br/>                              |
| E\_INK\_EXCEPTION<br/>                    | Exception occurred.<br/>                                                           |
| E\_OUTOFMEMORY<br/>                       | System cannot allocate memory to complete the operation.<br/>                      |
| E\_FAIL<br/>                              | Unspecified failure occurred.<br/>                                                 |
| E\_INVALIDOPERATION<br/>                  | Member attempted to use an invalid operation.<br/>                                 |
| TPC\_E\_INVALID\_MODE<br/>                | Member attempted to use an invalid mode.<br/>                                      |
| TPC\_E\_INVALID\_CONFIGURATION<br/>       | Member attempted to use an invalid configuration.<br/>                             |
| TPC\_E\_INVALID\_PACKET\_DESCRIPTION<br/> | Member attempted to use an invalid packet description.<br/>                        |



 

## Related topics

<dl> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




