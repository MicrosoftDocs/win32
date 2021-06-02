---
description: A recognizer may find several ways to break an ink sample into recognition segments. Because of this, the number of recognition alternates may be staggering, even for a small ink sample.
ms.assetid: 7ecffe3f-cbe4-4e65-a1cc-9b08534b26c9
title: Ink Segments and Alternates
ms.topic: article
ms.date: 05/31/2018
---

# Ink Segments and Alternates

A recognizer may find several ways to break an ink sample into recognition segments. Because of this, the number of recognition alternates may be staggering, even for a small ink sample.

For example, "t o g e t h e r" can yield the following results:

-   "to get her" (plus alternates for each word)
-   "to gather" (plus alternates for each word)
-   "tog ether" (plus alternates for each word)
-   "tog at her" (plus alternates for each word)
-   "together" (plus alternates for the word)

The [**RecognitionResult**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognitionresult) object supports efficient storage of full recognition results within the [**Ink**](inkdisp-class.md) object. The **Ink** object maps the recognition alternates to the strokes in the **Ink** object and may also contain other information such as baseline position, line indices, and language ranges.

 

 



