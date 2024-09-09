---
title: Multistep Format Conversion
description: Multistep Format Conversion
ms.assetid: 21d837e7-d665-461d-9676-68add3829fb0
keywords:
- audio compression manager (ACM),converting data
- ACM (audio compression manager),converting data
- ACM examples,converting data
- converting data
- acmFormatSuggest function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Multistep Format Conversion

\[The feature associated with this page, [﻿Audio Compression Manager](/windows/win32/multimedia/audio-compression-manager), is a legacy feature. Microsoft strongly recommends that new code does not use this feature.\]

Sometimes the ACM cannot convert data from one format to another in a single step. For example, an application might need to convert 16-bit, 44-kHz stereo data to 11-kHz mono ADPCM. If the compressor or decompressor cannot do this conversion directly, the application might attempt it in two steps. This usually means making one conversion between two PCM formats, then another conversion to the final format type.

To convert in two steps, use the [**acmFormatSuggest**](/windows/desktop/api/Msacm/nf-msacm-acmformatsuggest) function to find a PCM format that matches the ADPCM format. Then use two conversion streams to perform the conversion. For example, perform one conversion from 16-bit, 44-kHz stereo PCM to 16-bit, 11-kHz mono, then convert from 16-bit, 11-kHz mono to 11-kHz mono ADPCM.

Multistep conversion also happens when either the source or the destination format is not PCM. If the source format is not PCM, it should be changed to a PCM format before conversion. If the destination format is not PCM, the source must be converted to an intermediate PCM format and then converted to the final destination format.

The most straightforward conversions occur when the source and destination formats are both PCM formats. When either the source or destination format is not PCM, the conversion might require an additional step. If both source and destination formats are not PCM, the conversion will usually require more than one step, and, in some instances, conversion might not be possible.

 

 




