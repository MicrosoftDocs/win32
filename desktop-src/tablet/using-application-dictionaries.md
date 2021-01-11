---
description: By default, the recognizer uses a system dictionary that contains all of the commonly written words in a language.
ms.assetid: 2ddf04dd-613b-4570-9474-0e33208c4012
title: Using Application Dictionaries
ms.topic: article
ms.date: 05/31/2018
---

# Using Application Dictionaries

By default, the recognizer uses a system dictionary that contains all of the commonly written words in a language. In addition, the recognizer has a user dictionary that contains words that the user has added to the dictionary. Users add a word to the user dictionary through Tablet PC Input Panel through selections in:

-   The alternate list (when writing).
-   The Speech Tools menu (when speaking).

If you are designing an application into which you anticipate the user will write words that are not found in either the system dictionary or the user dictionary, create an application dictionary. An application dictionary further improves recognition accuracy by providing the recognizer with an additional customized list of words likely to be entered as handwriting into an application.

You create an application dictionary by using the [**WordList**](inkwordlist-class.md) object. The ensuing application dictionary increases recognition accuracy by providing the recognizer with a list of expected words. For example, an application dictionary that contains medical terminology increases recognition accuracy within an application developed for the medical industry into which the terms are likely to be written.

As another example, when designing a form for someone to order musical instruments, create a [**WordList**](inkwordlist-class.md) object that contains the names of the most common instrument manufacturers. Set the [**WordList**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_wordlist) property of the [**RecognizerContext**](inkrecognizercontext-class.md) object to the **WordList** object you created. This list of words is then passed to the recognizer by the **RecognizerContext** object. The application dictionary increases recognition accuracy when those names are written in a field in the application.

The following topics describe how to use application dictionaries.

-   [Understanding Word Lists, Recognizer Context, and Factoids](understanding-wordlists--the-recognizercontext--and-factoids.md)
-   [Using Application Dictionaries with the Tablet PC Platform APIs](using-application-dictionaries-with-the-tablet-pc-platform-apis.md)
-   [Creating Custom Dictionaries for Handwriting Recognition](creating-custom-dictionaries-for-handwriting-recognition-in-windows-7-and-windows-server-2008-r2.md)

 

 



