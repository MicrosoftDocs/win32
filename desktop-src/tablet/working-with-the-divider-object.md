---
description: The Divider object provides access to the Tablet PC layout analysis features.
ms.assetid: 9fa299fe-3713-4fa8-95c6-be15f144103a
title: Working with the Divider Object
ms.topic: article
ms.date: 05/31/2018
---

# Working with the Divider Object

The [Divider](/previous-versions/ms583616(v=vs.100)) object provides access to the Tablet PC layout analysis features.

In managed code, the [Divider](/previous-versions/ms583616(v=vs.100)) object can be instantiated by calling one of the [Divider](/previous-versions/ms839465(v=msdn.10)) constructors. In Automation, this is called the [**InkDivider**](inkdivider-class.md) object, and it can be instantiated by calling the [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) method in C++.

You can obtain a snapshot of the current analysis result by calling the [Divide](/previous-versions/ms839461(v=msdn.10)) method of the [Divider](/previous-versions/ms583616(v=vs.100)) object. The analysis result is returned in a [DivisionResult](/previous-versions/ms839371(v=msdn.10)) object. Each time you call the Divide method, the Divider object creates a DivisionResult object. For more information about the DivisionResult object, see [Working with the DivisionResult Object](working-with-the-divisionresult-object.md).

The [Strokes](/previous-versions/ms552701(v=vs.100)) collection that the [Divider](/previous-versions/ms583616(v=vs.100)) object analyzes is contained in the [Strokes](/previous-versions/ms839422(v=msdn.10)) property of the Divider object. The Divider object dynamically analyzes the Strokes collection as you add to or delete from the collection. For more information about the Strokes property of the Divider object, see [Working with a Strokes Collection](working-with-a-strokes-collection.md).

The [Divider](/previous-versions/ms583616(v=vs.100)) object uses a recognizer context to improve its analysis of recognition segments and to generate recognition text for handwriting elements. You can set the recognizer context by using the [RecognizerContext](/previous-versions/ms839415(v=msdn.10)) property of the Divider object. The RecognizerContext property cannot be changed after strokes have been assigned to the Divider object. For more information about the RecognizerContext property of the Divider object, see [Working with a Recognizer Context](working-with-a-recognizer-context.md).

> [!Caution]  
> In managed code, you must call the [Dispose](/previous-versions/ms839450(v=msdn.10)) method on this object before it goes out of scope. This object maintains non-managed resources. Relying on finalization for this object can cause memory leaks and exceptions within your application.

 

 

 
