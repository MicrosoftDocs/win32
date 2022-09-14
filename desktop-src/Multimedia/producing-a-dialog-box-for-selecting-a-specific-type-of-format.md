---
title: Producing a Dialog Box for Selecting a Specific Type of Format
description: Producing a Dialog Box for Selecting a Specific Type of Format
ms.assetid: e454f9d6-5cbf-4e1b-937e-771cf1dd38ba
keywords:
- audio compression manager (ACM),producing dialog boxes
- ACM (audio compression manager),producing dialog boxes
- ACM examples,producing dialog boxes
- producing dialog boxes
- acmFormatChoose function
- audio compression manager (ACM),selecting format types
- ACM (audio compression manager),selecting format types
- ACM examples,selecting format types
- selecting format types
ms.topic: article
ms.date: 05/31/2018
---

# Producing a Dialog Box for Selecting a Specific Type of Format

You might want an application to allow the user to select a format from a restricted list of formats in a dialog box. Restrictions might limit the number of channels, the sampling rate, the waveform-audio format tag, or the number of bits per sample. In all of these cases, you can generate the list by using the [**acmFormatChoose**](/windows/desktop/api/Msacm/nf-msacm-acmformatchoose) function, setting the **fdwEnum** and **pwfxEnum** members of the [**ACMFORMATCHOOSE**](/windows/win32/api/msacm/ns-msacm-acmformatchoose) structure. The following example illustrates this process.


```C++
MMRESULT            mmr; 
ACMFORMATCHOOSE     afc; 
WAVEFORMATEX        wfxSelection; 
WAVEFORMATEX        wfxEnum; 
 
// Initialize the ACMFORMATCHOOSE members. 
memset(&afc, 0, sizeof(afc)); 
 
afc.cbStruct    = sizeof(afc); 
afc.fdwStyle    = 0L;               // no special style flags 
afc.hwndOwner   = hwnd;             // hwnd of parent window 
afc.pwfx        = &wfxSelection;    // wfx to receive selection 
afc.cbwfx       = sizeof(wfxSelection); 
afc.pszTitle    = TEXT("16 Bit PCM Selection"); 
 
//  Request that all 16-bit PCM formats be displayed for the user 
//  to select from. 
memset(&wfxEnum, 0, sizeof(wfxEnum)); 
wfxEnum.wFormatTag = WAVE_FORMAT_PCM; 
wfxEnum.wBitsPerSample = 16; 
afc.fdwEnum = ACM_FORMATENUMF_WFORMATTAG | 
    ACM_FORMATENUMF_WBITSPERSAMPLE; 
afc.pwfxEnum = &wfxEnum; 
mmr = acmFormatChoose(&afc); 
if ((MMSYSERR_NOERROR != mmr) && (ACMERR_CANCELED != mmr)) 
{ 
    // There was a fatal error in bringing up the list 
    // dialog box (probably invalid input parameters). 
} 
 
```



 

 




