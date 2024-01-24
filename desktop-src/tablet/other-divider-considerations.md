---
description: 'Consider the following when deciding when and how to use the Divider object in an application:'
ms.assetid: 17404789-7f08-4cf1-88f8-e1f70296c163
title: Other Divider Considerations
ms.topic: article
ms.date: 05/31/2018
---

# Other Divider Considerations

Consider the following when deciding when and how to use the [**Divider**](inkdivider-class.md) object in an application:

-   The [**Divider**](inkdivider-class.md) object is designed to separate drawings and blocks of handwriting, but not to recognize higher levels of structure, such as tables or columns.
-   The [**Divider**](inkdivider-class.md) object does not provide interfaces specifically for correction of results of layout analysis.
-   The use of timeout and number of stroke heuristics to add or remove multiple strokes at a time from the strokes in the [**Divider**](inkdivider-class.md) object may improve performance.

## Reanalysis Considerations

If you are considering using the [**Divider**](inkdivider-class.md) object in an application where the **Divider** object may have to reanalyze large amounts of ink, keep the following in mind.

### Retaining Copies of Ink and Strokes

An application can keep copies of [**Ink**](inkdisp-class.md) and [**DivisionResult**](/windows/desktop/api/msinkaut15/nn-msinkaut15-iinkdivisionresult) objects for application elements that may be revisited later in the application session. This eliminates the need to reanalyze the **Ink** object if the user returns to the element. This approach trades off memory for better performance.

### Data Reduction Heuristics

You may be able to record the analysis results as application data, and implement heuristics to determine when to reanalyze a set of strokes. This practice would reduce the need to reanalyze all the ink in the application between application sessions. However, care must be taken to preserve structural element boundaries or to reanalyze all the strokes for affected elements.

## Related topics

<dl> <dt>

[**InkDivider Class**](inkdivider-class.md)
</dt> <dt>

[Microsoft.Ink.Divider Class](/previous-versions/ms583616(v=vs.100))
</dt> </dl>

 

 
