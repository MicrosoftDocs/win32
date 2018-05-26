---
Description: The Divider object uses a RecognizerContext to improve its analysis of recognition segments and to generate recognition text for handwriting elements.
ms.assetid: 33d9abc4-151e-47b4-b66f-ff6adfe21222
title: Working with a Recognizer Context
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Working with a Recognizer Context

The [**Divider**](/windows/win32/msinkaut15/?branch=master) object uses a [**RecognizerContext**](/windows/win32/msinkaut/?branch=master) to improve its analysis of recognition segments and to generate recognition text for handwriting elements.

You can set the recognizer context by using the [**RecognizerContext**](/windows/win32/msinkaut15/?branch=master) property of the [**Divider**](/windows/win32/msinkaut15/?branch=master) object or by supplying the recognizer context in the call to the [Divider](frlrfMicrosoftInkDividerClassctorTopic) constructor (in managed code). If a recognizer context for a non-handwriting recognizer or for a recognizer that does not support the free input capability is assigned to the **RecognizerContext** property, then an exception is thrown.

If recognizers are not installed or a recognizer context is not assigned to the [**Divider**](/windows/win32/msinkaut15/?branch=master) object, the **Divider** object does not use a recognizer context. In this case, the layout analysis feature performs the segment division, and no text is associated with the [**DivisionResult**](/windows/win32/msinkaut15/nn-msinkaut15-iinkdivisionresult?branch=master) object.

> [!Note]  
> The [**RecognizerContext**](/windows/win32/msinkaut15/?branch=master) property cannot be changed after strokes have been assigned to the [**Divider**](/windows/win32/msinkaut15/?branch=master) object. The **Divider** object uses the default property values of the [**RecognizerContext**](/windows/win32/msinkaut/?branch=master) object.

 

The [**Divider**](/windows/win32/msinkaut15/?branch=master) object applies the recognizer context to handwritten elements during layout analysis. Any strokes you assign directly to the recognizer context are ignored by the **Divider** object. For more information about text recognition, see [About Handwriting Recognition](about-handwriting-recognition.md).

 

 



