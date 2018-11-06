---
title: Generating a Nonstandard Format
description: Generating a Nonstandard Format
ms.assetid: e9f80aec-d5dc-4c44-aea0-95220542e48d
keywords:
- audio compression manager (ACM),nonstandard formats
- ACM (audio compression manager),nonstandard formats
- ACM examples,nonstandard formats
- acmFormatSuggest function
ms.topic: article
ms.date: 05/31/2018
---

# Generating a Nonstandard Format

Sometimes an application needs a nonstandard format. For example, an application might need a 16-kHz ADPCM-format file. Because 16 kHz is nonstandard, the enumeration functions will not generate this format. In fact, short of custom coding the format algorithms into the application, there is no reliable way to generate a nonstandard format. It is sometimes possible, however, to generate an analogous format by setting up a valid PCM format with all the required information and then using the [**acmFormatSuggest**](/windows/desktop/api/Msacm/nf-msacm-acmformatsuggest) function. Because compressors and decompressors try to suggest a format that is closest to the desired format, the number of channels and frequency are usually preserved.

 

 




