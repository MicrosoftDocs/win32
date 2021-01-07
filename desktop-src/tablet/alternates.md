---
description: An alternate is a potential word match for a recognition segment. A recognizer generates alternates and bases them on acceptable matches of the ink or audio input against a dictionary or factoid.
ms.assetid: 69327f1d-f240-4b8a-8bee-0a96a0c425c2
title: Alternates
ms.topic: article
ms.date: 05/31/2018
---

# Alternates

An alternate is a potential word match for a recognition segment. A recognizer generates alternates and bases them on acceptable matches of the ink or audio input against a dictionary or factoid.

> [!Note]  
> Confidence evaluation is currently available only for the Microsoft English (United States) and gesture recognizers.

 

Sometimes the ink may have ambiguous distinctions between segments. The recognizer compares these segments to a recognizer dictionary to determine possible matches. When the recognizer compares the segments, it maintains a list of possible alternate matches and assigns a confidence level to each one, picking a top choice.

> [!Note]  
> The recognizer cannot provide alternates for a portion of ink that is smaller than a recognition segment.

 

 

 



