---
description: To obtain a level of confidence for each recognition result, you can get either the Confidence property of the RecognitionAlternate object or the Confidence property of the Gesture object.
ms.assetid: b2495c5b-6db4-401c-ab7a-6556c55bbe46
title: Confidence Property [About Recognition]
ms.topic: article
ms.date: 05/31/2018
---

# Confidence Property \[About Recognition\]

To obtain a level of confidence for each recognition result, you can get either the [**Confidence**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognitionalternate-get_confidence) property of the [**RecognitionAlternate**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognitionalternate) object or the [**Confidence**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkgesture-get_confidence) property of the [**Gesture**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkgesture) object. The confidence level is a number that indicates the degree of confidence for each alternate recognition result that the recognizer returns for a corresponding recognition segment.

Confidence is returned as low, average, or high. The application uses these results to:

-   Indicate to the user that multiple possibilities exist.
-   Rank the alternates by confidence level.

## What Affects Confidence

Some of the things that make handwriting recognition difficult and affect confidence include:

-   Difficulty determining word segmentation

![image showing writing that is too close](images/5c5d1c42-cbd1-46d0-a6f8-653f204f52cd.jpg)

-   Case difficulties

![image showing difficulties with handwritten versions of the word "case"](images/1bdfb2e3-06ac-4c49-a39b-f0be51aed0e8.jpg)

-   Uncommon writing styles
-   Isolated punctuation

![image showing quotation marks that are too far away from text](images/743364b3-af62-4775-9d0d-f13f6e36c922.jpg)

-   Accented characters in English recognizers

> [!Note]  
> Confidence evaluation is available only for United States English and all gesture recognizers in this release. Methods that provide the confidence property for any other recognizer will return **E\_NOTIMPL**.

 

 

 



