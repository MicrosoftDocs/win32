---
description: This section contains the core functions for Tablet PC.
ms.assetid: 8f94a82c-de93-4649-a9b5-0adcbe01333d
title: Core Tablet PC Functions
ms.topic: article
ms.date: 05/31/2018
---

# Core Tablet PC Functions

This section contains the core functions for Tablet PC.

## In This Section



| Function                                                         | Description                                                                                                                                                                                         |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddOneStroke**](addonestroke.md)                             | Adds a new [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) object to the [**InkDivider**](inkdivider-class.md) object that was passed in.                                                                 |
| [**CallDivide**](calldivide.md)                                 | Retrieves analysis information from the [**InkDivider**](inkdivider-class.md) object.                                                                                                              |
| [**CallDivideResults**](calldivideresults.md)                   | Returns analysis results from the [**InkDivider**](inkdivider-class.md) object.                                                                                                                    |
| [**CallDivideResultsStrokeIds**](calldivideresultsstrokeids.md) | Retrieves the [**Id**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkstrokedisp-get_id) properties for the [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) objects of the corresponding word, line, paragraph, or drawing determined by ink analysis. |
| [**CreateInkDivider**](createinkdivider.md)                     | Instantiates an implementation of the [**InkDivider**](inkdivider-class.md) interface and returns its handle.                                                                                      |
| [**DeleteInkDivider**](deleteinkdivider.md)                     | Deletes an [**InkDivider**](inkdivider-class.md) object and releases associated resources.                                                                                                         |
| [**InvokeIDispatch**](invokeidispatch.md)                       | Invokes helper functionality for the IDispatch interface.                                                                                                                                           |
| [**RecognizerContextSet**](recognizercontextset.md)             | Tests whether the [**InkDivider**](inkdivider-class.md) object can use the [**InkRecognizerContext**](inkrecognizercontext-class.md) class to analyze words.                                      |
| [**RemoveStrokes**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkstrokes-removestrokes)                | Removes [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) objects from the [**InkDivider**](inkdivider-class.md).                                                                                           |
| [**SetLineHeight**](setlineheight.md)                           | Sets the [**LineHeight**](/windows/win32/api/msinkaut15/nf-msinkaut15-iinkdivider-get_lineheight) property on the [**InkDivider**](inkdivider-class.md) object.                                                                                 |
| [**SetLineRecoCallback**](setlinerecocallback.md)               | Sets a callback function to be used during line recognition.                                                                                                                                        |



 

 

 
