---
title: Input Formats, Input Settings, and Data Unit Extensions
description: Input Formats, Input Settings, and Data Unit Extensions
ms.assetid: 8e8a0ec8-cb7c-4483-86b0-142ea9f2b835
keywords:
- Windows Media Format SDK,input formats and settings
- Windows Media Format SDK,data unit extensions
- Windows Media Format SDK,payload extension systems
- Advanced Systems Format (ASF),input formats and settings
- ASF (Advanced Systems Format),input formats and settings
- Advanced Systems Format (ASF),data unit extensions
- ASF (Advanced Systems Format),data unit extensions
- Advanced Systems Format (ASF),payload extension systems
- ASF (Advanced Systems Format),payload extension systems
- data unit extensions,about
- payload extension systems
ms.topic: article
ms.date: 05/31/2018
---

# Input Formats, Input Settings, and Data Unit Extensions

The writer object supports input settings, input formats, and data unit extensions, all of which enable you to control features of the writer. It is not always obvious which methods to use to control a specific feature.

Input formats are media formats that describe the basic properties of the media that you pass to the writer for encoding. For example, the frame size and color space of input video is described by the input format.

Input settings are characteristics of the input data beyond the basics, or information about transforms to perform on the data. Interlaced video settings and information about a watermarking system are examples of input settings.

Data unit extensions, also called payload extension systems, are values that are attached to individual samples in the data section of the file. SMPTE time codes and non-square pixel information are examples of data unit extensions.

## Related topics

<dl> <dt>

[**Configuring Data Unit Extensions**](configuring-data-unit-extensions.md)
</dt> <dt>

[**Data Unit Extensions**](data-unit-extensions.md)
</dt> <dt>

[**File Writing Features**](file-writing-features.md)
</dt> <dt>

[**Input Format Enumeration**](input-format-enumeration.md)
</dt> <dt>

[**Input Settings**](input-settings.md)
</dt> <dt>

[**Working with Inputs**](working-with-inputs.md)
</dt> </dl>

 

 




