---
title: Input Format Enumeration
description: Input Format Enumeration
ms.assetid: 75264598-0226-435a-b71f-6997ff0fcaff
keywords:
- Windows Media Format SDK,input format enumerations
- Windows Media Format SDK,enumerating input formats
- Advanced Systems Format (ASF),input format enumerations
- ASF (Advanced Systems Format),input format enumerations
- Advanced Systems Format (ASF),enumerating input formats
- ASF (Advanced Systems Format),enumerating input formats
- input format enumerations
ms.topic: article
ms.date: 05/31/2018
---

# Input Format Enumeration

The writer object gets stream format information from the profile you give it. Stream configuration information in a profile gives the writer all of the information it needs about how the data is to be written in the file. The profile does not provide the writer with any information about the format of the input samples that your application delivers. Input formats will be unknown only for streams compressed with one of the Windows Media codecs; inputs for arbitrary stream types are predictable based on the information in the profile.

The writer object can communicate with the codec for a stream to determine the input types that can be used. Methods are provided to enumerate the possible input types. You should always find the input type that matches your input media by enumerating the supported types rather than setting the input media properties manually. For more information, see [To Enumerate Input Formats](to-enumerate-input-formats.md).

## Related topics

<dl> <dt>

[**File Writing Features**](file-writing-features.md)
</dt> <dt>

[**Working with Inputs**](working-with-inputs.md)
</dt> </dl>

 

 




