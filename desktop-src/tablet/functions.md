---
Description: This section contains the core functions for Tablet PC.
ms.assetid: 8f94a82c-de93-4649-a9b5-0adcbe01333d
title: Core Tablet PC Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Core Tablet PC Functions

This section contains the core functions for Tablet PC.

## In This Section



| Function                                                         | Description                                                                                                                                                                                         |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddOneStroke**](addonestroke.md)                             | Adds a new [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) object to the [**InkDivider**](/windows/desktop/api/msinkaut15/) object that was passed in.                                                                 |
| [**CallDivide**](calldivide.md)                                 | Retrieves analysis information from the [**InkDivider**](/windows/desktop/api/msinkaut15/) object.                                                                                                              |
| [**CallDivideResults**](calldivideresults.md)                   | Returns analysis results from the [**InkDivider**](/windows/desktop/api/msinkaut15/) object.                                                                                                                    |
| [**CallDivideResultsStrokeIds**](calldivideresultsstrokeids.md) | Retrieves the [**Id**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkstrokedisp-get_id) properties for the [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) objects of the coresponding word, line, paragraph, or drawing determined by ink analysis. |
| [**CreateInkDivider**](createinkdivider.md)                     | Instantiates an implementation of the [**InkDivider**](/windows/desktop/api/msinkaut15/) interface and returns its handle.                                                                                      |
| [**DeleteInkDivider**](deleteinkdivider.md)                     | Deletes an [**InkDivider**](/windows/desktop/api/msinkaut15/) object and releases associated resources.                                                                                                         |
| [**InvokeIDispatch**](invokeidispatch.md)                       | Invokes helper functionality for the IDispatch interface.                                                                                                                                           |
| [**RecognizerContextSet**](recognizercontextset.md)             | Tests whether the [**InkDivider**](/windows/desktop/api/msinkaut15/) object can use the [**InkRecognizerContext**](/windows/desktop/api/msinkaut/) class to analyze words.                                      |
| [**RemoveStrokes**](/windows/desktop/api/msinkaut/)                | Removes [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) objects from the [**InkDivider**](/windows/desktop/api/msinkaut15/).                                                                                           |
| [**SetLineHeight**](setlineheight.md)                           | Sets the [**LineHeight**](/windows/desktop/api/msinkaut15/) property on the [**InkDivider**](/windows/desktop/api/msinkaut15/) object.                                                                                 |
| [**SetLineRecoCallback**](setlinerecocallback.md)               | Sets a callback function to be used during line recognition.                                                                                                                                        |



 

 

 



