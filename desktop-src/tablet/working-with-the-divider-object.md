---
Description: The Divider object provides access to the Tablet PC layout analysis features.
ms.assetid: 9fa299fe-3713-4fa8-95c6-be15f144103a
title: Working with the Divider Object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Working with the Divider Object

The [Divider](https://www.bing.com/search?q=Divider) object provides access to the Tablet PC layout analysis features.

In managed code, the [Divider](https://www.bing.com/search?q=Divider) object can be instantiated by calling one of the [Divider](https://www.bing.com/search?q=Divider) constructors. In Automation, this is called the [**InkDivider**](https://msdn.microsoft.com/en-us/library/ms696382(v=VS.85).aspx) object, and it can be instantiated by calling the [**CoCreateInstance**](https://msdn.microsoft.com/en-us/library/ms686615(v=VS.85).aspx) method in C++.

You can obtain a snapshot of the current analysis result by calling the [Divide](https://www.bing.com/search?q=Divide) method of the [Divider](https://www.bing.com/search?q=Divider) object. The analysis result is returned in a [DivisionResult](https://www.bing.com/search?q=DivisionResult) object. Each time you call the Divide method, the Divider object creates a DivisionResult object. For more information about the DivisionResult object, see [Working with the DivisionResult Object](working-with-the-divisionresult-object.md).

The [Strokes](https://www.bing.com/search?q=Strokes) collection that the [Divider](https://www.bing.com/search?q=Divider) object analyzes is contained in the [Strokes](https://www.bing.com/search?q=Strokes) property of the Divider object. The Divider object dynamically analyzes the Strokes collection as you add to or delete from the collection. For more information about the Strokes property of the Divider object, see [Working with a Strokes Collection](working-with-a-strokes-collection.md).

The [Divider](https://www.bing.com/search?q=Divider) object uses a recognizer context to improve its analysis of recognition segments and to generate recognition text for handwriting elements. You can set the recognizer context by using the [RecognizerContext](https://www.bing.com/search?q=RecognizerContext) property of the Divider object. The RecognizerContext property cannot be changed after strokes have been assigned to the Divider object. For more information about the RecognizerContext property of the Divider object, see [Working with a Recognizer Context](working-with-a-recognizer-context.md).

> \[!Caution\]  
> In managed code, you must call the [Dispose](https://www.bing.com/search?q=Dispose) method on this object before it goes out of scope. This object maintains non-managed resources. Relying on finalization for this object can cause memory leaks and exceptions within your application.

 

 

 



