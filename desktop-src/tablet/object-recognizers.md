---
description: In addition to recognizing text, recognizers can recognize a class of related objects.
ms.assetid: 53b6137d-2998-4a3b-b469-3d1204ea194b
title: Object Recognizers
ms.topic: article
ms.date: 05/31/2018
---

# Object Recognizers

In addition to recognizing text, recognizers can recognize a class of related objects. Object recognizers recognize general shapes, according to their purpose. Object recognizers are used to recognize:

-   Musical notes
-   Geometric shapes
-   Math equations
-   Flow chart elements

Usually, the objects that are recognized by such a recognizer are in a two-dimensional spatial or functional relationship with each other. For example, within the complex relationships in a math equation, a recognizer can return different results for an upper limit on a definite integral as opposed to a numerator in a fraction.

Because of the very general nature of these relationships, it is extremely difficult to define the set of interfaces that will work for every object recognizer.

The Tablet PC Technology provides a basic framework for object recognizers in the Managed Library and Automation interfaces. However, you must develop custom interfaces that describe complex spatial relationships between recognized objects for each object recognizer. Specifically, for object recognizers, the platform provides the basic [**RecognizerContext**](inkrecognizercontext-class.md) object for associating the [**Ink**](inkdisp-class.md) object with the recognizer context and for calling the recognizer to perform the recognition.

 

 



