---
Description: Layout analysis operates on a Strokes collection and classifies the strokes into handwriting and drawing elements. The Divider object provides access to the Tablet PC layout analysis features.
ms.assetid: ac30d5c2-13a1-4f9e-a519-2bf428e21c75
title: Layout Analysis
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Layout Analysis

Layout analysis operates on a [**Strokes**](/windows/win32/msinkaut/?branch=master) collection and classifies the strokes into handwriting and drawing elements. The [**Divider**](/windows/win32/msinkaut15/?branch=master) object provides access to the Tablet PC layout analysis features.

The following table describes the structural element types of the [**InkDivisionType**](inkdivisiontype.md) enumeration into which the [**Divider**](/windows/win32/msinkaut15/?branch=master) object classifies strokes.



| Type          | Description                                                                      |
|---------------|----------------------------------------------------------------------------------|
| **Segment**   | A recognition segment.<br/>                                                |
| **Line**      | A line of handwriting that contains one or more recognition segments.<br/> |
| **Paragraph** | A block of strokes that contains one or more lines of handwriting.<br/>    |
| **Drawing**   | Ink that is not handwriting.<br/>                                          |



 

The [**Divider**](/windows/win32/msinkaut15/?branch=master) object has a [**Strokes**](/windows/win32/msinkaut/?branch=master) collection, which the **Divider** object dynamically analyzes each time you add to or delete from the collection. The **Divider** object is not serializable, and you cannot save its analysis state. Thus the **Divider** object is designed for applications that must differentiate between mixed handwriting and drawing input, but do not need to reanalyze large amounts of ink between sessions.

You can obtain a static snapshot of the current analysis result, which is returned in a [**DivisionResult**](/windows/win32/msinkaut15/nn-msinkaut15-iinkdivisionresult?branch=master) object. You can obtain [**DivisionUnit**](/windows/win32/msinkaut15/nn-msinkaut15-iinkdivisionunit?branch=master) objects, each which represents a single structural element of a **DivisionResult** object. The **DivisionResult** and **DivisionUnit** objects are not serializable. However, state information from these objects is available.

The [**Divider**](/windows/win32/msinkaut15/?branch=master) object works only with left-to-right handwriting. For the **Divider** object to analyze vertical languages such as Chinese correctly, the characters must be drawn left-to-right instead of top-to-bottom.

 

 




