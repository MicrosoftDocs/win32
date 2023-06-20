---
title: Finding a Specific Format
description: Finding a Specific Format
ms.assetid: 0c892758-d409-4ed7-8f38-a24eee646b65
keywords:
- audio compression manager (ACM),finding formats
- ACM (audio compression manager),finding formats
- ACM examples,finding formats
- finding formats
- acmFormatEnum function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Finding a Specific Format

\[The feature associated with this page, [﻿Audio Compression Manager](/windows/win32/multimedia/audio-compression-manager), is a legacy feature. Microsoft strongly recommends that new code does not use this feature.\]

An application might have only a partial specification for a format when it needs the full specification. For example, the specification might stipulate an 11-kHz mono, 4-bit ADPCM format, but not the average bytes per second. The application can get the full format without user intervention by using the [**acmFormatEnum**](/windows/desktop/api/Msacm/nf-msacm-acmformatenum) function and specifying flags in the *fdwEnum* parameter.

 

 




