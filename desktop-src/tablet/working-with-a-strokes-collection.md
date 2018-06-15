---
Description: The Strokes collection that the Divider object analyzes is kept in the Strokes property of the Divider object.
ms.assetid: c2def964-6f2d-4b79-bfbf-a6719baf3c13
title: Working with a Strokes Collection
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Working with a Strokes Collection

The [**Strokes**](https://msdn.microsoft.com/en-us/library/ms703293(v=VS.85).aspx) collection that the [**Divider**](https://msdn.microsoft.com/en-us/library/ms696382(v=VS.85).aspx) object analyzes is kept in the [**Strokes**](https://msdn.microsoft.com/en-us/library/ms698600(v=VS.85).aspx) property of the **Divider** object. Because a **Strokes** collection is a reference to ink data and is not the actual data itself, changes in the parent [**Ink**](https://msdn.microsoft.com/en-us/library/ms704893(v=VS.85).aspx) object of the **Strokes** collection can invalidate the **Strokes** collection. For more information about ink data, see [Ink Data](ink-data.md). For more information about ink collection, see [Ink Collection](ink-collection.md).

To keep the [**Strokes**](https://msdn.microsoft.com/en-us/library/ms698600(v=VS.85).aspx) property of the [**Divider**](https://msdn.microsoft.com/en-us/library/ms696382(v=VS.85).aspx) object synchronized with an [**Ink**](https://msdn.microsoft.com/en-us/library/ms704893(v=VS.85).aspx) object, use the [**InkAdded**](inkdisp-inkadded.md) and [**InkDeleted**](inkdisp-inkdeleted.md) events of the **Ink** object to listen for strokes that should be added or removed from the **Divider** object. This covers cases where strokes are added to, deleted from, clipped, or split within the **Ink** object. Moving, scaling, or other transformations on strokes in the **Ink** object do not generate **InkAdded** or **InkDeleted** events. To reflect such a transformation in the **Strokes** property of the **Divider** object, perform the same transformation on the strokes in the **Divider** object.

The [**Strokes**](/windows/desktop/api/msinkaut15/nf-msinkaut15-iinkdivisionresult-get_strokes) property of the [**DivisionResult**](/windows/desktop/api/msinkaut15/nn-msinkaut15-iinkdivisionresult) object contains a copy of the strokes in the [**Divider**](https://msdn.microsoft.com/en-us/library/ms696382(v=VS.85).aspx) object at the time the **DivisionResult** object was created. You can compare the **Strokes** properties of two **DivisionResult** objects to determine if the strokes have changed between the two times the [**Divide**](https://msdn.microsoft.com/en-us/library/ms702500(v=VS.85).aspx) method was called.

The [**Strokes**](/windows/desktop/api/msinkaut15/nf-msinkaut15-iinkdivisionunit-get_strokes) property of the [**DivisionUnit**](/windows/desktop/api/msinkaut15/nn-msinkaut15-iinkdivisionunit) object contains the subset of the strokes in the [**DivisionResult**](/windows/desktop/api/msinkaut15/nn-msinkaut15-iinkdivisionresult) object that correspond to this element. You can pass these strokes to a separate [**RecognizerContext**](https://msdn.microsoft.com/en-us/library/ms696371(v=VS.85).aspx) to get a recognition result for the element. Since handwriting elements exist at different levels of detail, the [**Strokes**](https://msdn.microsoft.com/en-us/library/ms703293(v=VS.85).aspx) collections for different elements may overlap. For example, the **Strokes** collection for a recognition segment element will be a subset of the **Strokes** collection for the line element of which the recognition segment is a part.

 

 



