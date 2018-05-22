---
Description: 'The DivisionResult object represents a snapshot of the layout analysis of the strokes contained by the Divider object. It contains the stroke classification and grouping information from the layout analysis.'
ms.assetid: '2bcf5223-7bf4-420c-8f04-a972f04f262d'
title: Working with the DivisionResult Object
---

# Working with the DivisionResult Object

The **DivisionResult** object represents a snapshot of the layout analysis of the strokes contained by the **Divider** object. It contains the stroke classification and grouping information from the layout analysis.

You can get information from the **DivisionResult** object by structural element type, such as drawing or lines of handwriting. The **DivisionResult** object can persist after the **Divider** object is destroyed. In Automation, this object is called the [**IInkDivisionResult Interface**](iinkdivisionresult.md) object.

The [**Strokes**](iinkdivisionresult-strokes.md) property of the **DivisionResult** object contains a copy of the **Strokes** collection in the **Divider** object at the time the **DivisionResult** object was created.

The [**InkDivisionType**](inkdivisiontype.md) enumeration defines the structural element types that the layout analysis recognizes.

The [**ResultByType**](iinkdivisionresult-resultbytype.md) method of the **DivisionResult** object returns a **DivisionUnits** collection that contains all structural elements of a given type. An individual structural element is represented by a **DivisionUnit** object. Each time you call the **ResultByType** method, the **DivisionResult** object creates a **DivisionUnits** collection. For more information about the **DivisionUnit** object, see [Working with the DivisionUnit Object](working-with-the-divisionunit-object.md).

 

 



