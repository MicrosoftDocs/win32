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
| [**AddOneStroke**](addonestroke.md)                             | Adds a new [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) object to the [**InkDivider**](https://msdn.microsoft.com/en-us/library/ms696382(v=VS.85).aspx) object that was passed in.                                                                 |
| [**CallDivide**](calldivide.md)                                 | Retrieves analysis information from the [**InkDivider**](https://msdn.microsoft.com/en-us/library/ms696382(v=VS.85).aspx) object.                                                                                                              |
| [**CallDivideResults**](calldivideresults.md)                   | Returns analysis results from the [**InkDivider**](https://msdn.microsoft.com/en-us/library/ms696382(v=VS.85).aspx) object.                                                                                                                    |
| [**CallDivideResultsStrokeIds**](calldivideresultsstrokeids.md) | Retrieves the [**Id**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkstrokedisp-get_id) properties for the [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) objects of the coresponding word, line, paragraph, or drawing determined by ink analysis. |
| [**CreateInkDivider**](createinkdivider.md)                     | Instantiates an implementation of the [**InkDivider**](https://msdn.microsoft.com/en-us/library/ms696382(v=VS.85).aspx) interface and returns its handle.                                                                                      |
| [**DeleteInkDivider**](deleteinkdivider.md)                     | Deletes an [**InkDivider**](https://msdn.microsoft.com/en-us/library/ms696382(v=VS.85).aspx) object and releases associated resources.                                                                                                         |
| [**InvokeIDispatch**](invokeidispatch.md)                       | Invokes helper functionality for the IDispatch interface.                                                                                                                                           |
| [**RecognizerContextSet**](recognizercontextset.md)             | Tests whether the [**InkDivider**](https://msdn.microsoft.com/en-us/library/ms696382(v=VS.85).aspx) object can use the [**InkRecognizerContext**](https://msdn.microsoft.com/en-us/library/ms696371(v=VS.85).aspx) class to analyze words.                                      |
| [**RemoveStrokes**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkstrokes-removestrokes)                | Removes [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) objects from the [**InkDivider**](https://msdn.microsoft.com/en-us/library/ms696382(v=VS.85).aspx).                                                                                           |
| [**SetLineHeight**](setlineheight.md)                           | Sets the [**LineHeight**](https://msdn.microsoft.com/en-us/library/ms699524(v=VS.85).aspx) property on the [**InkDivider**](https://msdn.microsoft.com/en-us/library/ms696382(v=VS.85).aspx) object.                                                                                 |
| [**SetLineRecoCallback**](setlinerecocallback.md)               | Sets a callback function to be used during line recognition.                                                                                                                                        |



 

 

 



