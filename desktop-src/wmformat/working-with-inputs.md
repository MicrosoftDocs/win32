---
title: Working with Inputs
description: Working with Inputs
ms.assetid: 72daa7ca-4264-46bf-91ac-8b95fdbfd41c
keywords:
- Windows Media Format SDK,working with inputs
- Advanced Systems Format (ASF),working with inputs
- ASF (Advanced Systems Format),working with inputs
- profiles,working with inputs
- streams,working with inputs
- codecs,working with inputs
ms.topic: article
ms.date: 05/31/2018
---

# Working with Inputs

Just as the proper stream configuration in the profile is required to get the codec to compress a stream, you must also ensure that the type of uncompressed media you pass to the writer is accurately described. Every Windows Media codec has an associated default input type, but several input types are supported. You can examine the supported inputs and select the one that matches your data. The process of working with inputs is summarized in the following steps:

1.  When you load a profile for the writer to use, the writer object assigns an input number for each connection in the profile. For more information about loading profiles for the writer, see [To Use Profiles with the Writer](to-use-profiles-with-the-writer.md). Unless you are using mutual exclusion by bit rate, there is one connection for each stream. Streams that are mutually exclusive by bit rate share a single connection.
2.  Your application should identify the input numbers for the file. For more information about identifying input numbers, see [To Identify Inputs By Number](to-identify-inputs-by-number.md).
3.  For each input, you should ensure that the input format matches your data. You can enumerate the input formats supported by the SDK. For more information, see [To Enumerate Input Formats](to-enumerate-input-formats.md). You cannot enumerate the input formats of arbitrary streams or streams that are already compressed. For more information about these special cases, see [Arbitrary and Precompressed Stream Inputs](arbitrary-and-precompressed-stream-inputs.md).
4.  Assign the correct input format for each connection. For more information, see [Assigning Input Formats](assigning-input-formats.md).
5.  Some codec and writer features are configured at encoding time instead of in the profile. To configure these features, you must use input settings. For more information, see [To Set Input Settings](to-set-input-settings.md).

## Related topics

<dl> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




