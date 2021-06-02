---
description: The ELS language detection service is called Microsoft Language Detection. This service uses Microsoft-patented technology to allow applications to detect the language in which specific text is written.
ms.assetid: 11438e0b-d841-44d0-b68f-77868be4c92f
title: Microsoft Language Detection
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft Language Detection

The ELS language detection service is called Microsoft Language Detection. This service uses Microsoft-patented technology to allow applications to detect the language in which specific text is written.

## Input to Microsoft Language Detection

The input to the Microsoft Language Detection service is UTF-16 (normalized form C) text. The service has to determine the language for this text.

## Output of Microsoft Language Detection

The Microsoft Language Detection service retrieves a double-null-terminated, registry-formatted UTF-16 string listing languages, represented by their names, separated by null character delimiters. The list is sorted by relevance. For most languages, neutral names are used. However, for some, for example, sr-Cyrl, sr-Latn, zh-Hant, and zh-Hans, full names are used.

## Microsoft Language Detection Operation

The Microsoft Language Detection service checks the Unicode script of the text provided by the application. It segments the text based on the scripts that it detects, and then determines the language in which each segment is written. If a script indicates a single language, the language is guaranteed to be present in the output list of languages. The service uses a patented algorithm to determine the relevance of each supported language.

## Microsoft Language Detection GUID

The GUID for the Microsoft Language Detection service is declared in Elssrvc.h, as shown in the following code.


```C++
// {CF7E00B1-909B-4d95-A8F4-611F7C377702}
static const GUID ELS_GUID_LANGUAGE_DETECTION =
    { 0xCF7E00B1, 0x909B, 0x4D95, { 0xA8, 0xF4, 0x61, 0x1F, 0x7C, 0x37, 0x77, 0x02 } };
```



## Related topics

<dl> <dt>

[About Extended Linguistic Services](about-extended-linguistic-services.md)
</dt> </dl>

 

 



