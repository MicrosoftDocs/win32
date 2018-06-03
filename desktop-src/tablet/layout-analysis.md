---
Description: Layout analysis operates on a Strokes collection and classifies the strokes into handwriting and drawing elements. The Divider object provides access to the Tablet PC layout analysis features.
ms.assetid: ac30d5c2-13a1-4f9e-a519-2bf428e21c75
title: Layout Analysis
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Layout Analysis

Layout analysis operates on a [**Strokes**](/windows/desktop/api/msinkaut/) collection and classifies the strokes into handwriting and drawing elements. The [**Divider**](/windows/desktop/api/msinkaut15/) object provides access to the Tablet PC layout analysis features.

The following table describes the structural element types of the [**InkDivisionType**](https://www.bing.com/search?q=**InkDivisionType**) enumeration into which the [**Divider**](/windows/desktop/api/msinkaut15/) object classifies strokes.



| Type          | Description                                                                      |
|---------------|----------------------------------------------------------------------------------|
| **Segment**   | A recognition segment.<br/>                                                |
| **Line**      | A line of handwriting that contains one or more recognition segments.<br/> |
| **Paragraph** | A block of strokes that contains one or more lines of handwriting.<br/>    |
| **Drawing**   | Ink that is not handwriting.<br/>                                          |



 

The [**Divider**](/windows/desktop/api/msinkaut15/) object has a [**Strokes**](/windows/desktop/api/msinkaut/) collection, which the **Divider** object dynamically analyzes each time you add to or delete from the collection. The **Divider** object is not serializable, and you cannot save its analysis state. Thus the **Divider** object is designed for applications that must differentiate between mixed handwriting and drawing input, but do not need to reanalyze large amounts of ink between sessions.

You can obtain a static snapshot of the current analysis result, which is returned in a [**DivisionResult**](/windows/desktop/api/msinkaut15/nn-msinkaut15-iinkdivisionresult) object. You can obtain [**DivisionUnit**](/windows/desktop/api/msinkaut15/nn-msinkaut15-iinkdivisionunit) objects, each which represents a single structural element of a **DivisionResult** object. The **DivisionResult** and **DivisionUnit** objects are not serializable. However, state information from these objects is available.

The [**Divider**](/windows/desktop/api/msinkaut15/) object works only with left-to-right handwriting. For the **Divider** object to analyze vertical languages such as Chinese correctly, the characters must be drawn left-to-right instead of top-to-bottom.

 

 




