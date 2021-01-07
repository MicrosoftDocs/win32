---
description: Provides access to layout analysis, writing and drawing classification, and handwriting recognition.
ms.assetid: 3a19db78-df14-43c2-9e3e-8cf674aa7b9c
title: IInkAnalyzer interface (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer interface

Provides access to layout analysis, writing and drawing classification, and handwriting recognition.

## Members

The **IInkAnalyzer** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IInkAnalyzer** also has these types of members:

-   [Methods](#methods)

### Methods

The **IInkAnalyzer** interface has these methods.



| Method                                                                                                  | Description                                                                                                                                                                                  |
|:--------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Abort**](iinkanalyzer-abort.md)                                                                     | Cancels the current analysis operation.<br/>                                                                                                                                           |
| [**AddStroke**](iinkanalyzer-addstroke.md)                                                             | Adds stroke data for a single stroke to the **IInkAnalyzer** and assigns the active input thread's culture identifier to the stroke.<br/>                                              |
| [**AddStrokeForLanguage**](iinkanalyzer-addstrokeforlanguage.md)                                       | Adds stroke data for a single stroke to the **IInkAnalyzer** and assigns a specific culture identifier to the stroke.<br/>                                                             |
| [**AddStrokes**](iinkanalyzer-addstrokes.md)                                                           | Adds stroke data for multiple strokes to the **IInkAnalyzer** and assigns the active input thread's culture identifier to the strokes.<br/>                                            |
| [**AddStrokesForLanguage**](iinkanalyzer-addstrokesforlanguage.md)                                     | Adds stroke data for multiple strokes to the **IInkAnalyzer** and assigns the specified culture identifier to the strokes.<br/>                                                        |
| [**AddStrokesToCustomRecognizer**](iinkanalyzer-addstrokestocustomrecognizer.md)                       | Adds stroke data for multiple strokes to a custom recognizer node.<br/>                                                                                                                |
| [**AddStrokeToCustomRecognizer**](iinkanalyzer-addstroketocustomrecognizer.md)                         | Adds stroke data for a single stroke to a custom recognizer node.<br/>                                                                                                                 |
| [**Analyze**](iinkanalyzer-analyze.md)                                                                 | Performs synchronous ink analysis.<br/>                                                                                                                                                |
| [**BackgroundAnalyze**](iinkanalyzer-backgroundanalyze.md)                                             | Performs asynchronous ink analysis.<br/>                                                                                                                                               |
| [**ClearStrokeData**](iinkanalyzer-clearstrokedata.md)                                                 | Clears stroke packet data from the **IInkAnalyzer**.<br/>                                                                                                                              |
| [**CreateAnalysisHint**](iinkanalyzer-createanalysishint.md)                                           | Adds a new analysis hint node with an infinite area to the **IInkAnalyzer**.<br/>                                                                                                      |
| [**CreateContextNodes**](iinkanalyzer-createcontextnodes.md)                                           | Creates an [**IContextNodes**](icontextnodes.md) object.<br/>                                                                                                                         |
| [**CreateCustomRecognizer**](iinkanalyzer-createcustomrecognizer.md)                                   | Creates a new custom recognizer node for the **IInkAnalyzer**.<br/>                                                                                                                    |
| [**DeleteAnalysisHint**](iinkanalyzer-deleteanalysishint.md)                                           | Removes an analysis hint from the **IInkAnalyzer**.<br/>                                                                                                                               |
| [**FindInkLeafNodes**](iinkanalyzer-findinkleafnodes.md)                                               | Retrieves all of the ink leaf nodes.<br/>                                                                                                                                              |
| [**FindInkLeafNodesForStrokes**](iinkanalyzer-findinkleafnodesforstrokes.md)                           | Retrieves the ink leaf nodes that contain the specified strokes.<br/>                                                                                                                  |
| [**FindLeafNodes**](iinkanalyzer-findleafnodes.md)                                                     | Retrieves all of the leaf nodes.<br/>                                                                                                                                                  |
| [**FindNode**](iinkanalyzer-findnode.md)                                                               | Retrieves the [**IContextNode**](icontextnode.md) object for a specified globally unique identifier (GUID).<br/>                                                                      |
| [**FindNodesOfType**](iinkanalyzer-findnodesoftype.md)                                                 | Retrieves all of the [**IContextNode**](icontextnode.md) objects of the specified type.<br/>                                                                                          |
| [**FindNodesOfTypeForStrokes**](iinkanalyzer-findnodesoftypeforstrokes.md)                             | Retrieves all of the [**IContextNode**](icontextnode.md) objects of the specified type that contain the specified strokes.<br/>                                                       |
| [**FindNodesOfTypeInSubTree**](iinkanalyzer-findnodesoftypeinsubtree.md)                               | Retrieves all of the [**IContextNode**](icontextnode.md) objects of the specified type that are descendants of the specified **IContextNode** object.<br/>                            |
| [**FindNodesWithCallBack**](iinkanalyzer-findnodeswithcallback.md)                                     | Retrieves all of the [**IContextNode**](icontextnode.md) objects that match the specified criteria.<br/>                                                                              |
| [**FindNodesWithCallBackInSubTree**](iinkanalyzer-findnodeswithcallbackinsubtree.md)                   | Retrieves all of the [**IContextNode**](icontextnode.md) objects that match the specified criteria and are descendants of the specified **IContextNode** object.<br/>                 |
| [**GetAlternates**](iinkanalyzer-getalternates.md)                                                     | Retrieves 10 analysis alternates for all ink associated with the **IInkAnalyzer**.<br/>                                                                                                |
| [**GetAlternatesForContextNodes**](iinkanalyzer-getalternatesforcontextnodes.md)                       | Retrieves analysis alternates for the nodes in a specified [**IContextNodes**](icontextnodes.md) collection.<br/>                                                                     |
| [**GetAlternatesForStrokes**](iinkanalyzer-getalternatesforstrokes.md)                                 | Retrieves analysis alternates for the strokes with the specified stroke identifiers.<br/>                                                                                              |
| [**GetAnalysisHints**](iinkanalyzer-getanalysishints.md)                                               | Retrieves all of the analysis hint [**IContextNode**](icontextnode.md) objects that are attached to the **IInkAnalyzer**.<br/>                                                        |
| [**GetAnalysisHintsByName**](iinkanalyzer-getanalysishintsbyname.md)                                   | Retrieves all of the analysis hint [**IContextNode**](icontextnode.md) objects that are attached to the **IInkAnalyzer** and that have the specified name.<br/>                       |
| [**GetAnalysisModes**](iinkanalyzer-getanalysismodes.md)                                               | Retrieves flags that control how the **IInkAnalyzer** performs ink analysis.<br/>                                                                                                      |
| [**GetDirtyRegion**](iinkanalyzer-getdirtyregion.md)                                                   | Retrieves the area that has changed since the last analysis operation.<br/>                                                                                                            |
| [**GetInkAnalysisRecognizersByPriority**](iinkanalyzer-getinkanalysisrecognizersbypriority.md)         | Retrieves an ordered collection of [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) objects.<br/>                                                                              |
| [**GetNodesFromTextRange**](iinkanalyzer-getnodesfromtextrange.md)                                     | Retrieves a collection of [**IContextNode**](icontextnode.md) objects that are relevant to the specified text range for the specified context nodes.<br/>                             |
| [**GetRecognizedString**](iinkanalyzer-getrecognizedstring.md)                                         | Retrieves the best-result string of the recognition operation for the entire context node tree in the **IInkAnalyzer**.<br/>                                                           |
| [**GetRootNode**](iinkanalyzer-getrootnode.md)                                                         | Retrieves the root [**IContextNode**](icontextnode.md) of the **IInkAnalyzer** object's context tree.<br/>                                                                            |
| [**GetStrokeLanguageId**](iinkanalyzer-getstrokelanguageid.md)                                         | Retrieves the locale identifier of the specified stroke.<br/>                                                                                                                          |
| [**GetStrokeType**](iinkanalyzer-getstroketype.md)                                                     | Retrieves the type of the specified stroke.<br/>                                                                                                                                       |
| [**GetTextRangeFromNodes**](iinkanalyzer-gettextrangefromnodes.md)                                     | Finds the text range in the recognized string that corresponds to a collection of [**IContextNode**](icontextnode.md) objects.<br/>                                                   |
| [**IsAnalyzing**](iinkanalyzer-isanalyzing.md)                                                         | Retrieves a value indicating whether the **IInkAnalyzer** is performing ink analysis.<br/>                                                                                             |
| [**LoadResults**](iinkanalyzer-loadresults.md)                                                         | Loads saved analysis results into the **IInkAnalyzer**.<br/>                                                                                                                           |
| [**ModifyTopAlternate**](iinkanalyzer-modifytopalternate.md)                                           | Changes the current top alternate to the specified alternate and clears the confirmation type for all [**IContextNode**](icontextnode.md) objects associated with the alternate.<br/> |
| [**ModifyTopAlternateWithConfirmation**](iinkanalyzer-modifytopalternatewithconfirmation.md)           | Changes the current top alternate to the specified [**IAnalysisAlternate**](ianalysisalternate.md).<br/>                                                                              |
| [**Reconcile**](iinkanalyzer-reconcile.md)                                                             | Determines which portions of the analysis results have changed during background ink analysis.<br/>                                                                                    |
| [**RemoveStroke**](iinkanalyzer-removestroke.md)                                                       | Removes the specified stroke from the **IInkAnalyzer**.<br/>                                                                                                                           |
| [**RemoveStrokes**](iinkanalyzer-removestrokes.md)                                                     | Removes the specified strokes from the **IInkAnalyzer**.<br/>                                                                                                                          |
| [**SaveResults**](iinkanalyzer-saveresults.md)                                                         | Saves all analysis results for an **IInkAnalyzer**.<br/>                                                                                                                               |
| [**SaveResultsForNodes**](iinkanalyzer-saveresultsfornodes.md)                                         | Saves analysis results for a specific context node collection associated with an **IInkAnalyzer**.<br/>                                                                                |
| [**SaveResultsForStrokes**](iinkanalyzer-saveresultsforstrokes.md)                                     | Saves analysis results for the specified strokes associated with an **IInkAnalyzer**.<br/>                                                                                             |
| [**Search**](iinkanalyzer-search.md)                                                                   | Provides a fuzzy, case-insensitive phrase based search for analyzed writing strokes and analyzed drawing strokes that have recognized types.<br/>                                      |
| [**SearchWithLanguageId**](iinkanalyzer-searchwithlanguageid.md)                                       | Provides a fuzzy, case-insensitive phrase based search for analyzed writing strokes and analyzed drawing strokes that have recognized types.<br/>                                      |
| [**SetAnalysisModes**](iinkanalyzer-setanalysismodes.md)                                               | Modifies flags that control how the **IInkAnalyzer** performs ink analysis.<br/>                                                                                                       |
| [**SetDirtyRegion**](iinkanalyzer-setdirtyregion.md)                                                   | Modifies the area that has changed since the last analysis operation.<br/>                                                                                                             |
| [**SetHighestPriorityInkAnalysisRecognizer**](iinkanalyzer-sethighestpriorityinkanalysisrecognizer.md) | Moves the specified [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) to the first position in the **IInkAnalyzer** object's list of ink recognizers.<br/>                      |
| [**SetStrokeLanguageId**](iinkanalyzer-setstrokelanguageid.md)                                         | Changes the locale identifier for the specified stroke.<br/>                                                                                                                           |
| [**SetStrokesLanguageId**](iinkanalyzer-setstrokeslanguageid.md)                                       | Changes the locale identifier for the specified strokes.<br/>                                                                                                                          |
| [**SetStrokesType**](iinkanalyzer-setstrokestype.md)                                                   | Changes the type of the specified strokes.<br/>                                                                                                                                        |
| [**SetStrokeType**](iinkanalyzer-setstroketype.md)                                                     | Changes the type of the specified stroke.<br/>                                                                                                                                         |
| [**UpdateStrokesData**](iinkanalyzer-updatestrokesdata.md)                                             | Updates the packet data for the specified strokes.<br/>                                                                                                                                |



 

## Remarks

**IInkAnalyzer** uses stroke packet data to analyze ink and does not interact with [**InkDisp Class**](inkdisp-class.md) or [InkStrokes Collection](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) objects directly.

To add or remove strokes to the **IInkAnalyzer** for analysis, use one of the following methods.

-   [**IInkAnalyzer::AddStroke Method**](iinkanalyzer-addstroke.md)
-   [**IInkAnalyzer::AddStrokes Method**](iinkanalyzer-addstrokes.md)
-   [**IInkAnalyzer::RemoveStroke Method**](iinkanalyzer-removestroke.md)
-   [**IInkAnalyzer::RemoveStrokes Method**](iinkanalyzer-removestrokes.md)

These methods update the dirty region (see [**IInkAnalyzer::GetDirtyRegion Method**](iinkanalyzer-getdirtyregion.md)), which is the region for which strokes are analyzed in the next analysis operation.

To analyze ink, use the [**IInkAnalyzer::Analyze Method**](iinkanalyzer-analyze.md) or [**IInkAnalyzer::BackgroundAnalyze Method**](iinkanalyzer-backgroundanalyze.md) method. During analysis, the **IInkAnalyzer** performs layout analysis, stroke classification, and handwriting recognition.

To change the layout analysis and stroke classification settings, use the [**IInkAnalyzer::SetAnalysisModes Method**](iinkanalyzer-setanalysismodes.md) property.

During analysis, the **IInkAnalyzer** receives a number of events, including events generated during background analysis. [**\_IAnalysisProxyEvents**](-ianalysisproxyevents.md) supports the data proxy features of the **IInkAnalyzer**. For more information, see [Data Proxy with Ink Analysis](data-proxy-with-ink-analysis.md). To stop the analysis process from within an event handler, call [**IInkAnalyzer::Abort Method**](iinkanalyzer-abort.md).

To modify the language the ink analyzer uses to recognize handwriting, use [**IInkAnalyzer::SetStrokeLanguageId Method**](iinkanalyzer-setstrokelanguageid.md) or [**IInkAnalyzer::SetStrokesLanguageId Method**](iinkanalyzer-setstrokeslanguageid.md). To modify how the ink analyzer classifies specific strokes, use [**IInkAnalyzer::SetStrokeType Method**](iinkanalyzer-setstroketype.md) or [**IInkAnalyzer::SetStrokesType Method**](iinkanalyzer-setstrokestype.md).

The **IInkAnalyzer** loads information for all of the installed ink recognizers. [**IInkAnalyzer::GetInkAnalysisRecognizersByPriority Method**](iinkanalyzer-getinkanalysisrecognizersbypriority.md) returns an [**IInkAnalysisRecognizers**](iinkanalysisrecognizers.md) collection containing each available [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md). If more than one ink recognizer supports a specific language, use [**IInkAnalyzer::SetHighestPriorityInkAnalysisRecognizer Method**](iinkanalyzer-sethighestpriorityinkanalysisrecognizer.md) to set which ink recognizer handles strokes for that language.

Using analysis hints can improve the recognition accuracy by providing extra context to the ink analyzer. The additional context information can help the ink analyzer limit the number of possible recognition results. For example, you can narrow the scope by defining factoids and expected words or by structuring your input into a recognition guide. For more information about providing context to the ink analyzer, see:

-   [**IInkAnalyzer::CreateAnalysisHint Method**](iinkanalyzer-createanalysishint.md)
-   [**IInkAnalyzer::DeleteAnalysisHint Method**](iinkanalyzer-deleteanalysishint.md)
-   [**IInkAnalyzer::GetAnalysisHints Method**](iinkanalyzer-getanalysishints.md)
-   [**IInkAnalyzer::GetAnalysisHintsByName Method**](iinkanalyzer-getanalysishintsbyname.md)

The ink analyzer represents analysis results as a string or as a tree of [**IContextNode**](icontextnode.md) objects. To access the recognized string, use [**IInkAnalyzer::GetRecognizedString Method**](iinkanalyzer-getrecognizedstring.md). To access the root of the context node tree, use [**IInkAnalyzer::GetRootNode Method**](iinkanalyzer-getrootnode.md). The ink analyzer has the following methods for finding specific context nodes or text.

-   [**IInkAnalyzer::FindInkLeafNodes Method**](iinkanalyzer-findinkleafnodes.md)
-   [**IInkAnalyzer::FindInkLeafNodesForStrokes Method**](iinkanalyzer-findinkleafnodesforstrokes.md)
-   [**IInkAnalyzer::FindLeafNodes Method**](iinkanalyzer-findleafnodes.md)
-   [**IInkAnalyzer::FindNode Method**](iinkanalyzer-findnode.md)
-   [**IInkAnalyzer::FindNodesOfType Method**](iinkanalyzer-findnodesoftype.md)
-   [**IInkAnalyzer::FindNodesOfTypeForStrokes Method**](iinkanalyzer-findnodesoftypeforstrokes.md)
-   [**IInkAnalyzer::FindNodesOfTypeInSubTree Method**](iinkanalyzer-findnodesoftypeinsubtree.md)
-   [**IInkAnalyzer::FindNodesWithCallBack Method**](iinkanalyzer-findnodeswithcallback.md)
-   [**IInkAnalyzer::FindNodesWithCallBackInSubTree Method**](iinkanalyzer-findnodeswithcallbackinsubtree.md)

To work with alternate analysis results, use one of the following methods.

-   [**IInkAnalyzer::GetAlternates Method**](iinkanalyzer-getalternates.md)
-   [**IInkAnalyzer::GetAlternatesForContextNodes Method**](iinkanalyzer-getalternatesforcontextnodes.md)
-   [**IInkAnalyzer::GetAlternatesForStrokes Method**](iinkanalyzer-getalternatesforstrokes.md)
-   [**IInkAnalyzer::ModifyTopAlternate Method**](iinkanalyzer-modifytopalternate.md)
-   [**IInkAnalyzer::ModifyTopAlternateWithConfirmation Method**](iinkanalyzer-modifytopalternatewithconfirmation.md)

To save analysis results, use one of the following methods.

-   [**IInkAnalyzer::SaveResults Method**](iinkanalyzer-saveresults.md)
-   [**IInkAnalyzer::SaveResultsForNodes Method**](iinkanalyzer-saveresultsfornodes.md)
-   [**IInkAnalyzer::SaveResultsForStrokes Method**](iinkanalyzer-saveresultsforstrokes.md)

To load saved results, use [**IInkAnalyzer::LoadResults Method**](iinkanalyzer-loadresults.md).

For more information about using the **IInkAnalyzer** to analyze ink, see [Ink Analysis Overview](ink-analysis-overview.md).

## Requirements



| Requirement | Value |
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

 

