---
title: Audio Compression Manager Functions and Structures
description: Audio Compression Manager Functions and Structures
ms.assetid: eb00ec23-ecae-4a6c-a767-fa27513c168d
keywords:
- multimedia audio,ACM functions
- audio,ACM functions
- audio compression manager (ACM),functions
- ACM (audio compression manager),functions
- multimedia audio,ACM structures
- audio,ACM structures
- audio compression manager (ACM),structures
- ACM (audio compression manager),structures
- ACM structures
- ACM functions
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Audio Compression Manager Functions and Structures

\[The feature associated with this page, [﻿Audio Compression Manager](/windows/win32/multimedia/audio-compression-manager), is a legacy feature. Microsoft strongly recommends that new code does not use this feature.\]

The ACM functions fall into several categories. Naming conventions for the functions make it easy to identify these categories. Function names (with two exceptions) are of the form *acmGroupFunction*, where *Group* designates the ACM category (such as "Driver," "Format," "FormatTag," "Filter," "FilterTag," or "Stream"), and *Function* describes the action performed by the function.

The functions in the filter and format groups are very similar. Almost every function that acts on filters has a parallel function that acts on formats.

In the format group, some functions use waveform-audio format tags (the **wFormatTag** member of a [**WAVEFORMATEX**](/windows/win32/api/mmeapi/ns-mmeapi-waveformatex) structure) while others require full waveform-audio formats (the full **WAVEFORMATEX** structure). (For reference information about the **WAVEFORMATEX** structure, see [Error](error.md).)

In the filter group, some functions use waveform-audio filter tags (the **dwFilterTag** member of a [**WAVEFILTER**](/windows/desktop/api/Mmreg/ns-mmreg-wavefilter) structure), while others require full waveform-audio filters (the full **WAVEFILTER** structure).

The functions in the stream group represent the many steps involved in a conversion: opening a conversion instance, preparing for the conversion, performing the conversion, cleaning up after the conversion is complete, and closing the conversion instance.

 

 