---
title: Producing a Dialog Box for Selecting a Format for Saving
description: Producing a Dialog Box for Selecting a Format for Saving
ms.assetid: f833b28c-13e1-497c-bfc4-2e3bc84d7fff
keywords:
- audio compression manager (ACM),producing dialog boxes
- ACM (audio compression manager),producing dialog boxes
- ACM examples,producing dialog boxes
- producing dialog boxes
- acmFormatChoose function
- audio compression manager (ACM),selecting format for saving
- ACM (audio compression manager),selecting format for saving
- ACM examples,selecting format for saving
- selecting format for saving
ms.topic: article
ms.date: 05/31/2018
---

# Producing a Dialog Box for Selecting a Format for Saving

You might want an application to save existing waveform-audio data in another format. For example, a waveform-audio editor could save a waveform-audio file as a compressed file. To list only the suggested destination formats for a specified source format in the dialog box created by the [**acmFormatChoose**](/windows/desktop/api/Msacm/nf-msacm-acmformatchoose) function, specify the source format in the **pwfxEnum** member and the ACM\_FORMATENUMF\_SUGGEST flag in the **fdwEnum** member of the [**ACMFORMATCHOOSE**](/windows/win32/api/msacm/ns-msacm-acmformatchoose) structure.

Similarly, to list valid destination formats for a specified format, use the ACM\_FORMATENUMF\_CONVERT flag instead of the ACM\_FORMATENUMF\_SUGGEST flag.

 

 




