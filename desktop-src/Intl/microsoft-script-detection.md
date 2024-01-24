---
description: The ELS script detection service is called Microsoft Script Detection.
ms.assetid: daf9f549-1eff-4666-b777-227ec31fba30
title: Microsoft Script Detection
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft Script Detection

The ELS script detection service is called Microsoft Script Detection. This service allows applications to detect the scripts in which text is written. The National Language Support (NLS) counterpart of a script detection service is the [GetStringScripts](/windows/desktop/api/Winnls/nf-winnls-getstringscripts) function. However, the ELS service additionally retrieves the text ranges that belong to each writing system.

## Input to Microsoft Script Detection

The input to the Microsoft Script Detection service is UTF-16 text for which the service determines script ranges.

## Output of Microsoft Script Detection

The output of the Microsoft Script Detection service is an array of ranges, each containing a null-terminated UTF-16 string with the Unicode-specified name of the associated writing system. The service reports regular common (Zyyy) and inherited (Qaai) characters as belonging to the previous script range. Beginning common and inherited characters are reported as belonging to the next script range. If all the characters in the input text are common or inherited, the output of the service is a single range with the empty string as its data.

## Microsoft Script Detection Operation

The Microsoft Script Detection service maps the code points belonging to the common range to the preceding writing system. Alternatively, the service can map the code points to the next writing system if the code points are at the beginning of the input string. The application does not have to deal with the common range at all.

## Microsoft Script Detection GUID

The GUID for the Microsoft Language Detection service is declared in Elssrvc.h, as shown in the following code.


```C++
// {2D64B439-6CAF-4f6b-B688-E5D0F4FAA7D7}
static const GUID ELS_GUID_SCRIPT_DETECTION =
    { 0x2D64B439, 0x6CAF, 0x4F6B, { 0xB6, 0x88, 0xE5, 0xD0, 0xF4, 0xFA, 0xA7, 0xD7 } };
```



## Related topics

<dl> <dt>

[About Extended Linguistic Services](about-extended-linguistic-services.md)
</dt> </dl>

 

 



