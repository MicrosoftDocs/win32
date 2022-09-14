---
description: A recognition segment is the basic ink unit that a recognizer uses internally to produce a recognition result for a particular Ink object.
ms.assetid: 5215a0bd-6dff-4cda-b2e5-c54f64680e02
title: Recognition Segments
ms.topic: article
ms.date: 05/31/2018
---

# Recognition Segments

A recognition segment is the basic ink unit that a recognizer uses internally to produce a recognition result for a particular Ink object. A recognition segment is a collection of ink strokes. For example, a recognizer that is capable of recognizing English cursive handwriting might use a word as the basic recognition segment.

Other recognizers may use parts of composite words as basic segments. For example, in Spanish, short words are commonly combined to provide longer composite words. "Damelo" is a Spanish word that is composed of three words "da me lo" (give me that), but it is written as a single word. A Spanish recognizer could recognize each subword as a segment.

A recognizer may find several ways to break an ink sample into recognition segments. Because ambiguity is involved in recognizing the user's intended input, the recognizer can return many alternate matches.

For more information about alternates, see [Alternates](alternates.md).

 

 



