---
title: Producing a Dialog Box for Selecting a Format for Recording
description: Producing a Dialog Box for Selecting a Format for Recording
ms.assetid: e94ca8da-4ee6-4362-a144-27b86f2cadac
keywords:
- audio compression manager (ACM),producing dialog boxes
- ACM (audio compression manager),producing dialog boxes
- ACM examples,producing dialog boxes
- producing dialog boxes
- acmFormatChoose function
- audio compression manager (ACM),selecting format for recoding
- ACM (audio compression manager),selecting format for recoding
- ACM examples,selecting format for recoding
- selecting format for recoding
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Producing a Dialog Box for Selecting a Format for Recording

\[The feature associated with this page, [﻿Audio Compression Manager](/windows/win32/multimedia/audio-compression-manager), is a legacy feature. Microsoft strongly recommends that new code does not use this feature.\]

An application can allow the user to select a format for which an installed waveform-audio device provides native support. For example, you might want a waveform-audio editor to record new waveform-audio data without using an ACM compressor or decompressor to provide a translation layer. To do this, use the [**acmFormatChoose**](/windows/desktop/api/Msacm/nf-msacm-acmformatchoose) function, specifying the ACM\_FORMATENUMF\_HARDWARE and ACM\_FORMATENUMF\_INPUT flags in the **fdwEnum** member of the [**ACMFORMATCHOOSE**](/windows/win32/api/msacm/ns-msacm-acmformatchoose) structure.

 

 




