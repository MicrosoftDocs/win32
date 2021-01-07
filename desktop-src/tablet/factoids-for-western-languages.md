---
description: Western languages are defined as English (United Kingdom), English (United States), French, German, and Spanish.
ms.assetid: d4728506-7484-4c4c-a5ae-e98d699f7e76
title: Factoids for Western Languages
ms.topic: article
ms.date: 05/31/2018
---

# Factoids for Western Languages

Western languages are defined as English (United Kingdom), English (United States), French, German, and Spanish. The formats within each factoid shown in the following table are specific to each language's recognizer. For example, the **Telephone** factoid is different in each language. Furthermore, each factoid is specific to a particular recognizer. For example, the French **Telephone** factoid can be used only with the French recognizer.

> [!Note]  
> In addition to the following factoids, all languages use the factoids listed in [Factoids Common Across Languages](factoids-common-across-languages.md).

 



| Factoid              | Definition                                                                                                                                                                                                                                                                                                                                                                                                           | Examples                                                                                                                                                                                                                                                            |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Filename**         | Sets bias for a file name path. The name cannot include the characters<br/> / " < > \|<br/> The characters \* and ? are included in this factoid to enable searching. Also, extended characters are supported in European languages.<br/>                                                                                                                                                    | c:<br/> \\\\directoryname\\filename<br/> \\\\directory1\\directory2\\filename<br/> \\\\directoryname\\\*.\*<br/> filename.?<br/> myfile.doc<br/>                                                                                |
| **SystemDictionary** | Enables the system dictionary only. This is useful if an application queries whether a word is in the system dictionary. Set the factoid to **SystemDictionary** and call the [**IsStringSupported**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-isstringsupported) method.<br/>                                                                                                                                                 | The default language model includes grammar for the language as well as the system dictionary. This factoid biases recognition toward only the words that occur in the system dictionary. Each language has its own system dictionary.<br/>                   |
| **WordList**         | Enables the word list only. If the factoid is set to **WordList** but no word list is assigned to the [**InkRecognizerContext**](inkrecognizercontext-class.md) ([RecognizerContext](/previous-versions/ms552546(v=vs.100)) in managed code), the user dictionary is used. For more information about word lists and dictionaries, see [Using Application Dictionaries](using-application-dictionaries.md).<br/> | This factoid biases the recognizer toward returning only words in the word list. For example, to enable the user to enter a color into a form, you may use this factoid and a word list that contains "Green", "Red", "Blue", "White", and other colors.<br/> |



 

The following combinations of factoids are supported for western languages only. Other combinations of factoids are not supported in this version of the Tablet PC Platform application programming interfaces (APIs). These factoid combinations employ a logical **OR** operator, therefore the input can match any of the factoids in the expression.



| Factoid Combination     | Definition                                                                   |
|-------------------------|------------------------------------------------------------------------------|
| **WebWordList**         | The **Web** factoid or the word list.<br/>                             |
| **EmailWordList**       | The **Email** factoid or the word list.<br/>                           |
| **FilenameWebWordList** | The **Filename** factoid or the **Web** factoid or the word list.<br/> |



 

The following topics show the formats supported for each western language.

-   [English (Worldwide) Factoids](english--worldwide--factoids.md)
-   [English (United States) Factoids](english--united-states--factoids.md)
-   [French Factoids](french-factoids.md)
-   [German Factoids](german-factoids.md)
-   [Spanish Factoids](spanish-factoids.md)

 

