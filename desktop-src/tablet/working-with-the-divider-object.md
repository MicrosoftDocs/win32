---
Description: The Divider object provides access to the Tablet PC layout analysis features.
ms.assetid: 9fa299fe-3713-4fa8-95c6-be15f144103a
title: Working with the Divider Object
ms.topic: article
ms.date: 05/31/2018
---

# Working with the Divider Object

The [Divider](https://msdn.microsoft.com/library/ms583616(v=VS.100).aspx) object provides access to the Tablet PC layout analysis features.

In managed code, the [Divider](https://msdn.microsoft.com/library/ms583616(v=VS.100).aspx) object can be instantiated by calling one of the [Divider](https://msdn.microsoft.com/library/ms839465(v=MSDN.10).aspx) constructors. In Automation, this is called the [**InkDivider**](inkdivider-class.md) object, and it can be instantiated by calling the [**CoCreateInstance**](https://msdn.microsoft.com/en-us/library/ms686615(v=VS.85).aspx) method in C++.

You can obtain a snapshot of the current analysis result by calling the [Divide](https://msdn.microsoft.com/library/ms839461(v=MSDN.10).aspx) method of the [Divider](https://msdn.microsoft.com/library/ms583616(v=VS.100).aspx) object. The analysis result is returned in a [DivisionResult](https://msdn.microsoft.com/library/ms839371(v=MSDN.10).aspx) object. Each time you call the Divide method, the Divider object creates a DivisionResult object. For more information about the DivisionResult object, see [Working with the DivisionResult Object](working-with-the-divisionresult-object.md).

The [Strokes](https://msdn.microsoft.com/library/ms552701(v=VS.100).aspx) collection that the [Divider](https://msdn.microsoft.com/library/ms583616(v=VS.100).aspx) object analyzes is contained in the [Strokes](https://msdn.microsoft.com/library/ms839422(v=MSDN.10).aspx) property of the Divider object. The Divider object dynamically analyzes the Strokes collection as you add to or delete from the collection. For more information about the Strokes property of the Divider object, see [Working with a Strokes Collection](working-with-a-strokes-collection.md).

The [Divider](https://msdn.microsoft.com/library/ms583616(v=VS.100).aspx) object uses a recognizer context to improve its analysis of recognition segments and to generate recognition text for handwriting elements. You can set the recognizer context by using the [RecognizerContext](https://msdn.microsoft.com/library/ms839415(v=MSDN.10).aspx) property of the Divider object. The RecognizerContext property cannot be changed after strokes have been assigned to the Divider object. For more information about the RecognizerContext property of the Divider object, see [Working with a Recognizer Context](working-with-a-recognizer-context.md).

> \[!Caution\]  
> In managed code, you must call the [Dispose](https://msdn.microsoft.com/library/ms839450(v=MSDN.10).aspx) method on this object before it goes out of scope. This object maintains non-managed resources. Relying on finalization for this object can cause memory leaks and exceptions within your application.

 

 

 



