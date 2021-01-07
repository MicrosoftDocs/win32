---
description: The Tablet PC Platform supports a number of factoids that are used to increase recognition accuracy.
ms.assetid: 9d5fc370-ba58-438b-8850-f31f0f0f6608
title: Supported Factoids from Version 1
ms.topic: article
ms.date: 05/31/2018
---

# Supported Factoids from Version 1

\[Note the following description of the factoids supported in version 1 of the Microsoft Windows XP Tablet PC Edition Software Development Kit (SDK) are still supported by recognizers, but it is recommended that all new development (for recognizers of Latin script) use the values defined in the [InputScope](/windows/win32/api/inputscope/ne-inputscope-inputscope) enumeration.\]

The Tablet PC Platform supports a number of factoids that are used to increase recognition accuracy. When using factoids, it is important that the expected input exactly match the definition of the factoid. If the input does not match the definition of the factoid, recognition accuracy suffers. For example, if the **Number** factoid is set and the user enters letters, the recognition accuracy for letters is poor.

Certain factoids, such as **Email** and **Digit**, are almost identical across languages. Other factoids, such as **Telephone** and **PostalCode**, vary by language. Examine the format of each factoid for the language that you are using. A list of formats for each factoid in each language can be found in the tables in the topics following this topic.

> [!Note]  
> There is a subtle but important distinction between factoids for western languages and factoids for East Asian languages. Factoids for western languages are implemented by using expressions that describe the desired result. The recognizer is then biased to produce results that match this expression. Factoids for East Asian languages are implemented by specifying an acceptable range of Unicode characters. For example, the **Date** factoid for East Asian languages accepts only Unicode characters within a certain range.

 

Factoids for western languages include factoids for English (United Kingdom), English (United States), French, German, and Spanish. Factoids for East Asian languages include factoids for Chinese (Simplified), Chinese (Traditional), Japanese, and Korean.

The following sections show the formats supported for each factoid in each language:

-   [Factoids Common Across Languages](factoids-common-across-languages.md)
-   [Factoids for Western Languages](factoids-for-western-languages.md)
-   [Factoids for East Asian Languages](factoids-for-east-asian-languages.md)

If you expect input that is different from the formats listed in the tables in these sections, do not use a factoid. In addition, factoids are built into the recognizer for each language. You cannot use factoids from one language with a recognizer from another language. For example, you cannot use the French **Telephone** factoid with a Japanese recognizer.

## Related topics

<dl> <dt>

[**Factoid Constants**](factoid-constants.md)
</dt> <dt>

[Microsoft.Ink.Factoid Class](/previous-versions/ms583657(v=vs.100))
</dt> </dl>

 

 
