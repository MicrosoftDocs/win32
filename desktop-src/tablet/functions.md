---
Description: This section contains the core functions for Tablet PC.
ms.assetid: 8f94a82c-de93-4649-a9b5-0adcbe01333d
title: Core Tablet PC Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Core Tablet PC Functions

This section contains the core functions for Tablet PC.

## In This Section



| Function                                                         | Description                                                                                                                                                                                         |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddOneStroke**](addonestroke.md)                             | Adds a new [**IInkStrokeDisp**](/windows/win32/msinkaut/nn-msinkaut-iinkstrokedisp?branch=master) object to the [**InkDivider**](/windows/win32/msinkaut15/?branch=master) object that was passed in.                                                                 |
| [**CallDivide**](calldivide.md)                                 | Retrieves analysis information from the [**InkDivider**](/windows/win32/msinkaut15/?branch=master) object.                                                                                                              |
| [**CallDivideResults**](calldivideresults.md)                   | Returns analysis results from the [**InkDivider**](/windows/win32/msinkaut15/?branch=master) object.                                                                                                                    |
| [**CallDivideResultsStrokeIds**](calldivideresultsstrokeids.md) | Retrieves the [**Id**](/windows/win32/msinkaut/nf-msinkaut-iinkstrokedisp-get_id?branch=master) properties for the [**IInkStrokeDisp**](/windows/win32/msinkaut/nn-msinkaut-iinkstrokedisp?branch=master) objects of the coresponding word, line, paragraph, or drawing determined by ink analysis. |
| [**CreateInkDivider**](createinkdivider.md)                     | Instantiates an implementation of the [**InkDivider**](/windows/win32/msinkaut15/?branch=master) interface and returns its handle.                                                                                      |
| [**DeleteInkDivider**](deleteinkdivider.md)                     | Deletes an [**InkDivider**](/windows/win32/msinkaut15/?branch=master) object and releases associated resources.                                                                                                         |
| [**InvokeIDispatch**](invokeidispatch.md)                       | Invokes helper functionality for the IDispatch interface.                                                                                                                                           |
| [**RecognizerContextSet**](recognizercontextset.md)             | Tests whether the [**InkDivider**](/windows/win32/msinkaut15/?branch=master) object can use the [**InkRecognizerContext**](/windows/win32/msinkaut/?branch=master) class to analyze words.                                      |
| [**RemoveStrokes**](/windows/win32/msinkaut/?branch=master)                | Removes [**IInkStrokeDisp**](/windows/win32/msinkaut/nn-msinkaut-iinkstrokedisp?branch=master) objects from the [**InkDivider**](/windows/win32/msinkaut15/?branch=master).                                                                                           |
| [**SetLineHeight**](setlineheight.md)                           | Sets the [**LineHeight**](/windows/win32/msinkaut15/?branch=master) property on the [**InkDivider**](/windows/win32/msinkaut15/?branch=master) object.                                                                                 |
| [**SetLineRecoCallback**](setlinerecocallback.md)               | Sets a callback function to be used during line recognition.                                                                                                                                        |



 

 

 



