---
description: Tablet PC includes technology for recognizing ink input that is most commonly in the form of handwriting.
ms.assetid: 614971a8-2b56-40d4-abb6-aba5ded01883
title: About Handwriting Recognition
ms.topic: article
ms.date: 05/31/2018
---

# About Handwriting Recognition

Tablet PC includes technology for recognizing ink input that is most commonly in the form of handwriting. The software module that provides the recognition is called a recognizer. A recognizer recognizes one language, a group of related languages, or a class of related objects such as musical notes, system gestures, or geometric shapes. You can dynamically add recognizers to the ink services system.

## Recognition Steps

Recognition is handled through the use of a recognizer context. Recognition consists of four basic steps:

1.  Setting up the recognition constraints by:
    -   Selecting the recognizer and input mode (geometric constraints).
    -   Setting the language constraints. For example, you can restrict input to alphanumeric characters or you can pass schemas to assist the recognizer.
2.  Sending ink to the recognizer.
3.  Processing the input (recognizing).
4.  Returning the results of the recognition.

Steps 2 and 3 may be repeated in a loop, or all of the ink strokes may be added to the ink before recognition is attempted.

## Samples and Related Topics

[Advanced Recognition Sample](advanced-recognition-sample.md) demonstrates how to use recognizers with [**Ink**](inkdisp-class.md) objects to perform ink recognition.

[Recognizer DLL Sample Template](recognizer-dll-sample-template.md) contains a template for creating a recognizer DLL. The template contains functions for registering and unregistering the server, as well as skeletons for primary recognizer functions.

The following sections describe the basic concepts behind the Tablet PC recognition technology. For detailed information about creating custom recognizers, see [Creating a Recognizer](creating-a-recognizer.md).

-   [Text Recognizers](text-recognizers.md)
-   [Object Recognizers](object-recognizers.md)
-   [Using the Recognizers Collection](using-the-recognizers-collection.md)
-   [Recognizer Context](recognizer-context.md)
-   [Recognition Segments](recognition-segments.md)
-   [Recognition of Angled Text](recognition-of-angled-text.md)
-   [Recognizer Stroke Reordering Support](recognizer-stroke-reordering-support.md)
-   [Dictionaries and Factoids](dictionaries-and-factoids.md)
-   [Confidence Property \[About Recognition\]](confidence-property--about-recognition.md)
-   [Alternates](alternates.md)
-   [Ink Segments and Alternates](ink-segments-and-alternates.md)

 

 



