---
description: The DivisionUnit object represents a single structural element of a DivisionResult object. A DivisionUnit object may represent a drawing, a single recognition segment of handwriting, a line of handwriting, or a block of handwriting.
ms.assetid: 13f6121c-2b83-4788-9d06-460dc03094bf
title: Working with the DivisionUnit Object
ms.topic: article
ms.date: 05/31/2018
---

# Working with the DivisionUnit Object

The **DivisionUnit** object represents a single structural element of a **DivisionResult** object. A **DivisionUnit** object may represent a drawing, a single recognition segment of handwriting, a line of handwriting, or a block of handwriting.

The [**InkDivisionType**](/windows/win32/api/msinkaut15/ne-msinkaut15-inkdivisiontype) enumeration defines the structural element types that the layout analysis recognizes. In Automation, the **DivisionUnit** object is called [**IInkDivisionUnit**](/windows/desktop/api/msinkaut15/nn-msinkaut15-iinkdivisionunit).

The [**DivisionType**](/windows/desktop/api/msinkaut15/nf-msinkaut15-iinkdivisionunit-get_divisiontype) property of the **DivisionUnit** object returns the structural element type that the **DivisionUnit** object is. The [**RecognitionString**](/previous-versions/windows/desktop/legacy/ms703283(v=vs.85)) property of the **DivisionUnit** object returns the recognition text for handwriting elements, or **NULL** for drawing elements.

The [**Strokes**](/windows/desktop/api/msinkaut15/nf-msinkaut15-iinkdivisionunit-get_strokes) property of the **DivisionUnit** object contains the subset of the strokes in the **DivisionResult** object that correspond to this element. Because handwriting elements exist for different levels of detail, the **Strokes** collections for different elements may overlap. Specifically, a recognition segment shares strokes with the line and block it is part of, and a line shares strokes with the block it is part of.

The [**RotationTransform**](/windows/desktop/api/msinkaut15/nf-msinkaut15-iinkdivisionunit-get_rotationtransform) property of the **DivisionUnit** object returns a matrix for rotating the strokes of the element to horizontal. For paragraph and drawing elements the **RotationTransform** property returns the identity matrix. A text recognizer performs much better on handwriting that is horizontally aligned than it does on handwriting that is not. In Automation, this is called the **RotationTransform** property, and it returns an [**InkTransform**](inktransform-class.md) object which contains the transformation matrix. The **RotationTransform** property returns **NULL** for paragraph and drawing elements.

For more information about the **DivisionResult** object, see [Working with the DivisionResult Object](working-with-the-divisionresult-object.md).

 

 
